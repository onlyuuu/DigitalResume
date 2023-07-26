import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My_Resume", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_project= load_lottieurl("https://lottie.host/4df1ebdd-2098-4d07-a0a6-fe6b2014a0c4/kmjTYZ8rjn.json")
lottie_certificate=load_lottieurl("https://lottie.host/46e0e5ab-deec-46e0-85c4-2d19738e05f8/dAyNzGA96Y.json")
lottie_language=load_lottieurl("https://lottie.host/78c9e1a3-ec87-49cf-afb4-d4bcc2b6faa1/vredvsbfSg.json")


header_container = st.container()

with header_container:
    header_col1, header_col2 = st.columns([3, 9])

    with header_col1:
        profile_photo = Image.open("image/My_profile.png")
        profile_photo = profile_photo.resize((150, 150))
        st.image(profile_photo, width=150, caption="Sylesh Sathish Kumar")

    with header_col2:
        st.subheader("Hi, I am sylesh :wave:")
        st.title(
            "I am an aspiring student currently pursuing my final year B.Tech Information Technology with great enthusiasm and curiosity."
        )
        st.write(
            "[LinkedIn](https://www.linkedin.com/in/sylesh-s-191656208) | 201001111@rajalakshmi.edu.in | Contact no: 7358014128"
        )
        if st.button("Download Resume"):
            st.markdown(
                "[Download Resume](https://drive.google.com/file/d/1avQgyRIdLbrwLBzAMstM6YUjRPTPIJDE/view?usp=sharing)",
                unsafe_allow_html=True
            )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Skills")
        st.write("##")
        with st.expander("Programming Languages"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("Python Programming")
                st.write("Java Programming")
                st.write("C programming")
            with col2:
                st.progress(4/5)
                st.progress(4/5)
                st.progress(4/5)
        with st.expander("Web Development"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("HTML & CSS")
            with col2:
                st.progress(4/5)
        with st.expander("Other Skills"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("Problem solving")
                st.write("Database Management System")
                st.write("Git")
            with col2:
                st.progress(4/5)
                st.progress(4/5)
                st.progress(3/5)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_project)
    with right_column:
        st.subheader("Real Time NEWS feed Application using Android Studio")
        st.write(
            """
            The Newsfeed Android application is designed to provide users with access to the latest news from around the world.
            """
        )
        st.markdown("[GitHub](https://github.com/onlyuuu/android-news-app)")

        st.subheader("Smart Power Shutdown System")
        st.write(
            """
           This project proposes a system to monitor the LPG gas level using an MQ-4 sensor and shutdown the power supply in case of a gas leak.
            """
        )
        st.subheader("Payment Card Prediction Model")
        st.write(
            """
            This project was conducted as part of the Catalyst Serverless Workshop by Zoho and aimed to develop a machine learning (ML) model that predicts the type of payment card based on a given dataset.
            """
        )
with st.container():
    
    left_column, right_column = st.columns(2);
    with left_column:
        st.write("---")
        st.header("Certifications")
        st.write("##")
        st.subheader("Google Data Analytics")
        st.write("It provided me with useful, real-world examples that helped me lay the groundwork for a career as a data analyst.")
        st.markdown("[Certificate Link](https://drive.google.com/file/d/1kt-jycTtATiOPd2gsu_AzqssV6B10ltN/view)")
        st.subheader("Data Analytics with Python")
        st.write("I completed an NPTEL (National Programme on Technology Enhanced Learning) course on data analytics with python, where I learned essential concepts and techniques for data preprocessing, visualization, and statistical analysis.")
        st.markdown("[Certificate Link](https://drive.google.com/file/d/1C6SrK8VYRfUiapqV9DL6YGQPsi4bF_nl/view)")
        st.subheader("UI Path")
        st.write("It aided me in gaining a foundational understanding of automation and the procedures associated in it.")
        st.markdown("[Certificate Link](https://drive.google.com/file/d/1LFrQhilEjY4wjTOB-oHiARuBu4YzwdXT/view)")
        st.subheader("Catalyst Serverless Workshop")
        st.write("This workshop conducted by zoho taught me a new approach towards problem solving.")
        st.markdown("[Certificate Link](https://drive.google.com/file/d/1Tx49i3ZdTIXppaR3-Ehc8HcwTreOxAGP/view)")
        st.write("##")
with right_column:
    st_lottie(lottie_certificate,height=400,width=400)

with st.container():
    st.write("---")
    st.header("Languages")
    st.write("##")
    left_column, right_column = st.columns(2);
    with right_column:
        st.subheader("English")
        st.progress(4/5)
        st.subheader("Tamil")
        st.progress(4/5)
        st.subheader("Hindi")
        st.progress(3/5)
        st.subheader("Telugu")
        st.progress(3/5)
with left_column:
    st_lottie(lottie_language,height=200,width=400)

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/el/xuzowa" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
