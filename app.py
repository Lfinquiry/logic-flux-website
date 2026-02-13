import streamlit as st
from PIL import Image
import requests

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Logic Flux | AI Automation",
    page_icon="⚡",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FAFAFA; }
    h1 { font-family: 'Helvetica Neue', sans-serif; font-weight: 700; color: #00B4D8; }
    .stButton>button { 
        background-color: #00B4D8; 
        color: white; 
        width: 100%; 
        border-radius: 5px; 
        font-weight: bold; 
        border: none;
        padding: 10px;
    }
    .stButton>button:hover { background-color: #0096B4; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { 
        background-color: #262730; 
        color: white; 
        border-radius: 5px;
    }
    a { color: #00B4D8 !important; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.header("Logic-Flux.in")

st.markdown("<h1 style='text-align: center; margin-top: -20px;'>Logic Meets Motion.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #909090; font-weight: 300; font-size: 1.2rem;'>Premium AI Automation & Digital Systems</h3>", unsafe_allow_html=True)
st.divider()

# --- SERVICES ---
c1, c2 = st.columns(2)
with c1:
    st.subheader("🚀 For Businesses")
    st.markdown("""
    * **AI Agents:** 24/7 intelligent customer bots.
    * **Workflow Automation:** Eliminate manual data entry.
    * **Data Systems:** Smart, organized business intelligence.
    """)
with c2:
    st.subheader("⚡ The Technology")
    st.markdown("""
    * **Python Logic:** Custom-built, scalable code.
    * **Cloud Integration:** Seamless data flux across apps.
    * **Live Dashboards:** Visualize your growth in real-time.
    """)
st.divider()

# --- CONTACT FORM ---
st.markdown("<h3 style='text-align: center;'>Start Your Transformation</h3>", unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns([1, 1.5])

with contact_col1:
    st.info("📧 **Direct Contact**")
    st.markdown("""
    **Business Inquiries:**
    [inquiry@logic-flux.in](mailto:inquiry@logic-flux.in)
    
    **Office Hours:**
    Mon-Fri, 9am - 6pm IST
    
    **Response Time:**
    Within 24 Hours
    """)

with contact_col2:
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Project Details or Inquiry")
        submit = st.form_submit_button("Send Request 🚀")

        if submit:
            if not name or not email or not message:
                st.warning("⚠️ Please fill out all fields.")
            else:
                # --- THE BUSINESS ENGINE ---
                # 👇 TARGET IS NOW YOUR PROFESSIONAL EMAIL 👇
                target_email = "inquiry@logic-flux.in"  
                
                url = f"https://formsubmit.co/{target_email}"
                
                data = {
                    "name": name,
                    "email": email,
                    "message": message,
                    "_subject": f"New Lead: {name}",
                    "_captcha": "false",
                    "_template": "table"
                }
                
                # THE SECRET HANDSHAKE (Required for success)
                headers = {
                    "Referer": "https://logic-flux.in"
                }
                
                try:
                    response = requests.post(url, data=data, headers=headers)
                    
                    if response.status_code == 200:
                        st.success("✅ Inquiry Received! The Logic Flux Team will be in touch.")
                        st.toast("Request Sent Successfully!", icon="🚀")
                    else:
                        st.error("❌ Technical error. Please email us directly.")
                except Exception as e:
                    st.error(f"Connection Error: {e}")