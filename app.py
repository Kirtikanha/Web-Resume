# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:02:24 2025

@author: Kirti
"""

import streamlit as st
from PIL import Image

# Set sidebar width via custom CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            min-width: 200px;
            max-width: 200px;
        }
    </style>
""", unsafe_allow_html=True)

# Load your image
image = Image.open("Kirti.jpg")
st.image(image, width=200, caption="Kirti Sharma")


# Sidebar
st.sidebar.title("🔗 **Connect**")
st.sidebar.markdown("""
- 📧 [Email](mailto:kirti.sharma151700@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/kirti-sharma-0826171b0/)
- 🧠 [GitHub](https://github.com/Kirtikanha)
""")

# Header
st.title("👩‍🔬 **Kirti Sharma**")
st.subheader("Ph.D. Scholar")
st.subheader("Birla Institute of Technology | Mesra | Ranchi")


st.header("Summary")
st.markdown("""
Welcome! I'm a research scholar with a strong foundation in Physics and Machine Learning techniques, specializing in the development of machine learning models for biosensor systems. My work involves advanced signal processing, regression modeling, and synthetic data generation for physiological datasets. I’m passionate about applying data-driven methods to accelerate innovation in various field of research.
""")

# Resume Summary
st.header("📄 Technical Expertise")
st.markdown("""
- 💻 **Programming Language**: Python, MATLAB, R
- 📈 **Machine Learning Techniques**: Regression, Classification, Generative Models
- 🛠 **Tools**: Jupyter, VS Code, Git
""")

with open("CV_Kirti_linup_.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    st.download_button(label="📥 Download My Resume (PDF)", data=PDFbyte, file_name="Kirti_Sharma_Resume.pdf", mime='application/pdf')

# Featured Projects
st.header("🧪 Reseach Projects")

st.markdown("### 🔬 Hematocrit Volume Prediction")
st.markdown("""
Developed a model using amperometric glucose signals to estimate hematocrit volume. Combined physics-informed features with machine learning for robust performance.  
🔗 [GitHub Repo](https://github.com/Kirtikanha/Hematocrit-Volume-Prediction)
""")

st.markdown("### 💉 Blood Viscosity Modeling")
st.markdown("""
Implemented ML algorithms on amperometric data to predict blood viscosity using the Krieger-Dougherty and Carreau-Yasuda models.  
🔗 [GitHub Repo](https://github.com/Kirtikanha/Blood-Viscosity-Model)
""")

st.markdown("### 🧬 Hemoglobin Prediction & Synthetic Data Generation")
st.markdown("""
Created synthetic bio-signal data using GaussianCopula for hemoglobin prediction models. Applied both generative and discriminative methods.  
🔗 [GitHub Repo](https://github.com/Kirtikanha/Hemoglobin-Prediction)
""")

st.markdown("### 🔎 Lead Generation Scraper (Caprae AI Handbook)")
st.markdown("""
Developed a web scraping tool to extract SaaS leads using Google Search + Streamlit. Features include company name, email, LinkedIn, and CSV export.  
🔗 [GitHub Repo](https://github.com/Kirtikanha/Project1)
""")


# Contact Form
st.header("📬 Get in Touch")
contact_form = """
<form action="https://formsubmit.co/kirti.sharma151700@gmail.com" method="POST">
    <input type="text" name="name" placeholder="Your Name" required><br><br>
    <input type="email" name="email" placeholder="Your Email" required><br><br>
    <textarea name="message" placeholder="Your Message Here" rows="5" required></textarea><br><br>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)