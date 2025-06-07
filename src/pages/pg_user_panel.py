import streamlit as st

st.title("👤 User Panel")
st.markdown("**User Management and Profile Settings**")

st.info("🚧 User Panel - Coming Soon!")

# Mock user info
with st.sidebar:
    st.header("User Info")
    st.text("Logged in as: John Doe")
    st.text("Role: Standard User")
    st.button("Logout")

# Mock user content
st.subheader("User Profile")
col1, col2 = st.columns(2)

with col1:
    st.text_input("Full Name", value="John Doe")
    st.text_input("Email", value="john.doe@mim3.com")

with col2:
    st.selectbox("Department", ["Sales", "Marketing", "IT", "Finance"])
    st.selectbox("Office Location", ["Jakarta", "Surabaya", "Medan"])

st.button("Update Profile")

st.subheader("Recent Activity")
st.text("Last login: 2024-01-01 09:30:00")
st.text("Reports generated: 5")
st.text("Data downloads: 3")
