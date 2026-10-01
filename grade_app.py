import streamlit as st
import pandas as pd

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Student Grade Dashboard",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------------
# Custom CSS
# -----------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 20px;
    }

    .student-count {
        text-align: center;
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------
# Initialize Session State
# -----------------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------------
# Grade Function
# -----------------------------------
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# -----------------------------------
# Header
# -----------------------------------
st.markdown(
    '<div class="title">🎓 Student Grade Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Add students, calculate grades, and view class performance'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------------
# Add Student Form
# -----------------------------------
st.markdown("### ➕ Add Student")

with st.form("student_form"):

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

    with col2:
        mark_input = st.text_input(
            "Mark",
            placeholder="Enter mark (0-100)"
        )

    with col3:
        st.write("")
        st.write("")
        submitted = st.form_submit_button(
            "➕ Add Student",
            use_container_width=True
        )


# -----------------------------------
# Add Student Validation
# -----------------------------------
if submitted:

    # Check student name
    if not name.strip():
        st.warning("⚠️ Please enter the student's name.")

    # Check mark is a number
    else:
        try:
            mark = float(mark_input)

            # Check for negative marks
            if mark < 0:
                st.warning(
                    "⚠️ Negative marks are not allowed. "
                    "Please enter a mark between 0 and 100."
                )

            # Check marks above 100
            elif mark > 100:
                st.warning(
                    "⚠️ Marks cannot be greater than 100. "
                    "Please enter a mark between 0 and 100."
                )

            # Valid mark
            else:
                student = {
                    "Name": name.strip(),
                    "Mark": mark,
                    "Grade": calculate_grade(mark)
                }

                st.session_state.students.append(student)

                st.success(
                    f"✅ {name.strip()} added successfully!"
                )

        except ValueError:
            st.warning(
                "⚠️ Invalid mark. Please enter a number between 0 and 100."
            )


# -----------------------------------
# Class Statistics
# -----------------------------------
if st.session_state.students:

    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    class_average = sum(marks) / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    st.markdown("### 📊 Class Performance")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "📈 Class Average",
            f"{class_average:.2f}"
        )

    with metric2:
        st.metric(
            "🏆 Highest Mark",
            f"{highest_mark:g}"
        )

    with metric3:
        st.metric(
            "📉 Lowest Mark",
            f"{lowest_mark:g}"
        )


    # -----------------------------------
    # Student Table
    # -----------------------------------
    st.markdown("### 📋 Student List")

    df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    # -----------------------------------
    # Student Count
    # -----------------------------------
    st.markdown(
        f"""
        <div class="student-count">
            👨‍🎓 Total Students: <strong>{len(st.session_state.students)}</strong>
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------
    # Clear Students
    # -----------------------------------
    if st.button(
        "🗑️ Clear All Students",
        use_container_width=True
    ):
        st.session_state.students = []
        st.rerun()

else:

    st.info(
        "👋 No students added yet. "
        "Use the form above to add your first student."
    )