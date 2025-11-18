"""
AI Teaching Assistant - Streamlit Dashboard
User-friendly interface for teachers to generate lesson notes, reports, and parent messages.
"""
import streamlit as st
import sys
import os
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.logic.lesson_generator import generate_lesson
from core.logic.report_generator import generate_report
from core.logic.parent_writer import generate_parent_message
from integrations.google_sheets import read_student_data, get_student_by_name, write_report_to_sheet

# Page configuration
st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PERFORMANCE OPTIMIZATION: Data Caching
# =====================================================

@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_students_cached():
    """
    Load student data with caching to avoid repeated API calls.
    Cache refreshes every 5 minutes.
    """
    try:
        return read_student_data()
    except Exception as e:
        st.error(f"Failed to load students: {e}")
        return []

@st.cache_data(ttl=300)
def get_student_cached(student_name):
    """
    Get individual student data with caching.
    """
    try:
        return get_student_by_name(student_name)
    except Exception as e:
        st.error(f"Failed to load student {student_name}: {e}")
        return None

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = None

# Header
st.markdown('<h1 class="main-header">🎓 AI Teaching Assistant</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar navigation
st.sidebar.title("📋 Navigation")
page = st.sidebar.radio(
    "Choose a tool:",
    ["🏠 Home", "📝 Lesson Generator", "📊 Report Generator", "💌 Parent Message", "👥 View Students"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip**: All generated content is automatically saved to the `data/output/` folder!")


# HOME PAGE
if page == "🏠 Home":
    st.header("Welcome to Your AI Teaching Assistant! 👋")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 What Can I Do?")
        st.markdown("""
        - **📝 Generate Lesson Notes**: Create structured, engaging lesson plans
        - **📊 Write Student Reports**: Professional progress reports in seconds
        - **💌 Draft Parent Messages**: Personalized communication templates
        - **👥 Manage Students**: View and access student data from Google Sheets
        """)
    
    with col2:
        st.subheader("🚀 Quick Start")
        st.markdown("""
        1. **Select a tool** from the sidebar
        2. **Fill in the details** (or pull from Google Sheets)
        3. **Click Generate** and get instant results!
        4. **Copy or download** your content
        """)
    
    st.markdown("---")
    
    # Quick stats
    st.subheader("📈 Quick Stats")
    try:
        students = load_students_cached()  # Use cached data
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Students", len(students))
        
        with col2:
            avg_score = sum([s.get('Score', 0) for s in students]) / len(students) if students else 0
            st.metric("Average Score", f"{avg_score:.1f}")
        
        with col3:
            subjects = set([s.get('Subject', '') for s in students])
            st.metric("Subjects", len(subjects))
            
    except Exception as e:
        st.warning(f"⚠️ Unable to load student data: {str(e)}")


# LESSON GENERATOR PAGE
elif page == "📝 Lesson Generator":
    st.header("📝 Lesson Note Generator")
    st.markdown("Create structured, age-appropriate lesson plans")
    
    col1, col2 = st.columns(2)
    
    with col1:
        subject = st.text_input("Subject *", placeholder="e.g., Mathematics, Science")
        topic = st.text_input("Topic *", placeholder="e.g., Introduction to Fractions")
        age_group = st.text_input("Age Group *", placeholder="e.g., 7-8 years (Grade 2)")
    
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=15, max_value=180, value=60, step=15)
        objectives = st.text_area(
            "Learning Objectives *",
            placeholder="e.g., Students will understand what fractions are and identify halves and quarters",
            height=100
        )
    
    st.markdown("---")
    
    if st.button("🚀 Generate Lesson Note", type="primary", width="stretch"):
        if not subject or not topic or not age_group or not objectives:
            st.error("❌ Please fill in all required fields (marked with *)")
        else:
            with st.spinner("✨ Generating your lesson note..."):
                try:
                    result = generate_lesson(subject, topic, age_group, objectives, duration)
                    
                    if result['success']:
                        st.success("✅ Lesson note generated successfully!")
                        st.markdown("### 📄 Your Lesson Note:")
                        st.markdown(result['lesson_note'])
                        
                        # Download button
                        st.download_button(
                            label="⬇️ Download as Text File",
                            data=result['lesson_note'],
                            file_name=f"lesson_{subject}_{topic}.txt".replace(" ", "_"),
                            mime="text/plain"
                        )
                        
                        st.info(f"💾 Saved to: `{result['metadata']['output_file']}`")
                    else:
                        st.error(f"❌ Error: {result.get('error', 'Unknown error')}")
                        
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")


# REPORT GENERATOR PAGE
elif page == "📊 Report Generator":
    st.header("📊 Student Report Generator")
    st.markdown("Create professional progress reports")
    
    # Option to load from Google Sheets
    use_sheets = st.checkbox("📊 Load student data from Google Sheets", value=True)
    
    if use_sheets:
        try:
            students = load_students_cached()  # Use cached data
            
            # Get unique student names
            import pandas as pd
            df_all = pd.DataFrame(students)
            unique_students = sorted(df_all['Name'].unique()) if 'Name' in df_all.columns else []
            
            selected_student = st.selectbox("Select Student *", unique_students)
            
            if selected_student:
                # Get all records for this student
                student_records = df_all[df_all['Name'] == selected_student] if 'Name' in df_all.columns else pd.DataFrame()
                
                # Aggregate data for the report
                all_subjects = student_records['Subject'].tolist() if 'Subject' in student_records.columns else []
                all_notes = student_records['Notes'].tolist() if 'Notes' in student_records.columns else []
                all_behaviors = student_records['Behavior'].tolist() if 'Behavior' in student_records.columns else []
                
                # Combine notes and behaviors
                combined_notes = "\n".join([f"- {subj}: {note}" for subj, note in zip(all_subjects, all_notes)])
                combined_behavior = "\n".join([f"- {subj}: {beh}" for subj, beh in zip(all_subjects, all_behaviors)])
                
                col1, col2 = st.columns(2)
                
                with col1:
                    student_name = st.text_input("Student Name *", value=selected_student)
                    period = st.text_input("Period *", value="Term 1 (2025)", placeholder="e.g., Term 1, Q2 2025")
                    subject = st.text_input("Subject *", value="Overall Progress", placeholder="e.g., Overall Progress or specific subject")
                
                with col2:
                    performance_notes = st.text_area(
                        "Performance Notes * (All Subjects)",
                        value=combined_notes if combined_notes else "No performance notes available",
                        height=150,
                        placeholder="Academic observations and achievements"
                    )
                    behavior_notes = st.text_area(
                        "Behavior Notes * (All Subjects)",
                        value=combined_behavior if combined_behavior else "No behavior notes available",
                        height=150,
                        placeholder="Social-emotional and behavioral observations"
                    )
                    save_to_sheets = st.checkbox("💾 Save report back to Google Sheets", value=True)
        
        except Exception as e:
            st.error(f"❌ Unable to load students from Google Sheets: {str(e)}")
            use_sheets = False
    
    if not use_sheets:
        col1, col2 = st.columns(2)
        
        with col1:
            student_name = st.text_input("Student Name *", placeholder="e.g., Emma Johnson")
            period = st.text_input("Period *", placeholder="e.g., Term 1, Q2 2025")
            subject = st.text_input("Subject *", placeholder="e.g., Overall Progress, Math")
        
        with col2:
            performance_notes = st.text_area(
                "Performance Notes *",
                height=100,
                placeholder="Academic observations and achievements"
            )
            behavior_notes = st.text_area(
                "Behavior Notes *",
                height=100,
                placeholder="Social-emotional and behavioral observations"
            )
            save_to_sheets = False
    
    st.markdown("---")
    
    if st.button("🚀 Generate Report", type="primary", width="stretch"):
        if not student_name or not period or not subject or not performance_notes or not behavior_notes:
            st.error("❌ Please fill in all required fields (marked with *)")
        else:
            with st.spinner("✨ Generating your report..."):
                try:
                    result = generate_report(student_name, period, subject, performance_notes, behavior_notes)
                    
                    if result['success']:
                        st.success("✅ Report generated successfully!")
                        st.markdown("### 📄 Progress Report:")
                        st.markdown(result['report'])
                        
                        # Save to sheets if requested
                        if save_to_sheets:
                            try:
                                write_report_to_sheet(result['report'], student_name)
                                st.success("✅ Report saved to Google Sheets!")
                            except Exception as e:
                                st.warning(f"⚠️ Could not save to sheets: {str(e)}")
                        
                        # Download button
                        st.download_button(
                            label="⬇️ Download Report",
                            data=result['report'],
                            file_name=f"report_{student_name}_{period}.txt".replace(" ", "_"),
                            mime="text/plain"
                        )
                        
                        st.info(f"💾 Saved to: `{result['metadata']['output_file']}`")
                    else:
                        st.error(f"❌ Error: {result.get('error', 'Unknown error')}")
                        
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")


# PARENT MESSAGE PAGE
elif page == "💌 Parent Message":
    st.header("💌 Parent Communication Writer")
    st.markdown("Draft personalized messages for parents")
    
    col1, col2 = st.columns(2)
    
    with col1:
        purpose = st.selectbox(
            "Message Purpose *",
            ["appreciation", "reminder", "feedback", "concern"],
            help="What is the main purpose of this message?"
        )
        child_name = st.text_input("Child's Name *", placeholder="e.g., Emma Johnson")
    
    with col2:
        teacher_name = st.text_input("Your Name", placeholder="e.g., Ms. Sarah Thompson")
        context = st.text_area(
            "Message Context *",
            height=150,
            placeholder="Provide details about what you want to communicate...\n\nExamples:\n- For appreciation: What did the student do well?\n- For reminder: What event/deadline/requirement?\n- For feedback: What progress or area to discuss?\n- For concern: What issue needs addressing?"
        )
    
    st.markdown("---")
    
    if st.button("🚀 Generate Message", type="primary", width="stretch"):
        if not purpose or not child_name or not context:
            st.error("❌ Please fill in all required fields (marked with *)")
        else:
            with st.spinner("✨ Crafting your message..."):
                try:
                    result = generate_parent_message(purpose, child_name, context, teacher_name)
                    
                    if result['success']:
                        st.success("✅ Message generated successfully!")
                        st.markdown("### 💌 Your Message:")
                        st.markdown(result['message'])
                        
                        # Copy to clipboard helper
                        st.code(result['message'], language=None)
                        
                        # Download button
                        st.download_button(
                            label="⬇️ Download Message",
                            data=result['message'],
                            file_name=f"parent_message_{purpose}_{child_name}.txt".replace(" ", "_"),
                            mime="text/plain"
                        )
                        
                        st.info(f"💾 Saved to: `{result['metadata']['output_file']}`")
                    else:
                        st.error(f"❌ Error: {result.get('error', 'Unknown error')}")
                        
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")


# VIEW STUDENTS PAGE
elif page == "👥 View Students":
    st.header("👥 Student Data")
    st.markdown("View and manage your students from Google Sheets")
    
    # Add refresh button at the top
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        if st.button("🔄 Refresh Data", help="Clear cache and reload from Google Sheets"):
            st.cache_data.clear()
            st.success("Cache cleared! Reloading...")
            st.rerun()
    
    try:
        students = load_students_cached()  # Use cached data
        
        if students:
            # Get unique student names
            import pandas as pd
            df_all = pd.DataFrame(students)
            unique_students = df_all['Name'].unique() if 'Name' in df_all.columns else []
            
            st.success(f"✅ Found {len(unique_students)} students with {len(students)} total subject records")
            
            # Option to toggle view
            view_mode = st.radio(
                "📊 View Mode:",
                ["Student Summary", "All Subject Records"],
                horizontal=True,
                help="Summary shows each student once with averages. Records shows all subject entries."
            )
            
            if view_mode == "Student Summary":
                # Aggregate data by student
                if 'Name' in df_all.columns and 'Score' in df_all.columns:
                    summary = df_all.groupby('Name').agg({
                        'Score': 'mean',
                        'Subject': lambda x: ', '.join(x.unique()[:3]) + ('...' if len(x.unique()) > 3 else ''),
                        'Behavior': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'N/A'
                    }).reset_index()
                    summary.columns = ['Name', 'Average Score', 'Subjects', 'Overall Behavior']
                    summary['Average Score'] = summary['Average Score'].round(1)
                    st.dataframe(summary, width="stretch", hide_index=True)
                else:
                    st.warning("Missing required columns (Name, Score) in your sheet")
            else:
                # Show all records
                st.dataframe(df_all, width="stretch", hide_index=True)
            
            st.markdown("---")
            
            # Individual student view with ALL subjects
            st.subheader("🔍 View Individual Student")
            selected_name = st.selectbox("Select a student", sorted(unique_students))
            
            if selected_name:
                # Get all records for this student
                student_records = df_all[df_all['Name'] == selected_name] if 'Name' in df_all.columns else pd.DataFrame()
                
                if not student_records.empty:
                    # Show student overview
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("📛 Name", selected_name)
                    with col2:
                        avg_score = student_records['Score'].mean() if 'Score' in student_records.columns else 0
                        st.metric("📊 Average Score", f"{avg_score:.1f}")
                    with col3:
                        num_subjects = len(student_records)
                        st.metric("📚 Subjects", num_subjects)
                    
                    st.markdown("---")
                    st.markdown("### 📚 Subject Breakdown")
                    
                    # Display each subject
                    for idx, record in student_records.iterrows():
                        with st.expander(f"**{record.get('Subject', 'N/A')}** - Score: {record.get('Score', 'N/A')}", expanded=False):
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.markdown("**📝 Notes:**")
                                st.info(record.get('Notes', 'No notes available'))
                            
                            with col2:
                                st.markdown("**🎭 Behavior:**")
                                behavior = record.get('Behavior', 'N/A')
                                if behavior == 'Excellent':
                                    st.success(behavior)
                                elif behavior == 'Good':
                                    st.info(behavior)
                                else:
                                    st.warning(behavior)
                                
                                if 'Attendance' in record:
                                    st.markdown(f"**📅 Attendance:** {record.get('Attendance', 'N/A')}")
                else:
                    st.error(f"No data found for {selected_name}")
                    
                    # Quick actions
                    st.markdown("---")
                    st.markdown("**⚡ Quick Actions:**")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("📊 Generate Report for This Student"):
                            st.session_state.page = "📊 Report Generator"
                            st.rerun()
                    
                    with col2:
                        if st.button("💌 Send Parent Message"):
                            st.session_state.page = "💌 Parent Message"
                            st.rerun()
        else:
            st.warning("⚠️ No students found in your Google Sheet")
            st.info("💡 Add students to your Google Sheet in the 'Students' tab")
            
    except Exception as e:
        st.error(f"❌ Unable to load students: {str(e)}")
        st.info("💡 Make sure your Google Sheets integration is properly configured")


# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ for educators | AI Teaching Assistant v1.0</p>
    </div>
    """,
    unsafe_allow_html=True
)
