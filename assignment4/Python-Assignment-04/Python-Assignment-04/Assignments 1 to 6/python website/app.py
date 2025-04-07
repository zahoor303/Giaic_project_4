import streamlit as st
import sqlite3
import smtplib
from email.message import EmailMessage
import hashlib
import os
from datetime import datetime
import openai

# --- DATABASE SETUP ---
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS messages (name TEXT, email TEXT, message TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS files (filename TEXT, uploaded_at TEXT)")
conn.commit()

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ultimate Streamlit Website", page_icon="🌍", layout="wide")

# --- DARK MODE ---
dark_mode = st.sidebar.toggle("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
            body {background-color: #1E1E1E; color: white;}
            .stButton>button {background-color: #444444; color: white;}
        </style>
        """, unsafe_allow_html=True
    )

# --- USER AUTHENTICATION ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    hashed_pw = hash_password(password)
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_pw))
    conn.commit()

def login_user(username, password):
    hashed_pw = hash_password(password)
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_pw))
    return c.fetchone()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🔗 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Portfolio", "Blog", "Contact", "File Upload", "Chatbot", "E-commerce", "Login", "Signup"])

# --- HOME PAGE ---
if page == "Home":
    st.title("🏠 Welcome to the Ultimate Streamlit Website!")
    st.write("This is a full-featured website with file uploads, chatbot, and e-commerce functionality! 🚀")
    st.image("https://source.unsplash.com/1200x500/?technology", use_column_width=True)
    st.success("💡 Use the sidebar to explore different sections.")

# --- PORTFOLIO PAGE ---
elif page == "Portfolio":
    st.title("💼 My Portfolio")
    st.write("Here are some of my latest projects:")
    st.image("https://source.unsplash.com/800x400/?coding", use_column_width=True)
    st.write("🔹 **Project 1**: AI Chatbot using Python")
    st.write("🔹 **Project 2**: E-commerce Website with Django")
    st.write("🔹 **Project 3**: Data Science Dashboard")

# --- BLOG PAGE ---
elif page == "Blog":
    st.title("📝 Blog")
    st.write("Read my latest blog posts:")
    st.subheader("📌 How to Build a Python Web App in 15 Minutes")
    st.write("Python is an amazing language for building web applications...")
    st.subheader("📌 5 Must-Know Libraries for Data Science")
    st.write("Here are 5 powerful Python libraries every Data Scientist should know...")

# --- CONTACT PAGE WITH EMAIL ---
elif page == "Contact":
    st.title("📩 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("👤 Your Name")
        email = st.text_input("📧 Your Email")
        message = st.text_area("✉️ Your Message")
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
            st.success("✅ Message sent successfully!")

# --- FILE UPLOAD & DOWNLOAD ---
elif page == "File Upload":
    st.title("📂 Upload & Download Files")
    
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        file_path = f"uploads/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        c.execute("INSERT INTO files (filename, uploaded_at) VALUES (?, ?)", (uploaded_file.name, datetime.now()))
        conn.commit()
        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

    st.subheader("📥 Download Uploaded Files")
    c.execute("SELECT filename FROM files")
    files = c.fetchall()
    for file in files:
        file_name = file[0]
        file_path = f"uploads/{file_name}"
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(f"⬇ Download {file_name}", f, file_name)

# --- AI CHATBOT ---
elif page == "Chatbot":
    st.title("🤖 AI Chatbot")
    openai_api_key = "your_openai_api_key"
    
    user_input = st.text_input("Ask the chatbot:")
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(f"🤖 Chatbot: {response['choices'][0]['message']['content']}")

# --- E-COMMERCE PAGE ---
elif page == "E-commerce":
    st.title("🛒 E-commerce Store")
    st.subheader("🔥 Trending Products")
    
    products = [
        {"name": "Smartphone", "price": "$699", "image": "https://source.unsplash.com/300x200/?smartphone"},
        {"name": "Laptop", "price": "$999", "image": "https://source.unsplash.com/300x200/?laptop"},
        {"name": "Headphones", "price": "$199", "image": "https://source.unsplash.com/300x200/?headphones"},
    ]
    
    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i]:
            st.image(product["image"], use_column_width=True)
            st.write(f"**{product['name']}**")
            st.write(f"💲 {product['price']}")
            st.button(f"🛒 Add to Cart", key=product["name"])

# --- LOGIN PAGE ---
elif page == "Login":
    st.title("🔑 Login")
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")
    login_button = st.button("Login")

    if login_button:
        user = login_user(username, password)
        if user:
            st.success(f"✅ Welcome back, {username}!")
        else:
            st.error("❌ Invalid credentials. Please try again.")

# --- SIGNUP PAGE ---
elif page == "Signup":
    st.title("📝 Signup")
    username = st.text_input("👤 Choose a Username")
    email = st.text_input("📧 Your Email")
    password = st.text_input("🔒 Choose a Password", type="password")
    signup_button = st.button("Sign Up")

    if signup_button:
        register_user(username, email, password)
        st.success("✅ Account created successfully! You can now log in.")

# --- FOOTER ---
st.markdown("---")
st.caption("🔹 Developed by ❤️ Zahoor fatima ")
