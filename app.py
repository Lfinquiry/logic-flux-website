import streamlit as st
import requests

st.set_page_config(
    page_title="Logic Flux | AI Automation Agency",
    page_icon="⚡",
    layout="wide",
    menu_items={
        'Get Help': 'mailto:inquiry@logic-flux.in',
        'About': "# Logic Flux: Premium AI Automation and Digital Systems."
    }
)
# ... (keep the rest of your code exactly the same) ...
# 2. CUSTOM CSS (Combines your dark theme with the glowing Hero text)
custom_css = """
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* General Colors */
    .main { background-color: #0E1117; color: #FAFAFA; }
    
    /* Hero Text Styling */
    .hero-title {
        font-size: 4rem !important;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        margin-top: -10px;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #A0AEC0;
        margin-top: 10px;
        margin-bottom: 40px;
    }
    
    /* Button Styling */
    .stLinkButton>a { 
        background-color: #00B4D8; 
        color: white !important; 
        width: 100%; 
        border-radius: 5px; 
        font-weight: bold; 
        text-align: center;
        padding: 10px;
        text-decoration: none;
    }
    .stLinkButton>a:hover { background-color: #0096B4; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. LOGO SECTION
col_logo1, col_logo2, col_logo3 = st.columns([1.5, 1, 1.5])
with col_logo2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass # If no logo, just skip smoothly

# 4. HERO SECTION & ACTION BUTTON
st.markdown('<p class="hero-title">Automate the Impossible.</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Logic Flux builds custom AI agents and workflows to scale your business on autopilot.</p>', unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn2:
    # This button now opens an email directly to you!
    st.link_button("Book a Free AI Audit 🚀", "mailto:inquiry@logic-flux.in", use_container_width=True)

st.divider()

# 5. SERVICES SECTION (The New 3-Column Enterprise Grid!)
st.write("") # Adds a little breathing room
st.write("")

st.markdown("<h2 style='text-align: center; color: #00C9FF;'>Our Enterprise AI Solutions</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #A0AEC0; margin-bottom: 40px;'>Stop doing repetitive tasks. Start scaling.</p>", unsafe_allow_html=True)

# Create 3 equal columns for our "Feature Cards"
col_service1, col_service2, col_service3 = st.columns(3)

with col_service1:
    st.markdown("### 🤖 Customer AI Agents")
    st.write("We build intelligent chatbots that handle your customer support 24/7, qualify leads, and close sales while you sleep.")
    st.markdown("**Perfect for:** E-commerce, Real Estate, Clinics.")

with col_service2:
    st.markdown("### ⚡ Workflow Automation")
    st.write("We connect your favorite apps (Gmail, CRM, Sheets) so data moves automatically. No more manual copying and pasting.")
    st.markdown("**Perfect for:** Marketing Agencies, B2B Sales.")

with col_service3:
    st.markdown("### 🧠 Internal Team AI")
    st.write("Secure, private AI assistants trained strictly on your company's SOPs and documents to help your employees work 10x faster.")
    st.markdown("**Perfect for:** Law Firms, Corporate Teams.")

st.write("")
st.write("")
st.divider() # Draws a clean line before the next section

# 6. CONTACT FORM SECTION
st.markdown("<h3 style='text-align: center;'>Start Your Transformation</h3>", unsafe_allow_html=True)

# 👇 ADD THIS EXACT LINE RIGHT HERE 👇
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



