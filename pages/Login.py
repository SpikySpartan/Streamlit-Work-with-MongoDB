import streamlit as st
import pymongo
conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb =conn["Prime"]
mycol = mydb["users"]
st.set_page_config(
    page_title="Secure Portal Login",
    page_icon="🔐",
    layout="centered"
)
import base64
import os
st.set_page_config(
    page_title="User Login",
    page_icon="🔐",
    layout="centered"
)

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/Login.jpg")
logo_base64 = get_base64_image("images/logo.png")

if bg_base64:
    st.markdown(
        f"""
        <style>
        /* Set full-screen background image */
        .stApp {{
            background: url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Keep main container structural layout clear */
        div[data-testid="stAppViewBlockContainer"] {{
            background: transparent !important;
        }}

        /* Translucent glass container positioned over cyber grid */
        div[data-testid="stContainer"] {{
            background-color: rgba(6, 18, 36, 0.45) !important;
            backdrop-filter: blur(6px);
            border: 1px solid rgba(0, 242, 254, 0.25) !important;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.15) !important;
            border-radius: 14px !important;
            padding: 35px !important;
            max-width: 450px;
            margin: 0 auto;
        }}

        /* Logo styling container with background mix-blend for transparency */
        .logo-box {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 25px;
        }}
        .logo-box img {{
            width: 180px;
            height: auto;
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(122, 70, 225, 0.5);
            /* Blends out the white background square of the logo png */
            mix-blend-mode: lighten; 
        }}

        /* Form fields custom styling to match neon terminal interface */
        div[data-testid="stTextInput"] label {{
            color: #00F2FE !important;  #(Vibrant Cyan)
            font-weight: 600;
            letter-spacing: 1px;
        }}
        
        div[data-testid="stTextInput"] input {{
            background-color: rgba(10, 25, 47, 0.85) !important;
            color: #FFFFFF !important; #(White)
            border: 1px solid #00F2FE !important;
            border-radius: 6px;
        }}

        /* Header typography styling */
        .title-text {{
            color: #00F2FE !important; #(Vibrant Cyan)
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            text-align: center;
            text-shadow: 0 0 12px rgba(0, 242, 254, 0.6);
            margin-bottom: 0px;
            margin-top: 30px;
            letter-spacing: 2px;
        }}
        .subtitle-text {{
            color: #94A3B8 !important; #(Rock Blue Color)
            font-size: 0.95rem !important;
            text-align: center;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .main-text {{
            color: #0A0A0A !important; #(Jet Black)
            font-size: 2.5rem !important;
            font-weight: 1000 !important;
            text-align: center;
            text-shadow: 0 0 12px rgba(0, 242, 254, 0.6);
            margin-bottom: 0px;
            margin-top: 30px;
            letter-spacing: 2px;
        }}
         /* Remove button background - just show text */
        div[class*="st-key-Button"]div[data-testid="stBaseButton"] button {{
             background-color: transparent !important;
             border: none !important;
             color: #00F2FE !important;
             font-weight: 600;
             cursor: pointer;
             padding: 8px 0 !important;
             text-decoration: underline;
         }}
         div[data-testid="stBaseButton"] button:hover {{
             opacity: 0.7;
         }}
         </style>
         """,
    unsafe_allow_html=True)
else:
    st.error("⚠️ System Alert: 'background.jpg' missing from root directory.")

st.markdown('<h3 class="main-text">User Login</h3>', unsafe_allow_html=True)
with st.container(border=True):
    
    if logo_base64:
        st.markdown(f'<div class="logo-box"><img src="data:image/png;base64,{logo_base64}"></div>', unsafe_allow_html=True)
    else:
        st.caption("⚠️ 'logo.png' structural target missing.")
username = st.text_input("Username", placeholder="e.g., admin_user")
password = st.text_input("Password", type="password", placeholder="••••••••")
login_col, Pass_col = st.columns([1, 3])
with login_col:
    login_clicked = st.button("Log In 🚀", use_container_width=True)
    if login_clicked:
        result = None
        if username.strip() == "" or password.strip() == "":
            st.error("⚠️ Validation Error: Both username and password fields are required.")
        else:
            try:
                result = mycol.find_one({"username": username, "password": password})
            except Exception as e:
                st.error(f"⚠️ Database connection error: {e}")
                result = None
        if result:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["password"] = password
            st.success("✅ Login successful! Redirecting to Utilities page...")
            st.switch_page("pages/Application.py")
        else:
            st.error("❌ Access Denied: Invalid username or password.")

with Pass_col:
    Forget_pass = st.button("Forget Password", use_container_width=True)
    if Forget_pass:
        st.switch_page("pages/Forgot Password.py")

st.markdown('<p class="main-text">Not a Member?</p>', unsafe_allow_html=True)
Sign_up = st.button("Signup Now", key="Button" , use_container_width=True)
if Sign_up:
    st.switch_page("pages/Sign up.py")

