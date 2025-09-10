import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="DAXI",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
    .stButton > button
     {
        background-color: #4c4f52;
        color: white;
    }
    .stButton > button:hover {
        background-color: #F79B72;
    }
    </style>
""", unsafe_allow_html=True)


# --- UI Layout ---

st.title("DAXI")

# Sidebar for project management
with st.sidebar:
    
    st.subheader("Create New Project")
    st.text_input("Project Name", key="new_project_name", help="Leave blank for a default name.")
   




