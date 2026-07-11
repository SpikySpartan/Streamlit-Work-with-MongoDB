import streamlit as st
import base64
import os
import pymongo
mongodb+srv://Awadhesh:<SwordArtOnline>@cluster0.gbpzk4b.mongodb.net/?appName=Cluster0
conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb =conn["Prime"]
mycol = mydb["users"]

st.set_page_config(page_title="Welcome - Secure Portal", page_icon="🔐", layout="wide")

#........background image and styling........

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""


def render_page_style(bg_base64):
    background_css = ""
    if bg_base64:
        background_css = f"background: linear-gradient(rgba(6, 18, 36, 0.6), rgba(6, 18, 36, 0.9)), url('data:image/jpg;base64,{bg_base64}') center/cover fixed no-repeat;"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(180deg, #07111f 0%, #03070f 100%);
            {background_css}
        }}

        div[data-testid="stAppViewBlockContainer"] {{
            background: transparent !important;
        }}

        .hero-section {{
            text-align: center;
            padding: 32px 24px 42px;
            background-color: rgba(6, 18, 36, 0.75);
            border-radius: 18px;
            margin-bottom: 40px;
        }}

        .hero-subtitle {{
            color: #cbd5e1;
            font-size: 1.05rem;
            line-height: 1.8;
            max-width: 780px;
            margin: 0 auto;
        }}

        .feature-card {{
            background-color: rgba(6, 18, 36, 0.72);
            border: 1px solid rgba(0, 242, 254, 0.18);
            border-radius: 16px;
            padding: 22px;
            margin: 14px 0;
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.08);
        }}

        .feature-title {{
            color: #00F2FE;
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .feature-text {{
            color: #e2e8f0;
            font-size: 0.98rem;
            line-height: 1.7;
        }}

        .footer-text {{
            color: #94a3b8;
            font-size: 0.92rem;
        }}

        .stButton button {{
            min-height: 52px;
            font-size: 1rem;
            font-weight: 600;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero(logo_base64):
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-subtitle">
                Welcome
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if logo_base64:
        st.markdown(
            f'<div style="text-align:center; margin-bottom:20px;"><img src="data:image/png;base64,{logo_base64}" style="width: 150px; max-width: 100%; border-radius: 50%; box-shadow: 0 0 18px rgba(0, 242, 254, 0.3);"></div>',
            unsafe_allow_html=True,
        )


def render_features():
    features = [
        ("🔐 Login Page", "Use this page to sign in securely and access your personal dashboard and tools."),
        ("✍️ Sign Up Page", "Create your account by entering your username, password, mobile number, email, and date of birth."),
        ("🧠 Application Page", "Explore helpful features like number tools, string tools, a calculator, notes, and a quiz."),
        ("👤 Profile Page", "View your profile details, update your password, or manage your account information."),
        ("🔑 Forgot Password Page", "Reset your password quickly if you ever need to recover access to your account."),
    ]

    for title, description in features:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-title">{title}</div>
                <div class="feature-text">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

#......switch to login page.............

def render_actions():
    _, right = st.columns([5, 1], gap="small")
    with right:
        if st.button("🚀 Login", use_container_width=True, key="welcome_login"):
            st.switch_page("pages/Login.py")


def render_footer():
    st.markdown(
        """
        <div style="text-align:center; margin-top: 46px;">
            <p class="footer-text">© 2026 Secure Portal. All rights reserved. Designed for safe access, smooth navigation, and everyday learning support.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

#..........background and logo images path.......

def main():
    bg_base64 = get_base64_image("images/background.jpg")
    logo_base64 = get_base64_image("")

    render_page_style(bg_base64)
    render_actions()
    render_hero(logo_base64)
    render_features()
    render_footer()


if __name__ == "__main__":
    main()
