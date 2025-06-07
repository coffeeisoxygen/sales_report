import streamlit as st

# Define pages
dashboard_page = st.Page(
    "pages/pg_dashboard.py", title="Dashboard Utama", icon="🏠", default=True
)
etl_page = st.Page("pages/pg_etl_process.py", title="ETL Data Process", icon="⚙️")
user_page = st.Page("pages/pg_user_panel.py", title="User Panel", icon="👤")
admin_page = st.Page("pages/pg_admin_panel.py", title="Admin Panel", icon="🔐")

# Create navigation with sections
pg = st.navigation({
    "Main": [dashboard_page],
    "Data Management": [etl_page],
    "User Management": [user_page, admin_page],
})

# Set page config
st.set_page_config(
    page_title="MIM3 Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Run the selected page
pg.run()
