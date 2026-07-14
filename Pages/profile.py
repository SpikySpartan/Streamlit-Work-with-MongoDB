import streamlit as st
import mysql.connector
import base64
import os   

#........background image and styling........

st.set_page_config(page_title="Math Utilities", page_icon="🧮", layout="centered")
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/Color2.png") #...Background image path....
if bg_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(10, 25, 47, 0.8), rgba(10, 25, 47, 0.8)), 
                        url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        div[data-testid="stContainer"] {{
            background-color: rgba(6, 18, 36, 0.6) !important;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 12px;
            padding: 30px;
        }}
        
        .main-title {{
            color: #00F2FE !important;
            font-size: 3rem !important;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown(
    """
    <style>
    .main-title {
        color: #FF4B4B;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#.............check if user is logged in........


if st.session_state.get("username", False):
    st.success(f"Welcome :{st.session_state['username']}")
else:
    st.error("⚠️ System Alert: You must be logged in to access this page.")
    st.stop()
st.markdown('<h1 class="main-title">User Profile</h1>', unsafe_allow_html=True)
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="Users"
)
header_col, logout_col = st.columns([3, 1])
with header_col:
     st.write("This is your profile page. Here you can view and manage your account details.")
     st.write("You can also update your password, email, and other personal information.")

with logout_col:  #...logout......
    if st.button("Logout"):
        del st.session_state["username"]
        st.switch_page("Main.py")

st.divider()#Draw a horizontal line to separate the header from the content

tab1, tab2, tab3 = st.tabs(["View Profile", "Update Password", "Delete Account"])

#............account details............

with tab1:
    st.markdown("<h2 class='main-title' color='#00F2FE'>Account Details</h2>", unsafe_allow_html=True)
    str1 = st.session_state["username"]
    str2 = st.session_state.get("password", "")
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM user_info WHERE username = %s AND password = %s", (str1, str2))
    res = mycursor.fetchall()
    if res:
        i = res[0]
        col_left, col_right = st.columns([1, 2])
        with col_left:
            st.markdown(f"**Username:** {i[0]}")
            st.markdown(f"**Password:** {i[1]}")
        with col_right:
            st.markdown(f"**Mobile:** {i[2]}")
            st.markdown(f"**Email:** {i[3]}")
            st.markdown(f"**Date of Birth:** {i[4]}")
    else:
        st.info("No profile details found.")

#............update password............

with tab2:
     st.markdown("<h2 class='main-title' color='#00F2FE'>Update Password</h2>", unsafe_allow_html=True)
     with st.form("password_form", clear_on_submit=True):
        change_password = st.text_input("Enter New Password", type="password", placeholder="Type new password...")
        submit_pass = st.form_submit_button("Update Password", type="primary")
        
        if submit_pass:
            if not change_password.strip():
                st.error("⚠️ Validation Error: Password field cannot be empty.")
            else:
                with conn.cursor() as mycursor:
                    mycursor.execute(
                        "UPDATE user_info SET password = %s WHERE username = %s", 
                        (change_password, st.session_state['username'])
                    )
                    conn.commit()
                # Crucial step: keep session state in sync with reality
                st.session_state['password'] = change_password
                st.success("✅ Password updated successfully!")

#............delete account............
with tab3:
    st.markdown("<h2 class='main-title' color='#00F2FE'>Delete Account Permanently</h2>", unsafe_allow_html=True)
    st.warning("⚠️ Warning: This action is irreversible. Deleting your account will permanently remove all your data.")
    if st.button("Delete Account"):
        with conn.cursor() as mycursor:
            mycursor.execute("DELETE FROM user_info WHERE username = %s", (st.session_state['username'],))
            conn.commit()
        st.session_state.clear()  # Clear session state to log the user out
        st.success("🗑️ Account deleted successfully! You will be redirected to the login page.")
        st.switch_page("Main.py")


