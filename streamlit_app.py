import streamlit as st

# Define Complyt's branding colors
PRIMARY_COLOR = "#0047AB"  # Deep Blue
SECONDARY_COLOR = "#0084FF"  # Lighter Blue
ACCENT_COLOR = "#00C9A7"  # Greenish-Teal
BACKGROUND_COLOR = "#F5F7FA"  # Light Grayish Blue

# Set page config
st.set_page_config(page_title="Complyt Onboarding", page_icon="🚀", layout="wide")

# Custom CSS to enhance the UI
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}
        .css-1aumxhk {{
            color: {PRIMARY_COLOR} !important;
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR} !important;
            color: white !important;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
        }}
        .stButton>button:hover {{
            background-color: {SECONDARY_COLOR} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.image("https://your-logo-url.com", width=200)  # Add Complyt logo (replace URL)
st.sidebar.title("🚀 Complyt Onboarding")
page = st.sidebar.radio("Navigate", ["Welcome", "Company Details", "Tax Setup", "Review & Submit"])

# Main Page Content
st.title("Welcome to Complyt Onboarding 🎉")
st.write("Get started with your tax compliance setup in just a few easy steps.")

if page == "Welcome":
    st.subheader("🚀 Let's get started")
    st.write("This onboarding tool will help you configure your Complyt account step by step.")

    st.image("https://your-welcome-image-url.com", use_column_width=True)  # Add a welcome image

    if st.button("Start Onboarding"):
        st.sidebar.radio("Navigate", ["Company Details"])

elif page == "Company Details":
    st.subheader("🏢 Company Information")
    st.text_input("Company Name")
    st.text_input("Business Type")
    st.text_input("EIN / Tax ID")

elif page == "Tax Setup":
    st.subheader("📑 Tax Configuration")
    st.selectbox("Primary Tax Jurisdiction", ["United States", "Canada", "Europe"])
    st.checkbox("Enable Automatic Tax Calculation")
    st.text_area("Additional Tax Notes")

elif page == "Review & Submit":
    st.subheader("✅ Review Your Information")
    st.write("Please review your details before submitting.")

    if st.button("Submit"):
        st.success("🎉 Your onboarding is complete! A Complyt representative will be in touch.")

# Footer
st.markdown("---")
st.markdown("💡 Powered by **Complyt** | Simplifying Tax Compliance")
