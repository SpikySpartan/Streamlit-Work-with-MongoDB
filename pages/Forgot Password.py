import base64
import os
import pymongo

import streamlit as st

conn = pymongo.MongoClient("mongodb+srv://Awadhesh:sword@cluster0.gbpzk4b.mongodb.net/?appName=Cluster0")
mydb =conn["Prime"]
mycol = mydb["users"]


st.set_page_config(page_title="Forgot Password", page_icon="🔐", layout="centered")


def get_base64_image(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    for candidate in ["images/Login.jpg", "images/Sign.jpg", "images/Color2.png", "images/logo.png"]:
        if os.path.exists(candidate):
            with open(candidate, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

    return ""


def render_page_style(bg_base64: str) -> None:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(6, 18, 36, 0.82), rgba(6, 18, 36, 0.96)),
                        url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        div[data-testid="stAppViewBlockContainer"] {{
            background: transparent !important;
        }}

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background-color: rgba(6, 18, 36, 0.7) !important;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(0, 242, 254, 0.25) !important;
            border-radius: 16px !important;
            padding: 24px !important;
            box-shadow: 0 0 24px rgba(0, 242, 254, 0.12) !important;
        }}

        .page-title {{
            color: #00F2FE !important;
            font-size: 2rem !important;
            font-weight: 800 !important;
            text-align: center;
            margin-bottom: 8px;
            text-shadow: 0 0 12px rgba(0, 242, 254, 0.35);
        }}

        .page-subtitle {{
            color: #cbd5e1 !important;
            font-size: 0.95rem !important;
            text-align: center;
            margin-bottom: 18px;
        }}

        div[data-testid="stTextInput"] label {{
            color: #00F2FE !important;
            font-weight: 600;
        }}

        div[data-testid="stTextInput"] input {{
            background-color: rgba(10, 25, 47, 0.9) !important;
            color: #ffffff !important;
            border: 1px solid #00F2FE !important;
            border-radius: 6px;
        }}

        div[data-testid="stBaseButton"] button {{
            background: linear-gradient(90deg, #00F2FE, #7a46e1) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    bg_base64 = get_base64_image("images/Forget1.png")
    render_page_style(bg_base64)

    st.markdown("<h2 class='page-title'>Forget Password</h2>", unsafe_allow_html=True)    
    st.markdown(
        "<p class='page-subtitle'>Enter your username and choose a new password for your secure portal account.</p>",
        unsafe_allow_html=True,
    )

    logo_base64 = get_base64_image("images/forget.jpg")
    if logo_base64:
        st.markdown(
            f'<div style="text-align:center; margin-bottom:16px;"><img src="data:image/png;base64,{logo_base64}" style="width:120px; border-radius:50%; box-shadow:0 0 18px rgba(0,242,254,0.25);"></div>',
            unsafe_allow_html=True,
        )

#............ Forget password .........

    username = st.text_input("Username", placeholder="Enter your username")
    new_password = st.text_input("New Password", type="password", placeholder="Enter a new password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter the new password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Forget Password", use_container_width=True):
            if not username.strip():
                st.error("Please enter your username.")
            elif not new_password.strip():
                st.error("Please enter a new password.")
            elif new_password != confirm_password:
                st.error("The password confirmation does not match.")
            else:
                if pymongo is None:
                    st.error("Database connection is not available right now.")
                    return

                try: #...connect to MongoDB and update the password...
                    conn = pymongo.MongoClient(
                        host="localhost",
                        user="root",
                        password="",
                        database="Prime"
                    )
                    cursor = conn.cursor()
                    cursor.execute("SELECT username FROM user_info WHERE username = %s", (username,))
                    if cursor.fetchone() is None:
                        st.error("Username not found. Please try again or sign up.")
                    else:
                        cursor.execute(
                            "UPDATE user_info SET password = %s WHERE username = %s",
                            (new_password, username),
                        )
                        conn.commit()
                        st.success("Password updated successfully.")
                except Exception as exc:
                    st.error(f"Unable to reset password: {exc}")
                finally:
                    if "conn" in locals():
                        conn.close()

#.........switch to login or signup pages.........


    with col2:
        if st.button("Back to Login", use_container_width=True):
            st.switch_page("pages/Login.py")

    if st.button("Create an account", use_container_width=True):
        st.switch_page("pages/Sign up.py")


if __name__ == "__main__":
    main()
