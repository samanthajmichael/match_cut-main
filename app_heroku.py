import os
import streamlit as st

# Get the port from Heroku's environment variable
port = int(os.environ.get("PORT", 8501))

if __name__ == '__main__':
    st.set_page_config(page_title="Match Cut")
    # Import your main app file
    import app
