import streamlit as st
import pandas as pd
import requests

# Complyt Nexa Colors
PRIMARY_COLOR = "#0047AB"  # Deep Blue
SECONDARY_COLOR = "#0084FF"  # Lighter Blue
ACCENT_COLOR = "#00C9A7"  # Greenish-Teal
BACKGROUND_COLOR = "#F5F7FA"  # Light Grayish Blue

# Streamlit Config
st.set_page_config(page_title="Nexa - Nexus Analyzer", page_icon="⚡", layout="wide")

# Custom CSS for styling
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
            padding: 10px 20px;
        }}
        .stButton>button:hover {{
            background-color: {SECONDARY_COLOR} !important;
        }}
        .uploadedFile {{"color: {PRIMARY_COLOR} !important;"}}
        footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            text-align: center;
            padding: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.image("https://complyt.io/wp-content/uploads/2024/03/LOGO.svg", width=200)
st.sidebar.title("⚡ Nexa - Nexus Analyzer")
page = st.sidebar.radio(
    "Navigate",
    [
        "Welcome",
        "Process Overview",
        "Step 1: Upload Physical Nexus",
        "Step 2: Product Classification",
        "Step 3: Upload Exempt Customers",
        "Step 4: Data Validation",
        "Step 5: Start Nexus Analysis"
    ]
)

# Welcome Page
if page == "Welcome":
    st.title("🚀 Welcome to Nexa - The Nexus Analyzer")
    st.write(
        "Nexa helps businesses analyze tax nexus exposure efficiently. "
        "Follow these steps to ensure compliance and optimize tax reporting."
    )

    # Load and display uploaded image
    local_image_path = "/mnt/data/image.png"
    st.image(local_image_path, use_container_width=True)

    if st.button("Start Now"):
        st.sidebar.radio("Navigate", ["Process Overview"])

# Process Overview
elif page == "Process Overview":
    st.title("🛠 How Nexa Works")
    st.markdown(
        """
        Nexa follows a structured approach to analyze **sales tax nexus and exposure**:
        1. **Upload Physical Nexus** 🏢 - List states where your company has a physical presence.
        2. **Product Classification** 📦 - Assign Complyt tax codes to your products.
        3. **Upload Exempt Customers** 📜 - Identify customers that qualify for tax exemptions.
        4. **Data Validation** 🔍 - Ensure data integrity before analysis.
        5. **Run Nexus Analysis** ⚡ - Generate an exposure report.

        ---
        **Let's get started!**
        """
    )

# Step 1: Upload Physical Nexus
elif page == "Step 1: Upload Physical Nexus":
    st.title("🏢 Upload Physical Nexus")
    st.write("Upload a CSV file with a list of states where your business has a physical presence.")

    uploaded_file = st.file_uploader("Upload Nexus File (CSV)", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.success("✅ File uploaded successfully!")

# Step 2: Product Classification with PC BOT
elif page == "Step 2: Product Classification":
    st.title("📦 Product Classification")
    st.write(
        "Upload your product list and classify them using Complyt tax codes. "
        "You can use PC BOT to assist with classification."
    )

    product_file = st.file_uploader("Upload Product List (CSV)", type=["csv"])
    if product_file:
        df = pd.read_csv(product_file)
        st.dataframe(df)

        st.write("🧠 **PC BOT: AI-Powered Product Classification**")
        user_input = st.text_input("Describe the product (e.g., 'Cloud-based SaaS subscription')")
        if st.button("Classify Product"):
            classification = "Digital Services - Software (Complyt Tax Code: DS100)"
            st.success(f"✅ PC BOT Suggests: {classification}")

# Step 3: Upload Exempt Customers
elif page == "Step 3: Upload Exempt Customers":
    st.title("📜 Upload Exempt Customers")
    st.write("Upload a CSV file containing a list of tax-exempt customers.")

    exempt_file = st.file_uploader("Upload Exempt Customers List (CSV)", type=["csv"])
    if exempt_file:
        df = pd.read_csv(exempt_file)
        st.dataframe(df)
        st.success("✅ Exempt customers uploaded successfully!")

# Step 4: Data Validation (API Call)
elif page == "Step 4: Data Validation":
    st.title("🔍 Data Validation")
    st.write("Upload your dataset for validation. The system will analyze missing fields and errors.")

    validation_file = st.file_uploader("Upload Data File for Validation (CSV)", type=["csv"])
    
    if validation_file:
        st.write("Processing file... 📤")
        response = requests.post(
            "https://your-cloud-function-url.com/validate",
            files={"file": validation_file.getvalue()}
        )
        
        if response.status_code == 200:
            validation_result = response.json()
            st.success("✅ Data validation complete!")
            st.json(validation_result)
        else:
            st.error("❌ Validation failed. Please check the file format.")

# Step 5: Initiate Nexus Analysis
elif page == "Step 5: Start Nexus Analysis":
    st.title("⚡ Initiate Nexus Analysis")
    st.write(
        "Click the button below to analyze your data and generate the **Nexus Exposure Report**."
    )

    if st.button("Run Nexus Analysis"):
        st.write("📡 **Running Analysis...**")
        analysis_response = requests.post("https://your-cloud-function-url.com/analyze")
        
        if analysis_response.status_code == 200:
            st.success("✅ Nexus Analysis Completed! Download your report.")
            st.download_button("Download Report", analysis_response.content, "nexus_report.pdf")
        else:
            st.error("❌ Analysis Failed. Try again later.")

# Footer (Ensures it is on every page)
st.markdown("---")
st.markdown(
    "<footer>💡 Powered by <b>Complyt</b> | Simplifying Tax Compliance</footer>",
    unsafe_allow_html=True
)
