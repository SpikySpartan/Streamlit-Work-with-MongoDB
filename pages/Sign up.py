import streamlit as st
import base64
import os
import pymongo

conn = pymongo.MongoClient("mongodb+srv://Awadhesh:SwordArtOnine@cluster0.gbpzk4b.mongodb.net/?appName=Cluster0")
mydb =conn["Prime"]
mycol = mydb["users"]

#.......background image and styling........

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/Sign.jpg")
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
    
    /* Remove button background - just show text */
    div[data-testid="stBaseButton"] button {
        background-color: transparent !important;
        border: none !important;
        color: #00F2FE !important;
        font-weight: 600;
        cursor: pointer;
        padding: 8px 0 !important;
        text-decoration: underline;
    }
    
    div[data-testid="stBaseButton"] button:hover {
        opacity: 0.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ..........Sign up form.........

st.markdown("<h2 class='main-title' color='#00F2FE'>Sign up ✍</h2>", unsafe_allow_html=True)
un=st.text_input("Username",placeholder="Enter your username")
p=st.text_input("Password",type="password",placeholder="Enter your password")
m=st.text_input("Mobile number",placeholder="Enter your mobile number")
e=st.text_input("Email id",placeholder="Enter your email id")
d=st.text_input("Date of Birth",placeholder="Enter your date of birth")
if st.button("Sign up"):
    mycol.insert_one({"uname":un,"password":p,"mobileno":m,"email":e,"dob":d})
    st.write("Welcome", username)
    st.success("Sign up successful")


#..................source code................

with st.expander("Sign up Source Code"):
    st.code('''import streamlit as st
st.title("Sign up")
username=st.text_input("Username",placeholder="Enter your username")
password=st.text_input("Password",type="password",placeholder="Enter your password")
mobile=st.text_input("Mobile number",placeholder="Enter your mobile number")
email=st.text_input("Email id",placeholder="Enter your email id")
dob=st.text_input("Date of Birth",placeholder="Enter your date of birth")
if st.button("Sign up"):
    st.write("Welcome", username)
    st.success("Sign up successful")''')
