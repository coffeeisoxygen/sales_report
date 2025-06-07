import streamlit as st

st.title("📊 MIM3 Dashboard")
st.markdown("**Monitoring Dashboard Terpadu untuk MIM3 Indonesia**")

st.info("🚧 Dashboard Utama - Coming Soon!")

# Mock sidebar content
with st.sidebar:
    st.header("Dashboard Controls")
    st.selectbox("Filter by Region:", ["All", "Jakarta", "Surabaya", "Medan"])
    st.date_input("Select Date Range:")
    st.button("Refresh Data")

# Mock main content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", "Rp 10.5M", "12%")

with col2:
    st.metric("Active Users", "1,234", "5%")

with col3:
    st.metric("Conversion Rate", "3.2%", "-2%")

st.subheader("Sample Chart")
st.line_chart({"Sales": [1, 3, 2, 4, 5, 3, 6]})
