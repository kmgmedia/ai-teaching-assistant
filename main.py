"""
AI Teaching Assistant - Main Application
Flask backend that serves API endpoints for lesson generation, report writing, and parent communication.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import settings
from core.logic.lesson_generator import generate_lesson
from core.logic.report_generator import generate_report
from core.logic.parent_writer import generate_parent_message
from integrations.google_sheets import read_student_data, get_student_by_name, write_report_to_sheet
from utils.helpers import setup_logger

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Set up logging
logger = setup_logger(__name__)


@app.route('/')
def home():
    """Health check endpoint."""
    return jsonify({
        "status": "running",
        "message": "AI Teaching Assistant API",
        "endpoints": {
            "lesson": "/generate/lesson",
            "report": "/generate/report",
            "parent_message": "/generate/parent-message",
            "students": "/students",
            "student": "/students/<name>"
        }
    })


@app.route('/generate/lesson', methods=['POST'])
def create_lesson():
    """
    Generate a lesson note.
    
    Expected JSON body:
    {
        "subject": "Mathematics",
        "topic": "Addition",
        "age_group": "5-6 years",
        "objectives": "Students will...",
        "duration": 60
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required = ['subject', 'topic', 'age_group', 'objectives']
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        result = generate_lesson(
            subject=data['subject'],
            topic=data['topic'],
            age_group=data['age_group'],
            objectives=data['objectives'],
            duration=data.get('duration', 60)
        )
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    except Exception as e:
        logger.error(f"Error in /generate/lesson: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/generate/report', methods=['POST'])
def create_report():
    """
    Generate a student progress report.
    
    Expected JSON body:
    {
        "student_name": "Emma Johnson",
        "period": "Term 1",
        "subject": "Overall Progress",
        "performance_notes": "...",
        "behavior_notes": "...",
        "save_to_sheets": false
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required = ['student_name', 'period', 'subject', 'performance_notes', 'behavior_notes']
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        result = generate_report(
            student_name=data['student_name'],
            period=data['period'],
            subject=data['subject'],
            performance_notes=data['performance_notes'],
            behavior_notes=data['behavior_notes']
        )
        
        # Optionally save to Google Sheets
        if result['success'] and data.get('save_to_sheets', False):
            try:
                write_report_to_sheet(
                    report_text=result['report'],
                    student_name=data['student_name']
                )
                result['saved_to_sheets'] = True
            except Exception as e:
                logger.warning(f"Failed to save to sheets: {e}")
                result['saved_to_sheets'] = False
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    except Exception as e:
        logger.error(f"Error in /generate/report: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/generate/parent-message', methods=['POST'])
def create_parent_message():
    """
    Generate a parent communication message.
    
    Expected JSON body:
    {
        "purpose": "reminder|feedback|appreciation|concern",
        "child_name": "Liam Chen",
        "context": "Details about the message...",
        "teacher_name": "Ms. Thompson"
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required = ['purpose', 'child_name', 'context']
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        result = generate_parent_message(
            purpose=data['purpose'],
            child_name=data['child_name'],
            context=data['context'],
            teacher_name=data.get('teacher_name', '')
        )
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    except Exception as e:
        logger.error(f"Error in /generate/parent-message: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/students', methods=['GET'])
def list_students():
    """
    Get all students from Google Sheets.
    """
    try:
        students = read_student_data()
        return jsonify({
            "success": True,
            "count": len(students),
            "students": students
        }), 200
    
    except Exception as e:
        logger.error(f"Error in /students: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/students/<student_name>', methods=['GET'])
def get_student(student_name):
    """
    Get specific student data by name.
    """
    try:
        student = get_student_by_name(student_name)
        
        if student:
            return jsonify({
                "success": True,
                "student": student
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": f"Student '{student_name}' not found"
            }), 404
    
    except Exception as e:
        logger.error(f"Error in /students/<name>: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    logger.info(f"Starting AI Teaching Assistant on {settings.FLASK_HOST}:{settings.FLASK_PORT}")
    app.run(
        host=settings.FLASK_HOST,
        port=settings.FLASK_PORT,
        debug=settings.FLASK_DEBUG
    )
