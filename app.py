import streamlit as st

# 1. PAGE CONFIGURATION (Must be the very first Streamlit command)
st.set_page_config(
    page_title="Logic Flux | AI Automation Agency",
    page_icon="⚡",
    layout="wide", # 'wide' uses the whole screen, looks much more professional
    initial_sidebar_state="collapsed"
)

# 2. CUSTOM CSS (The Secret Sauce)
# This hides Streamlit's default junk and styles our buttons
custom_css = """
<style>
    /* Hide the Streamlit Top Menu and Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style the main container to look like a modern website */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Custom glowing text effect for the main title */
    .hero-title {
        font-size: 4rem !important;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .hero-subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #A0AEC0;
        margin-top: 10px;
        margin-bottom: 50px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown('<p class="hero-title">Automate the Impossible.</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Logic Flux builds custom AI agents and workflows to scale your business on autopilot.</p>', unsafe_allow_html=True)

# 4. ACTION BUTTONS (Centered)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.button("Book a Free AI Audit 🚀", use_container_width=True, type="primary")

st.divider()

# --- The rest of your content (Services, Contact, etc.) goes below here ---

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
                 

st.divider()

# --- RULE-BASED CHATBOT SECTION ---
st.markdown("<h3 style='text-align: center;'>🤖 Logic Flux Assistant</h3>", unsafe_allow_html=True)

# 1. Setup the "Brain" state
if "chat_step" not in st.session_state:
    st.session_state.chat_step = "greeting"

# 2. The Chat Container
chat_container = st.container()

with chat_container:
    # --- STEP 1: GREETING & OPTIONS ---
    if st.session_state.chat_step == "greeting":
        with st.chat_message("assistant"):
            st.write("Welcome to Logic Flux! I'm here to help you automate your business. What would you like to know?")
            
            # Create clickable option buttons
            col1, col2, col3 = st.columns(3)
            if col1.button("🛠️ What services do you offer?", use_container_width=True):
                st.session_state.chat_step = "services"
                st.rerun()
            if col2.button("💰 How much does it cost?", use_container_width=True):
                st.session_state.chat_step = "pricing"
                st.rerun()
            if col3.button("📅 I want to book a call", use_container_width=True):
                st.session_state.chat_step = "contact"
                st.rerun()

    # --- STEP 2: RESPONSES ---
    
    # If they clicked Services
    elif st.session_state.chat_step == "services":
        with st.chat_message("user"):
            st.write("What services do you offer?")
        with st.chat_message("assistant"):
            st.write("""
            **We specialize in three main areas:**
            1. **Custom AI Chatbots:** For customer support and lead generation.
            2. **Workflow Automation:** Connecting your apps so you don't have to do manual data entry.
            3. **Internal AI Assistants:** Tools trained on your company data to help your team work faster.
            """)
            if st.button("⬅️ Back to Menu"):
                st.session_state.chat_step = "greeting"
                st.rerun()

    # If they clicked Pricing
    elif st.session_state.chat_step == "pricing":
        with st.chat_message("user"):
            st.write("How much does it cost?")
        with st.chat_message("assistant"):
            st.write("Every business is unique! We offer custom quotes based on the complexity of the automation. Most of our starter packages pay for themselves in saved employee hours within the first month.")
            if st.button("⬅️ Back to Menu"):
                st.session_state.chat_step = "greeting"
                st.rerun()

    # If they clicked Book a Call
    elif st.session_state.chat_step == "contact":
        with st.chat_message("user"):
            st.write("I want to book a call.")
        with st.chat_message("assistant"):
            st.success("Great! Please scroll up to our Contact Form, drop your email, and we will reach out within 24 hours to schedule your free AI audit.")
            if st.button("⬅️ Start Over"):
                st.session_state.chat_step = "greeting"
                st.rerun()
