"""
Google Sheets Integration
Handles reading from and writing to Google Sheets for student data.
OPTIMIZED: Uses singleton pattern for client reuse.
"""
import os
import gspread
from google.oauth2.service_account import Credentials
from config import settings
from utils.helpers import setup_logger
from functools import lru_cache

logger = setup_logger(__name__)

# Google Sheets API scopes
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Global client cache (singleton pattern)
_sheets_client = None


def _load_local_credentials():
    """Load credentials from local JSON file for development."""
    if not settings.GOOGLE_SHEETS_CREDENTIALS:
        raise ValueError("GOOGLE_SHEETS_CREDENTIALS not set in .env file")
    
    if not os.path.exists(settings.GOOGLE_SHEETS_CREDENTIALS):
        raise FileNotFoundError(
            f"Credentials file not found: {settings.GOOGLE_SHEETS_CREDENTIALS}"
        )
    
    credentials = Credentials.from_service_account_file(
        settings.GOOGLE_SHEETS_CREDENTIALS,
        scopes=SCOPES
    )
    logger.info("Using local credentials file for authentication")
    return credentials


@lru_cache(maxsize=1)
def get_sheets_client():
    """
    Authenticate and return a Google Sheets client.
    Uses singleton pattern to reuse the same client across calls.
    Supports both local development (JSON file) and Streamlit Cloud (secrets.toml).
    
    Returns:
        gspread.Client: Authenticated gspread client
    
    Raises:
        Exception: If authentication fails
    """
    global _sheets_client
    
    # Return cached client if available
    if _sheets_client is not None:
        return _sheets_client
    
    try:
        # Check if running on Streamlit Cloud
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and 'gcp_service_account' in st.secrets:
                # Use Streamlit Cloud secrets
                credentials = Credentials.from_service_account_info(
                    st.secrets["gcp_service_account"],
                    scopes=SCOPES
                )
                logger.info("Using Streamlit Cloud secrets for authentication")
            else:
                # Local development - use JSON file
                credentials = _load_local_credentials()
        except (ImportError, AttributeError):
            # Not in Streamlit context - use local credentials
            credentials = _load_local_credentials()
        
        # Authorize and cache client
        _sheets_client = gspread.authorize(credentials)
        logger.info("Google Sheets client authenticated successfully")
        
        return _sheets_client
    
    except Exception as e:
        logger.error(f"Failed to authenticate Google Sheets client: {e}")
        raise


def get_sheet(sheet_id=None, sheet_name=None):
    """
    Get a specific worksheet by ID and optional sheet name.
    
    Args:
        sheet_id (str): Google Sheet ID (from URL). Uses settings.GOOGLE_SHEET_ID if None
        sheet_name (str): Name of the specific sheet/tab (optional, defaults to first sheet)
    
    Returns:
        gspread.Worksheet: The requested worksheet
    """
    client = get_sheets_client()
    
    sheet_id = sheet_id or settings.GOOGLE_SHEET_ID
    if not sheet_id:
        raise ValueError("No sheet_id provided and GOOGLE_SHEET_ID not set in .env")
    
    try:
        spreadsheet = client.open_by_key(sheet_id)
        
        if sheet_name:
            worksheet = spreadsheet.worksheet(sheet_name)
        else:
            worksheet = spreadsheet.sheet1  # First sheet
        
        logger.info(f"Opened worksheet: {worksheet.title}")
        return worksheet
    
    except Exception as e:
        logger.error(f"Failed to open worksheet: {e}")
        raise


def read_student_data(sheet_id=None, sheet_name="Students"):
    """
    Read all student data from a Google Sheet.
    Expects columns: Name, Subject, Score, Notes, Behavior
    
    Args:
        sheet_id (str): Google Sheet ID
        sheet_name (str): Name of the sheet tab (default: "Students")
    
    Returns:
        list[dict]: List of student records as dictionaries
    """
    try:
        worksheet = get_sheet(sheet_id, sheet_name)
        
        # Get all records (first row as headers)
        records = worksheet.get_all_records()
        
        logger.info(f"Retrieved {len(records)} student records")
        return records
    
    except Exception as e:
        logger.error(f"Failed to read student data: {e}")
        raise


def write_report_to_sheet(report_text, student_name, sheet_id=None, sheet_name="Reports"):
    """
    Write a generated report back to Google Sheets.
    
    Args:
        report_text (str): The generated report content
        student_name (str): Name of the student
        sheet_id (str): Google Sheet ID
        sheet_name (str): Name of the sheet tab (default: "Reports")
    
    Returns:
        bool: True if successful
    """
    try:
        worksheet = get_sheet(sheet_id, sheet_name)
        
        # Find the next empty row
        next_row = len(worksheet.col_values(1)) + 1
        
        # Get current timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write data: [Student Name, Report, Timestamp]
        worksheet.update(f'A{next_row}:C{next_row}', [[student_name, report_text, timestamp]])
        
        logger.info(f"Report written to sheet for {student_name} at row {next_row}")
        return True
    
    except Exception as e:
        logger.error(f"Failed to write report to sheet: {e}")
        raise


def get_student_by_name(student_name, sheet_id=None, sheet_name="Students"):
    """
    Fetch data for a specific student by name.
    
    Args:
        student_name (str): Name of the student to find
        sheet_id (str): Google Sheet ID
        sheet_name (str): Name of the sheet tab
    
    Returns:
        dict: Student data, or None if not found
    """
    try:
        records = read_student_data(sheet_id, sheet_name)
        
        for record in records:
            if record.get("Name", "").lower() == student_name.lower():
                logger.info(f"Found student: {student_name}")
                return record
        
        logger.warning(f"Student not found: {student_name}")
        return None
    
    except Exception as e:
        logger.error(f"Failed to fetch student by name: {e}")
        raise


if __name__ == "__main__":
    # Test Google Sheets connection
    try:
        print("Testing Google Sheets connection...")
        client = get_sheets_client()
        print("✅ Connection successful!")
        
        # Try reading student data if GOOGLE_SHEET_ID is set
        if settings.GOOGLE_SHEET_ID:
            students = read_student_data()
            print(f"✅ Found {len(students)} student records")
            if students:
                print(f"Sample: {students[0]}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
