import streamlit as st
import pandas as pd
import os

def generate_custom_table(data, headers):
    table_style = """
    <style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 24px;
        font-size: 1.15em;
        background: #23282c;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }
    .custom-table th {
        background: #FFD700;
        color: #23282c;
        font-weight: bold;
        padding: 12px 10px;
        text-align: left;
        font-size: 1.1em;
    }
    .custom-table td {
        padding: 10px 10px;
        color: #fff;
        border-bottom: 1px solid #444;
    }
    .custom-table tr:nth-child(even) {
        background: #2a2f33;
    }
    .custom-table tr:nth-child(odd) {
        background: #23282c;
    }
    </style>
    """
    table_html = f"<table class='custom-table'><thead><tr>{''.join([f'<th>{h}</th>' for h in headers])}</tr></thead><tbody>"
    for row in data:
        table_html += "<tr>" + ''.join([f'<td>{cell}</td>' for cell in row]) + "</tr>"
    table_html += "</tbody></table>"
    return table_style + table_html

# Set page configuration for wide layout and cinematic theme
st.set_page_config(page_title="Pawan Kalyan Records", layout="wide", page_icon="🎬")

# Custom CSS for cinematic styling
st.markdown("""
    <style>
    /* Dark cinematic background */
    .stApp {
        background-color: #1C2526;
        color: #E0E0E0;
        font-family: 'Roboto', sans-serif;
    }
    /* Title styling */
    h1 {
        color: #FFD700;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 20px;
    }
    /* Section header styling */
    h2 {
        color: #FFD700;
        font-size: 2em;
        font-weight: bold;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 10px;
        margin-top: 40px;
    }
    /* Table styling */
    .dataframe {
        background-color: #2A2F33;
        border: 1px solid #FFD700;
        border-radius: 10px;
        padding: 10px;
    }
    .dataframe th {
        background-color: #FFD700;
        color: #1C2526;
        font-weight: bold;
    }
    .dataframe td {
        color: #E0E0E0;
    }
    /* Image caption styling */
    .stImage > div > div > img {
        border: 3px solid #FFD700;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    .stImage > div > div > .caption {
        color: #E0E0E0;
        font-style: italic;
        text-align: center;
    }
    /* Section container */
    .section-container {
        background-color: #2A2F33;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    /* Custom tab styling for better visibility */
    .stTabs [data-baseweb="tab"] {
        color: #FFD700 !important;
        font-weight: 500;
        font-size: 1.15em;
        opacity: 1 !important;
    }
    .stTabs [aria-selected="true"] {
        color: #fff !important;
        font-weight: bold !important;
        background: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Pawan Kalyan  Box Office Records</h1>", unsafe_allow_html=True)

# Data for each territory
data = {
    "East": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.29, "Status": "All Time Record"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.35, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 0.40, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 0.65, "Status": "All Time Record (Fixed Hires)"},
        {"Movie": "Teenmaar", "Collection (Cr)": 0.26, "Status": "Top 7"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.827, "Status": "All Time Record"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 0.702, "Status": "Top 2"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 1.05, "Status": "All Time Record"},
        {"Movie": "Gopala Gopala", "Collection (Cr)": 1.21, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 2.26, "Status": "All Time Record"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 3.56, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 2.86, "Status": "Top 4"}
    ],
    "West": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.25, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.30, "Status": "Top 2"},
        {"Movie": "Puli", "Collection (Cr)": 0.41, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 0.42, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.596, "Status": "Top 2"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 0.698, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 0.76, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 2.70, "Status": "All Time Record"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 2.91, "Status": "Top 2"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 3.70, "Status": "Top 2"}
    ],
    "Krishna": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.28, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.40, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 0.425, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 0.47, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.588, "Status": "All Time Record"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 0.66, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 0.71, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 1.51, "Status": "All Time Record"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 1.62, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 1.83, "Status": "Top 2"}
    ],
    "UA": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.215, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.425, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 0.44, "Status": "Top 2"},
        {"Movie": "Panjaa", "Collection (Cr)": 0.45, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.55, "Status": "Top 2"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 0.65, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 0.87, "Status": "Top 2"},
        {"Movie": "Gopala Gopala", "Collection (Cr)": 0.87, "Status": "Top 3"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 2.01, "Status": "All Time Record"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 3.01, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 4.30, "Status": "Top 2"}
    ],
    "Nizam": [
        {"Movie": "Annavaram", "Collection (Cr)": 1.1, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 1.3, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 1.52, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 1.67, "Status": "Top 3"},
        {"Movie": "Teenmaar", "Collection (Cr)": 1.60, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 2.21, "Status": "Top 2"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 2.93, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 3.28, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 5.03, "Status": "Top 3"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 5.48, "Status": "Top 2 (8.6 Cr Gross)"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 4.74, "Status": "Top 4"},
        {"Movie": "Vakeel Saab", "Collection (Cr)": 8.80, "Status": "Top 2"},
        {"Movie": "Bheemla Nayak", "Collection (Cr)": 11.8, "Status": "All Time Record"}
    ],
    "Ceeded": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.86, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 1.05, "Status": "Top 2"},
        {"Movie": "Panjaa", "Collection (Cr)": 1.32, "Status": "Top 2"},
        {"Movie": "Puli", "Collection (Cr)": 1.5, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 1.96, "Status": "Top 4"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 1.56, "Status": "Top 5"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 2.25, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 4.10, "Status": "Top 2"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 3.26, "Status": "Top 5"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 3.35, "Status": "Top 6"}
    ],
    "Guntur": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.34, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.51, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 0.645, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 0.78, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 1.12, "Status": "Top 2"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 1.11, "Status": "Top 3"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 1.41, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 2.46, "Status": "Top 2"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 2.93, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 3.78, "Status": "Top 2"}
    ],
    "Nellore": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.16, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.30, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 0.29, "Status": "Top 3"},
        {"Movie": "Panjaa", "Collection (Cr)": 0.21, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.365, "Status": "Top 2"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 0.356, "Status": "Top 3"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 0.57, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 0.85, "Status": "Top 2"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 1.33, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 1.64, "Status": "Top 2"}
    ],
    "Coastal AP": [
        {"Movie": "Annavaram", "Collection (Cr)": 1.54, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 2.285, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 2.61, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 2.98, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 4.04, "Status": "All Time Record"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 4.166, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 5.37, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 11.79, "Status": "All Time Record"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 15.36, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 17.56, "Status": "Top 2"}
    ],
    "AP/TS": [
        {"Movie": "Annavaram", "Collection (Cr)": 3.50, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 4.635, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 5.63, "Status": "All Time Record"},
        {"Movie": "Panjaa", "Collection (Cr)": 5.97, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 8.2136, "Status": "All Time Record"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 8.656, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 10.9, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 20.92, "Status": "Top 2"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 23.36, "Status": "All Time Record"},
        {"Movie": "Agnyaathavaasi", "Collection (Cr)": 26.94, "Status": "Top 2"}
    ]
}

# Dictionary for movie image paths (user to update with actual paths)
image_paths = {
    "Annavaram": "annavaram.jpeg",
    "Jalsa": "Jalsa.jpg",
    "Puli": "Puli.jpg",
    "Panjaa": "Panjaa.jpg",
    "Teenmaar": "teenmaar.webp",
    "Gabbar Singh": "GabbarSingh.jpg",
    "Camera Man Gangatho Rambabu": "Cameramangangathorambabu.jpg",
    "Attarintiki Daredi": "AttarintikiDaredi.jpg",
    "Gopala Gopala": "GopalaGopala.jpeg",
    "Sardaar Gabbar Singh": "Sardaar.jpg",
    "Katamarayudu": "KTM.jpg",
    "Agnyaathavaasi": "Agynatavasi.jpg",
    "Vakeel Saab": "Vakeelsaab.jpg",
    "Bheemla Nayak": "bheemla-nayak.jpeg",
    "Kushi": "Kushi_PSPK.jpg",
    "Badri": "Badri.jpeg",
    "Thammudu": "Thammudu.jpg"
}

# Sidebar navigation
st.sidebar.title("Pawan Kalyan Records")
nav_options = ["Records", "Center Wise Data"]
nav_choice = st.sidebar.radio("Go to", nav_options)

if nav_choice == "Records":
    record_types = ["Opening Records", "First Week Records", "Re-Release Opening Records", "USA Premier Records", "Closing Records", "Town Records (Full Run)"]
    selected_record_type = st.sidebar.selectbox("Select Record Type", ["-- Select --"] + record_types)
    selected_centerwise_movie = None
elif nav_choice == "Center Wise Data":
    centerwise_movies = [
    "Gabbar Singh",
    "Sardaar Gabbar Singh",
    "Vakeel Saab",
    "Bheemla Nayak",
    "Attarintiki Daredi",
    "Gabbar Singh (Re-Release)",
    "CameraMan Gangatho Rambabu",
    "Kushi (Re-Release)",
    "Annavaram",
    "Badri"
    ]
    selected_centerwise_movie = st.sidebar.selectbox("Select Movie", centerwise_movies)
    selected_record_type = None

# First Week Records Data
first_week_data = {
    "Nizam": [
        {"Movie": "Annavaram", "Collection (Cr)": 4.15, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 5.4, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 4.76, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 9.3, "Status": "All Time Record"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 7.46, "Status": "Top 2"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 13.12, "Status": "All Time Record"},
        {"Movie": "Bheemla Nayak", "Collection (Cr)": 32.7, "Status": "Top 2"},
    ],
    "West": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.67, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.68, "Status": "Top 2"},
        {"Movie": "Puli", "Collection (Cr)": 1.05, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 1.73, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 2.2, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 3.55, "Status": "Top 2"},
    ],
    "East": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.80, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.78, "Status": "Top 2"},
        {"Movie": "Puli", "Collection (Cr)": 1.03, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 2.03, "Status": "Top 2"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 2.62, "Status": "All Time Record"},
    ],
    "UA": [
        {"Movie": "Annavaram", "Collection (Cr)": 1.05, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 1.3, "Status": "Top 2"},
        {"Movie": "Puli", "Collection (Cr)": 1.51, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 2.51, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 3.46, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 3.94, "Status": "Top 2"},
    ],
    "Krishna": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.79, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 1.17, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 1.10, "Status": "Top 3"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 1.82, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 2.42, "Status": "All Time Record"},
    ],
    "Ceeded": [
        {"Movie": "Annavaram", "Collection (Cr)": 2.25, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 2.57, "Status": "Top 2"},
        {"Movie": "Puli", "Collection (Cr)": 3.27, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 5.1, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 6.5, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 7.17, "Status": "Top 2"},
    ],
    "Guntur": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.835, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 1.31, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 1.58, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 2.45, "Status": "Top 3"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 3.21, "Status": "All Time Record"},
    ],
    "Nellore": [
        {"Movie": "Annavaram", "Collection (Cr)": 0.475, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 0.60, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 0.76, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 1.03, "Status": "Top 2"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 1.51, "Status": "All Time Record"},
    ],
    "Coastal AP": [
        {"Movie": "Annavaram", "Collection (Cr)": 4.62, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 5.84, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 7.05, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 11.57, "Status": "All Time Record"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 15.42, "Status": "All Time Record"},
        {"Movie": "Sardaar Gabbar Singh", "Collection (Cr)": 18.69, "Status": "Top 2"},
    ],
    "AP/TS": [
        {"Movie": "Annavaram", "Collection (Cr)": 11.02, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 13.81, "Status": "All Time Record"},
        {"Movie": "Puli", "Collection (Cr)": 15.08, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 25.97, "Status": "All Time Record"},
        {"Movie": "Camera Man Gangatho Rambabu", "Collection (Cr)": 22, "Status": "Top 3"},
        {"Movie": "Attarintiki Daredi", "Collection (Cr)": 35.04, "Status": "All Time Record"},
        {"Movie": "Katamarayudu", "Collection (Cr)": 44.60, "Status": "Top 4"},
    ],
}

# Re-Release Opening Records Data
re_release_data = {
    "Nizam": [
        {"Movie": "Jalsa", "Collection (Cr)": 1.26, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 1.63, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 2.75, "Status": "All Time Record"},
    ],
    "East": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.09, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.47, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.24, "Status": "All Time Record"}
    ],
    "West": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.14, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.39, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.09, "Status": "Top 2"}
    ],
    "UA": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.26, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.53, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.29, "Status": "All Time Record"}
    ],
    "Ceeded": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.39, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.44, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.812, "Status": "All Time Record"},
    ],
    "Guntur": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.11, "Status": "Top 2"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.46, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.165, "Status": "All Time Record"}
    ],
    "Krishna": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.22, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.39, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.28, "Status": "All Time Record"},
    ],
    "Nellore": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.11, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.11, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.045, "Status": "Top 2"}
    ],
    "Coastal AP": [
        {"Movie": "Gabbar Singh", "Collection (Cr)": 2.35, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 1.11, "Status": "Top 2"},
        {"Movie": "Jalsa", "Collection (Cr)": 1.55, "Status": "All Time Record"},
    ],
    "AP/TS": [
        {"Movie": "Jalsa", "Collection (Cr)": 2.57, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 3.18, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 5.91, "Status": "All Time Record"},
    ],
    "Karnataka": [
        {"Movie": "Jalsa", "Collection (Cr)": 0.112, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 0.226, "Status": "All Time Record"},
        {"Movie": "Gabbar Singh", "Collection (Cr)": 0.51, "Status": "All Time Record"},
    ],
    "World Wide": [
        {"Movie": "Gabbar Singh", "Collection (Cr)": 7.532, "Status": "All Time Record"},
        {"Movie": "Kushi", "Collection (Cr)": 3.7, "Status": "All Time Record"},
        {"Movie": "Jalsa", "Collection (Cr)": 3.20, "Status": "All Time Record"},
    ],
}

# USA Premier Records Data (Since 2011)
usa_premier_data = [
    {"Movie": "Panjaa", "Collection": "$93K", "Status": "All Time Record"},
    {"Movie": "Gabbar Singh", "Collection": "$163K", "Status": "All Time Record"},
    {"Movie": "Camera Man Gangatho Rambabu", "Collection": "$173K", "Status": "All Time Record"},
    {"Movie": "Attarintiki Daredi", "Collection": "$345K", "Status": "All Time Record"},
    {"Movie": "Sardaar Gabbar Singh", "Collection": "$616K", "Status": "Top 2"},
    {"Movie": "Agnyaathavaasi", "Collection": "$1.52M", "Status": "Top 2"},
    {"Movie": "Bheemla Nayak", "Collection": "$878K", "Status": "Top 7"},
]

if nav_choice == "Records":
    if selected_record_type == "-- Select --":
        # Main landing page
        st.markdown("<div style='text-align: center; margin-top: 30px;'>", unsafe_allow_html=True)
        st.video("OG.MP4")
        st.markdown("""
            <h1 style='color: #FFD700; font-size: 2.5em; margin-bottom: 10px;'>Pawan Kalyan</h1>
            <p style='color: #E0E0E0; font-size: 1.2em; max-width: 700px; margin: 0 auto;'>
                Pawan Kalyan, fondly known as Power Star, is not only one of the most celebrated actors in Telugu cinema but also a dynamic leader and a symbol of inspiration for millions. Renowned for his electrifying screen presence, record-shattering box office performances, and a legacy of blockbuster films, he has set new benchmarks in the Indian film industry. <br><br>
                Beyond cinema, Pawan Kalyan serves as the <b>Deputy Chief Minister of Andhra Pradesh</b> and the <b>MLA of Pithapuram</b>, exemplifying his commitment to public service and leadership. He is widely respected for his philanthropic activities, generous donations, and unwavering support for social causes, making a significant impact on countless lives. <br><br>
                As a true icon, Pawan Kalyan continues to inspire with his humility, dedication, and vision—both on and off the screen. This app celebrates his phenomenal Day 1 and Closing box office records across various territories, as well as his remarkable journey as a superstar and a great leader.
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif selected_record_type == "Opening Records":
        area_options = list(data.keys())
        selected_area = st.sidebar.selectbox("Select Area", area_options)
        movies = data[selected_area]
        st.markdown(f"<h2>{selected_area} Collections</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-container">', unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, movie in enumerate(movies):
                col = cols[idx % 3]
                with col:
                    st.markdown(f"""
                        <div style='text-align: center; margin-bottom: 10px; margin-top: 20px;'>
                            <span style='font-weight: bold; font-size: 1.1em;'>{movie['Movie']}</span><br>
                            <span style='color: #FFD700; font-size: 1.1em;'>{movie['Collection (Cr)']} Cr</span>
                        </div>
                    """, unsafe_allow_html=True)
                    img_path = image_paths.get(movie["Movie"], "")
                    if img_path and os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown("<div style='color:#FFD700;'>Image not available</div>", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div style='text-align: center; margin-top: 10px; margin-bottom: 30px;'>
                            <span style='color: #E0E0E0; background: #333; padding: 4px 12px; border-radius: 8px; font-size: 1em;'>{movie['Status']}</span>
                        </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Summary for ATR and Top 2
            atr_movies = set(movie['Movie'] for movie in movies if 'ATR' in movie['Status'].upper() or 'ALL TIME RECORD' in movie['Status'].upper())
            top2_movies = set(movie['Movie'] for movie in movies if 'TOP 2' in movie['Status'].upper())
            atr_count = len(atr_movies)
            top2_count = len(top2_movies)
            total_unique = len(atr_movies.union(top2_movies))
            st.markdown(f"""
                <div style='text-align: center; margin-top: 20px; margin-bottom: 40px;'>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR (All Time Record): {atr_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>Top 2: {top2_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR + Top 2: {total_unique} films ended up as Top 1 / 2</span>
                </div>
            """, unsafe_allow_html=True)
    elif selected_record_type == "First Week Records":
        area_options = list(first_week_data.keys())
        selected_area = st.sidebar.selectbox("Select Area", area_options)
        movies = first_week_data[selected_area]
        st.markdown(f"<h2>{selected_area} Collections</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-container">', unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, movie in enumerate(movies):
                col = cols[idx % 3]
                with col:
                    st.markdown(f"""
                        <div style='text-align: center; margin-bottom: 10px; margin-top: 20px;'>
                            <span style='font-weight: bold; font-size: 1.1em;'>{movie['Movie']}</span><br>
                            <span style='color: #FFD700; font-size: 1.1em;'>{movie['Collection (Cr)']} Cr</span>
                        </div>
                    """, unsafe_allow_html=True)
                    img_path = image_paths.get(movie["Movie"], "")
                    if img_path and os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown("<div style='color:#FFD700;'>Image not available</div>", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div style='text-align: center; margin-top: 10px; margin-bottom: 30px;'>
                            <span style='color: #E0E0E0; background: #333; padding: 4px 12px; border-radius: 8px; font-size: 1em;'>{movie['Status']}</span>
                        </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Summary for ATR and Top 2
            atr_movies = set(movie['Movie'] for movie in movies if 'ATR' in movie['Status'].upper() or 'ALL TIME RECORD' in movie['Status'].upper())
            top2_movies = set(movie['Movie'] for movie in movies if 'TOP 2' in movie['Status'].upper())
            atr_count = len(atr_movies)
            top2_count = len(top2_movies)
            total_unique = len(atr_movies.union(top2_movies))
            st.markdown(f"""
                <div style='text-align: center; margin-top: 20px; margin-bottom: 40px;'>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR (All Time Record): {atr_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>Top 2: {top2_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR + Top 2: {total_unique} films ended up as Top 1 / 2</span>
                </div>
            """, unsafe_allow_html=True)
    elif selected_record_type == "Re-Release Opening Records":
        area_options = list(re_release_data.keys())
        selected_area = st.sidebar.selectbox("Select Area", area_options)
        movies = re_release_data[selected_area]
        st.markdown(f"<h2>{selected_area} Re-Release Opening Records</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-container">', unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, movie in enumerate(movies):
                col = cols[idx % 3]
                with col:
                    st.markdown(f"""
                        <div style='text-align: center; margin-bottom: 10px; margin-top: 20px;'>
                            <span style='font-weight: bold; font-size: 1.1em;'>{movie['Movie']}</span><br>
                            <span style='color: #FFD700; font-size: 1.1em;'>{movie['Collection (Cr)']} Cr</span>
                        </div>
                    """, unsafe_allow_html=True)
                    img_path = image_paths.get(movie["Movie"], "")
                    if img_path and os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown("<div style='color:#FFD700;'>Image not available</div>", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div style='text-align: center; margin-top: 10px; margin-bottom: 30px;'>
                            <span style='color: #E0E0E0; background: #333; padding: 4px 12px; border-radius: 8px; font-size: 1em;'>{movie['Status']}</span>
                        </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Summary for ATR and Top 2
            atr_movies = set(movie['Movie'] for movie in movies if 'ATR' in movie['Status'].upper() or 'ALL TIME RECORD' in movie['Status'].upper())
            top2_movies = set(movie['Movie'] for movie in movies if 'TOP 2' in movie['Status'].upper())
            atr_count = len(atr_movies)
            top2_count = len(top2_movies)
            total_unique = len(atr_movies.union(top2_movies))
            st.markdown(f"""
                <div style='text-align: center; margin-top: 20px; margin-bottom: 40px;'>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR (All Time Record): {atr_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>Top 2: {top2_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR + Top 2: {total_unique} films ended up as Top 1 / 2</span>
                </div>
            """, unsafe_allow_html=True)
    elif selected_record_type == "USA Premier Records":
        st.markdown("<h2>USA Premier Records</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1.1em; margin-bottom:16px;'><b>Note:</b> Data since 2011 only</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-container">', unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, movie in enumerate(usa_premier_data):
                col = cols[idx % 3]
                with col:
                    st.markdown(f"""
                        <div style='text-align: center; margin-bottom: 10px; margin-top: 20px;'>
                            <span style='font-weight: bold; font-size: 1.1em;'>{movie['Movie']}</span><br>
                            <span style='color: #FFD700; font-size: 1.1em;'>{movie['Collection']}</span>
                        </div>
                    """, unsafe_allow_html=True)
                    img_path = image_paths.get(movie["Movie"], "")
                    if img_path and os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown("<div style='color:#FFD700;'>Image not available</div>", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div style='text-align: center; margin-top: 10px; margin-bottom: 30px;'>
                            <span style='color: #E0E0E0; background: #333; padding: 4px 12px; border-radius: 8px; font-size: 1em;'>{movie['Status']}</span>
                        </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Summary for ATR and Top 2
            atr_movies = set(movie['Movie'] for movie in usa_premier_data if 'ATR' in movie['Status'].upper() or 'ALL TIME RECORD' in movie['Status'].upper())
            top2_movies = set(movie['Movie'] for movie in usa_premier_data if 'TOP 2' in movie['Status'].upper())
            atr_count = len(atr_movies)
            top2_count = len(top2_movies)
            total_unique = len(atr_movies.union(top2_movies))
            st.markdown(f"""
                <div style='text-align: center; margin-top: 20px; margin-bottom: 40px;'>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR (All Time Record): {atr_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>Top 2: {top2_count}</span><br>
                    <span style='color: #FFD700; font-weight: bold; font-size: 1.1em;'>ATR + Top 2: {total_unique} films ended up as Top 1 / 2</span>
                </div>
            """, unsafe_allow_html=True)
    elif selected_record_type == "Closing Records":
        closing_records = [
            {
                "title": "Annavaram",
                "image": image_paths.get("Annavaram", ""),
                "data": [
                    ("Nizam", "₹5.9cr"),
                    ("Ceded", "₹3.7cr"),
                    ("Vizag (UA)", "₹1.85cr"),
                    ("East", "₹1.6cr"),
                    ("West", "₹1.25cr"),
                    ("Krishna", "₹1.35cr"),
                    ("Guntur", "₹1.6cr"),
                    ("Nellore", "₹0.85cr"),
                    ("Total Ap/Tg Closing Share", "₹18.1 CR"),
                    ("Karnataka Share", "₹1.35 CR+"),
                    ("Rest of India Share", "₹0.25 CR"),
                    ("Overseas Share", "₹0.70 CR"),
                    ("Total WorldWide Closing collections", "Share - ₹20.4 CR+ | Gross - ₹31 CR+"),
                ],
                "note": "Second Highest Collected movie for #PawanKalyan after #Kushi (2001)"
            },
            {
                "title": "Puli",
                "image": image_paths.get("Puli", ""),
                "data": [
                    ("Nizam", "₹5.65cr"),
                    ("Ceded", "₹3.8cr"),
                    ("Vizag(UA)", "₹1.75cr"),
                    ("East", "₹1.34cr"),
                    ("West", "₹1.18cr"),
                    ("Krishna", "₹1.37cr"),
                    ("Guntur", "₹1.58cr"),
                    ("Nellore", "₹0.94cr"),
                    ("Total", "₹17.61 CR (Excl Sg)"),
                    ("Karnataka+ROI", "₹1.55CR"),
                    ("Overseas", "₹0.3CR"),
                    ("Total WW", "Share- ₹19.46 CR | Gross- ₹29 CR"),
                ],
                "note": None
            },
            {
                "title": "Kushi",
                "image": image_paths.get("Kushi", ""),
                "data": [
                    ("Nizam", "₹8.2cr"),
                    ("Ceded", "₹3.9cr"),
                    ("Vizag (UA)", "₹2cr"),
                    ("East", "₹1.47cr"),
                    ("West", "₹1.35cr"),
                    ("Krishna", "₹1.75cr"),
                    ("Guntur", "₹1.43cr"),
                    ("Nellore", "₹0.87cr"),
                    ("Total AP/TG Share", "₹20.97 CR Approx"),
                    ("Karnataka + Rest of India Share", "₹55 Lkhs+"),
                    ("Overseas Share", "₹40 Lkhs+"),
                    ("Total Worldwide Closing Collections", "Share - ₹21.92 CR Approx | Gross - ₹37 CR+ Approx (Estimates)"),
                ],
                "note": "All Time Telugu Film Industry Hit in both Gross & Share"
            },
            {
                "title": "Jalsa",
                "image": image_paths.get("Jalsa", ""),
                "data": [
                    ("Nizam", "₹9.43cr"),
                    ("Ceded", "₹4.5cr"),
                    ("Vizag (UA)", "₹2.85cr"),
                    ("East", "₹2.1cr"),
                    ("West", "₹1.8cr"),
                    ("Krishna", "₹1.82cr"),
                    ("Guntur", "₹2.05cr"),
                    ("Nellore", "₹1.1cr"),
                    ("Total Ap/Tg", "₹25.65 CR"),
                    ("Karnataka + Rest of India", "₹1.6cr"),
                    ("Overseas", "₹2.3cr"),
                    ("Total Worldwide Collections", "Share - ₹29.55 CR | Gross - ₹49 CR Approx"),
                ],
                "note": "All Time Top 2"
            },
            {
                "title": "Attarintiki Daredi",
                "image": image_paths.get("Attarintiki Daredi", ""),
                "data": [
                    ("Nizam", "₹23.6cr"),
                    ("Ceded", "₹10.5cr"),
                    ("Vizag (UA)", "₹6.3cr"),
                    ("East", "₹4.06cr"),
                    ("West", "₹3.38cr"),
                    ("Krishna", "₹3.69cr"),
                    ("Guntur", "₹5.1cr"),
                    ("Nellore", "₹2.63cr"),
                    ("Total Ap/Tg", "₹59.26 CR (Excluding Overflows)"),
                    ("Ap/Tg Share | Gross", "₹59.26cr | ₹97cr"),
                    ("Karnataka", "₹5.61cr | ₹12cr"),
                    ("TN + Rest of India", "₹1.65 CR | ₹4cr"),
                    ("Overseas", "₹9.3cr | ₹17cr"),
                    ("Total Worldwide", "₹75.82 CR | ₹130 CR"),
                    ("Total All India Share", "₹66.52 CR"),
                    ("Total All India Gross", "₹113 CR"),
                    ("Total WorldWide Share Including Overflows", "₹76-77cr (approx)")
                ],
                "note": None
            },
            {
                "title": "Bheemla Nayak",
                "image": image_paths.get("Bheemla Nayak", ""),
                "data": [
                    ("Nizam", "35.02Cr"),
                    ("Ceeded", "11.22Cr"),
                    ("UA", "7.65Cr"),
                    ("East", "5.49Cr"),
                    ("West", "5.11Cr"),
                    ("Guntur", "5.26Cr"),
                    ("Krishna", "4.29Cr"),
                    ("Nellore", "2.80Cr"),
                    ("AP-TG Total", "76.84CR (117.85Cr~ Gross)"),
                    ("KA+ROI", "8.24Cr"),
                    ("OS", "12.55Cr"),
                    ("Total World Wide", "97.63CR (159.10CR~ Gross)")
                ],
                "note": "NOTE : WOULD HAVE CROSSED 130C EASILY IF PROPER SHOWS AND TICKET HIKES WERE GIVEN BY THE GOVERNMENT. LOT OF GOVT HURDLES DURING RELEASE CAUSED A LOSS OF AROUND 20C ALONE IN AP."
            },
            {
                "title": "Vakeel Saab",
                "image": image_paths.get("Vakeel Saab", ""),
                "data": [
                    ("Nizam", "₹24cr/₹26.9cr"),
                    ("Ceded", "₹12.9cr"),
                    ("Vizag", "₹10.45cr/₹11.7cr"),
                    ("East", "₹6.5cr/₹7.28cr"),
                    ("West", "₹6.55cr/₹7.32cr"),
                    ("Krishna", "₹4.65cr/₹5.2cr"),
                    ("Guntur", "₹6.6cr/₹7.4cr"),
                    ("Nellore", "₹3.05cr/3.4cr"),
                    ("Total Ap/Tg Share", "₹74.7 CR/₹82.1 CR"),
                    ("Ap/Tg Share | Gross", "₹74.7cr(₹82.1cr Incl GST) | ₹124cr"),
                    ("Karnataka", "₹3.5cr | ₹7cr"),
                    ("Tamilnadu+Rest of India", "₹0.8cr | ₹1.8cr"),
                    ("Overseas", "₹4.6cr | ₹10.3cr"),
                    ("Total Worldwide", "Share - ₹83.6 CR (Excl GST) | Share - ₹91 CR (Incl GST) | Gross - ₹143.1 CR")
                ],
                "note": None
            },
            {
                "title": "Badri",
                "image": "Badri.jpeg",
                "data": [
                    ("AP/TS Share", "₹13.1 CR Approx"),
                    ("AP/TS Gross", "₹21 CR"),
                    ("Nizam", "Crossed 4Cr share mark in nizam [2000]")
                ],
                "note": None
            },
            {
                "title": "Thammudu",
                "image": "Thammudu.jpg",
                "data": [
                    ("Nizam", "₹3.20 crore"),
                    ("Andhra Pradesh", "₹6.05 crore"),
                    ("AP/TS", "₹9.25 crore")
                ],
                "note": None
            },
            {
                "title": "Panjaa",
                "image": image_paths.get("Panjaa", ""),
                "data": [
                    ("Nizam", "5.20C"),
                    ("Ceeded", "2.80C"),
                    ("Vizag", "1.60C"),
                    ("East", "1.30C"),
                    ("West", "1.15C"),
                    ("Krishna", "1.10C"),
                    ("Guntur", "1.90C"),
                    ("Nellore", "0.60C"),
                    ("Total AP/TS", "15.65 Crores"),
                    ("Karnataka", "1.00C"),
                    ("Rest of India", "0.40C"),
                    ("Overseas", "1.75C"),
                    ("WORLDWIDE", "18.8 Crores")
                ],
                "note": None
            },
            # Add Kushi (Re-Release) closing record
            {
                "title": "Kushi (Re-Release)",
                "image": image_paths.get("Kushi", ""),
                "data": [
                    ("Vizag(UA)", "₹40 Lkhs - ₹42 Lkhs"),
                    ("East", "₹42 Lkhs"),
                    ("West", "₹14 Lkhs"),
                    ("Krishna", "₹40 Lkhs"),
                    ("Guntur", "₹33 Lkhs"),
                    ("Nellore", "₹9 Lkhs"),
                    ("Andhra", "₹1.8 CR Approx"),
                    ("Ceded", "₹80 Lkhs (Incl bellary)"),
                    ("Nizam", "₹2.85 CR"),
                    ("Total Ap/Tg", "₹5.45 CR Approx"),
                    ("Karnataka", "₹42 Lkhs"),
                    ("TN + Rest of India", "₹14 Lkhs"),
                    ("Total All India Gross", "₹6.01 CR Approx"),
                    ("Overseas", "₹37 Lkhs"),
                    ("USA + Canada", "$24,296 (₹19.7 Lkhs)"),
                    ("Australia", "$8,141 (₹4.3 Lkhs)"),
                    ("UK", "£13,211 (₹13 Lkhs)"),
                    ("Total Worldwide Gross", "₹6.38 CR Approx")
                ],
                "note": "ALL TIME RECORD IN RE-RELEASES"
            },
            # Add Jalsa (Special Shows) closing record
            {
                "title": "Jalsa (Special Shows)",
                "image": image_paths.get("Jalsa", ""),
                "data": [
                    ("Nizam", "1.26Cr"),
                    ("Ceeded", "39L"),
                    ("UA", "26L"),
                    ("East", "9L"),
                    ("West", "14L"),
                    ("Guntur", "11L"),
                    ("Krishna", "22L"),
                    ("Nellore", "11L"),
                    ("AP-TG Total", "2.57CR Gross"),
                    ("Rest of India", "22L~"),
                    ("Overseas", "40L~"),
                    ("Total World Wide", "3.20CR Gross")
                ],
                "note": None
            },
            {
                "title": "Gabbar Singh",
                "image": image_paths.get("Gabbar Singh", ""),
                "data": [
                    ("Nizam", "19.5CR"),
                    ("Ceeded", "9.30CR"),
                    ("UA", "5.50CR"),
                    ("East", "3.75CR"),
                    ("West", "3.20CR"),
                    ("Krishna", "3.20CR"),
                    ("Guntur", "4.35CR"),
                    ("Nellore", "2.05CR"),
                    ("AP/TS", "50.85CR"),
                    ("KA", "3.30CR"),
                    ("ROI", "0.90CR"),
                    ("OS", "5.50CR"),
                    ("TOTAL WORLD WIDE", "60.55CR")
                ],
                "note": "[ALL TIME TOP 2 OVERALL]<br>NON-SSR INDUSTRY HIT"
            }
        ]
        st.markdown("<h2 style='color:#FFD700;'>Closing Records</h2>", unsafe_allow_html=True)
        tab_titles = [record["title"] for record in closing_records]
        tabs = st.tabs(tab_titles)
        for tab, record in zip(tabs, closing_records):
            with tab:
                st.markdown(f"<div class='section-container' style='margin-bottom:32px;'>", unsafe_allow_html=True)
                cols = st.columns([1, 3])
                with cols[0]:
                    img_path = record["image"]
                    if img_path and os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown("<div style='color:#FFD700;'>Image not available</div>", unsafe_allow_html=True)
                with cols[1]:
                    st.markdown(f"<h3 style='color:#FFD700;'>{record['title']}</h3>", unsafe_allow_html=True)
                    table_html = "<table class='custom-table'><tbody>"
                    for row in record["data"]:
                        table_html += f"<tr><td style='color:#FFD700;font-weight:bold;width:200px'>{row[0]}</td><td style='color:#fff;font-size:1.1em'>{row[1]}</td></tr>"
                    table_html += "</tbody></table>"
                    st.markdown(table_html, unsafe_allow_html=True)
                    if record["note"]:
                        st.markdown(f"<div style='color:#FFD700; font-size:1.1em; margin-top:8px;'><b>Note:</b> {record['note']}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    elif selected_record_type == "Town Records (Full Run)":
        town_data = [
            ("Kakinada Town", [("Kushi", "37L"), ("Jalsa", "53L"), ("Gabbar Singh", "98.5L")]),
            ("BVRM Town", [("Kushi", "21L"), ("Gabbar Singh", "66L")]),
            ("Amalapuram Town", [("Badri", "13L"), ("Kushi", "14.30L")]),
            ("RJY Town", [("Jalsa", "47L")]),
            ("Gudiwada Town", [("Kushi", "18.60L")]),
            ("MTM Town", [("Kushi", "18.50L")]),
            ("Mandapeta Town", [("Kushi", "14.50L"), ("Gopala Gopala", "25.22L")]),
            ("Ongole Town", [("Kushi", "20.56L"), ("Attarintiki Daredi", "76L")]),
            ("Kadapa Town", [("Kushi", "26L")]),
            ("Nellore Town", [("Kushi", "43.40L"), ("Attarintiki Daredi", "86L")]),
            ("Tirupati", [("Kushi", "33L"), ("Gabbar Singh", "83L"), ("Attarintiki Daredi", "93L")]),
            ("Kavali Town", [("Kushi", "7.40L")]),
            ("Macherla A", [("Gabbar Singh", "13.7L*"), ("Attarintiki Daredi", "14.4L")]),
            ("Kurnool Town", [("Kushi", "31L"), ("Attarintiki Daredi", "77.58L")]),
            ("Guntur City", [("Gabbar Singh", "1.02Cr"), ("Attarintiki Daredi", "1.16Cr")]),
            ("Vijayawada City", [("Kushi", "87L"), ("Attarintiki Daredi", "1.88Cr")]),
            ("Anakapalli Town", [("Kushi", "30.17L"), ("Attarintiki Daredi", "50.08L")]),
            ("Vizag City", [("Badri", "1.14Cr"), ("Kushi", "1.38Cr"), ("Gabbar Singh", "4.80Cr-5Cr")]),
            ("Ananthapur Town", [("Kushi", "29.20L")]),
            ("Pithapuram Town", [("Kushi", "9.20L"), ("Annavaram", "14L")]),
            ("Bobbili Town", [("Kushi", "6.47L")]),
            ("Tiruvuru Town", [("Kushi", "7.95L")]),
        ]
        total_town_records = sum(len(movies) for _, movies in town_data)
        st.markdown("<h2 style='color:#FFD700;'>Town Records (Full Run)</h2>", unsafe_allow_html=True)
        for town, records in town_data:
            st.markdown(f"<div class='section-container' style='margin-bottom:18px;'>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:#FFD700;'>{town}</h3>", unsafe_allow_html=True)
            table_html = "<table class='custom-table'><thead><tr><th>Movie</th><th>Collection</th></tr></thead><tbody>"
            for movie, collection in records:
                table_html += f"<tr><td style='color:#FFD700;font-weight:bold'>{movie}</td><td style='color:#fff;font-size:1.1em'>{collection}</td></tr>"
            table_html += "</tbody></table>"
            st.markdown(table_html, unsafe_allow_html=True)
            st.markdown(f"<div style='color:#FFD700; font-size:1em; margin-top:4px;'>Records in this town: <b>{len(records)}</b></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align:center; color:#FFD700; font-size:1.2em; margin-top:24px;'><b>Total Town Records: {total_town_records}</b></div>", unsafe_allow_html=True)

elif nav_choice == "Center Wise Data":
    def generate_centerwise_table(data, headers):
        table_style = """
        <style>
        .centerwise-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 24px;
            font-size: 1.2em;
            background: #23282c;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(255,215,0,0.25);
        }
        .centerwise-table th {
            background: #FFD700;
            color: #23282c;
            font-weight: bold;
            padding: 12px 10px;
            text-align: left;
            font-size: 1.1em;
        }
        .centerwise-table td {
            padding: 10px 10px;
            color: #fff;
            border-bottom: 1px solid #444;
        }
        .centerwise-table tr:nth-child(even) {
            background: #2a2f33;
        }
        .centerwise-table tr:nth-child(odd) {
            background: #23282c;
        }
        </style>
        """
        table_html = f"<table class='centerwise-table'><thead><tr>{''.join([f'<th>{h}</th>' for h in headers])}</tr></thead><tbody>"
        for row in data:
            table_html += "<tr>" + ''.join([f'<td>{cell}</td>' for cell in row]) + "</tr>"
        table_html += "</tbody></table>"
        return table_style + table_html

    if selected_centerwise_movie == "Gabbar Singh":
        st.markdown("<h2 style='color:#FFD700;'>Gabbar Singh - Center Wise Data</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>ATR</b> = All Time Record, <b>Sh</b> = Share</div>", unsafe_allow_html=True)

        # Day 1 ATR Centers
        gs_day1_atr = [
            ("Gudem", "5.6L"),
            ("BVRM", "17.3L"),
            ("Hanuman Junction", "4.09L [ATR]"),
            ("Kakinada", "11.50L [SH]"),
            ("MTM", "8L [ATR]")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Day 1 ATR Centers</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_day1_atr, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # First Week ATR Centers
        gs_first_week_atr = [
            ("KKD", "43.50L"),
            ("MDP", "25.94L"),
            ("Tanuku", "21L"),
            ("KRM", "34L"),
            ("ATP", "26.55L"),
            ("Kurnool Town", "47.35L"),
            ("Ongole", "30.8L"),
            ("Khammam", "25.75L"),
            ("Gudem", "15.3L (Sh)"),
            ("BVRM", "54.6L"),
            ("Proddutur", "23L (Sh)"),
            ("Kadapa", "30.2L (Sh)"),
            ("Vizag", "1.07C (Sh)")
        ]
        st.markdown("<h4 style='color:#FFD700;'>First Week ATR Centers</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_first_week_atr, ["Center", "First Week Collection"]), unsafe_allow_html=True)

        # 1 Cr+ Gross Centers
        st.markdown("<h4 style='color:#FFD700;'>1 Cr+ Gross Centers</h4>", unsafe_allow_html=True)
        gs_1cr_centers = [
            "X ROADS", "PRASAD MULTIPLEX", "DILSUKH NAGAR", "KUKATPALLY", "VIZAG", "GAJUWAKA", "KAKINADA", "RAJAHMUNDRY", "BHEEMAVARAM", "VIJAYAWADA", "GUNTUR", "NELLORE", "TIRUPATHI", "KURNOOL", "WARANGAL", "KARIMNAGAR"
        ]
        st.markdown("<ul style='color:#FFD700; font-size:1.1em;'>" + ''.join([f"<li>{center}</li>" for center in gs_1cr_centers]) + "</ul>", unsafe_allow_html=True)

        # X Roads Closing Gross Table
        st.markdown("<h4 style='color:#FFD700;'>X Roads Closing Gross</h4>", unsafe_allow_html=True)
        xroads_gross = [
            ("Sandhya70mm", "94,64,309/-"),
            ("Devi", "29,07,565/-")
        ]
        st.markdown(generate_centerwise_table(xroads_gross, ["Theatre", "Closing Gross"]), unsafe_allow_html=True)

        # Kukatpally 47 Days Gross Table
        st.markdown("<h4 style='color:#FFD700;'>Kukatpally 47 Days Gross</h4>", unsafe_allow_html=True)
        kukatpally_gross = [
            ("Brahmaramba", "47,18,521"),
            ("Arjun", "40,36,376"),
            ("Shivaparvathi", "21,00,500")
        ]
        st.markdown(generate_centerwise_table(kukatpally_gross, ["Theatre", "Closing Gross"]), unsafe_allow_html=True)

        # Records (rest as points)
        st.markdown("<h4 style='color:#FFD700;'>Records</h4>", unsafe_allow_html=True)
        gs_records = [
            "1st movie to run for 50 days in 2 theaters in Kukatpally",
            "FIRST TIME EVER in History of NELLORE: GS 69 days 1 Cr gross (1,00,20,000) in a Single theatre S2 multiplex",
            "GS is the 1st movie to collect 1cr share in Guntur City..",
            "Cineplanet Kompally Gross - 65 lakhs..All time record..",
            "First movie to run for 50 days in 2 theaters in Kukatpally"
        ]
        st.markdown("<ul style='color:#FFD700; font-size:1.1em;'>" + ''.join([f"<li>{rec}</li>" for rec in gs_records]) + "</ul>", unsafe_allow_html=True)

    elif selected_centerwise_movie == "Sardaar Gabbar Singh":
        sgs_day1_centers = [
            ("Nandhyala", "14.3L"),
            ("Eluru", "30.32L"),
            ("Tanuku", "23.27L"),
            ("Gudem", "16.17L"),
            ("NDVLE", "7.4L"),
            ("MTM", "17.2L"),
            ("Gudiwada", "10.03L"),
            ("Tenali", "21L (Sh)"),
            ("Kavali", "6.7L (Sh)"),
            ("ATP", "28.63L"),
            ("Dharmavaram", "9.28L"),
            ("KKD", "42.84L (Sh)"),
            ("Mandapeta", "11.3L (Sh)"),
            ("AMP", "10.4L (Sh)"),
            ("Yemmiganuru", "6.9L"),
            ("Nagari", "2.07L"),
            ("Nandikotukuru", "5.7L"),
            ("Peddapuram", "8.7L"),
            ("NSPETA", "22L"),
            ("Mydukuru", "1.98L"),
            ("Satenapallli", "9.1L"),
            ("Kodumuru", "2.86L"),
            ("Anaparthi", "5.6L (Sh)"),
            ("Bhimavaram", "49.6L"),
            ("Kurnool", "32.24L"),
            ("Kadapa", "22.8L"),
            ("Proddutur", "16.09L"),
            ("Adhoni", "15.49L"),
            ("Pithapuram", "6.75L"),
            ("Chirala", "6.75L"),
        ]
        st.markdown("<h2 style='color:#FFD700;'>Sardaar Gabbar Singh - ATR Centers Day 1</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>Sh</b> = Share</div>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(sgs_day1_centers, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "Vakeel Saab":
        st.markdown("<h2 style='color:#FFD700;'>Vakeel Saab - Centerwise Collections</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>Sh</b> = Share, <b>Gross</b> = Gross Collection</div>", unsafe_allow_html=True)

        vs_guntur_ongole = [
            ("Ongole", "30.38L (Sh)"), ("Tenali", "21.52L (Sh)"), ("Chpeta", "14.8L"), ("Npeta", "17.8L"), ("Chirala", "11.48L"), ("Bapatla", "10.51L"), ("Repalle", "7.78L"), ("Vinukonda", "9.49L"), ("Macherla", "7.86L"), ("Sattenapalli", "7.8L"), ("Piduguralla", "6.5L"), ("Ponnur", "5.58L"), ("Amaravathi", "5L"), ("Giddalur", "3.8L"), ("Markapur", "11.50L"), ("Kanigiri", "4.10L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Guntur & Ongole District Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_guntur_ongole, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        vs_east_godavari = [
            ("Kakinada", "54L (Sh)"), ("Anaparthi", "5.73L"), ("Pithapuram", "11.68L"), ("Amalapuram", "25L (Sh)"), ("Gollaprolu", "4.40L"), ("Jaggampeta", "15.5L"), ("Mandapeta", "18.5L (Sh)"), ("Tatipaka", "9L (Sh)")
        ]
        st.markdown("<h4 style='color:#FFD700;'>East Godavari Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_east_godavari, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        vs_west_godavari = [
            ("Bhimavaram", "46.64L"), ("Eluru", "36.66L"), ("Tanuku", "31.73L"), ("Tadepalligudem", "13.74L"), ("Nidadavole", "9.81L"), ("Chintalapudi", "5.32L"), ("Ganapavaram", "7.73L"), ("Kalla", "2.69L"), ("Devarapalli", "2.99L"), ("Valluru", "3.03L"), ("Nallajarla", "3.23L"), ("Chagallu", "2.59L"), ("Bhimadolu", "4.05L"), ("Tallapudi", "3.34L"), ("Undi", "1.8L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>West Godavari Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_west_godavari, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        vs_vizag = [
            ("Vizag", "104.03L"), ("Srikakulam", "29.40L"), ("Gajuwaka", "23.71L"), ("Gop.patnam", "12.81L"), ("Kancharpalem", "3.52L"), ("Tekkali", "2.95L"), ("Palasa", "12.51L"), ("Chodavaram", "9.86L"), ("Sompeta (main)", "3.48L"), ("Parawada", "2.74L"), ("Pedagantyada", "3.40L"), ("Vizianagaram", "37.54L"), ("Anakapalle", "21.29L"), ("Pendurthi", "4.86L"), ("Bobbili", "18.63L"), ("Palakonda", "4.1L (2shows)")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Vizag Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_vizag, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        vs_ceded = [
            ("Kurnool", "45.75L"), ("Tirupathi", "45.5L"), ("Kadapa", "38.04L"), ("Ananthapur", "32.13L"), ("Nandyala", "31.33L"), ("Proddutur", "21.50L"), ("Chittor", "15.68L"), ("Adoni", "14.68L"), ("Gunthakal", "11.4L"), ("Nandikotkur", "5.82L"), ("Railwaykodur", "7L"), ("Tadipatri", "12.25L"), ("Kadiri", "5.20L"), ("Jammalamadugu", "2.75L"), ("Guntakal", "11.40L"), ("Penukonda", "4.68L"), ("Kalyandurg", "2.50L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Ceded Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_ceded, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        vs_nizam = [
            ("Khammam", "30.31L"), ("Prasadz", "26.35L"), ("Nizamabad", "21.7L"), ("Cineplanet", "16.69L"), ("AMB Cinemas", "16.5L"), ("Mahabubnagar", "16.4L"), ("Suryapeta", "8.47L"), ("Kodad", "7.90L"), ("Manugur", "2.40L"), ("X-Roads", "34.40L"), ("Karimanagar", "26.85L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Nizam Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_nizam, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        vs_others = [
            ("Yemmiganur", "6.36L"), ("Kavali", "12.18L"), ("Machilipatnam", "19.01L"), ("Jangareddygudem", "19.6L gross (BS Gross 6.85L)"), ("Hindupur+Dharmavaram", "26.35L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Few Other Centers Day 1 Collection</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_others, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # First Week Gross Table
        vs_first_week_gross = [
            ("Vizag City", "3.07 Cr"), ("Kurnool", "1.46 Cr"), ("Tirupathi", "1.37 Cr"), ("Bhimavaram", "1.16 Cr"), ("Vizianagaram", "1.13 Cr"), ("Eluru", "1.07 Cr"), ("Anantapur", "1.00 Cr"), ("Kadapa", "97.7 L"), ("Srikakulam", "80.95 L"), ("Gajuwaka", "77.94 L"), ("Amalapuram", "65 L"), ("Nandyala", "64.91 L"), ("Tanuku", "63.56 L"), ("Proddutur", "59.6 L"), ("Anakapalli", "47.96 L"), ("Machilipatnam", "47.01 L"), ("Chittor", "41.08 L"), ("Adoni", "39.75 L"), ("T.P.Gudem", "37.75 L"), ("Gopalapatnam", "33.27 L"), ("Kavali", "32.96 L"), ("Chirala", "31.76 L"), ("Guntakal", "31.38 L"), ("Markapuram", "31.3 L"), ("Dharmavaram", "30.63 L"), ("Tadipatri", "30.35 L"), ("Narsapuram", "27 L"), ("Pithapuram", "25.93 L"), ("Chodavaram", "23.97 L"), ("Bapatla", "23.34 L"), ("Yemmiganur", "23.2 L"), ("Nayudupeta", "21.95 L"), ("Naidupeta", "21.95 L"), ("Sriharipuram", "19.35 L"), ("Macherla", "18.88 L"), ("Kodur", "17.36 L"), ("Pendurthi", "17.2 L"), ("Pulivendula", "16.94 L"), ("Kadiri", "16.83 L"), ("Gudur", "16.82 L"), ("Samalkot", "16.67 L"), ("Rajampeta", "16.24 L"), ("Venakatagiri", "15.45 L"), ("Rayachoti", "14.34 L"), ("Rayadurgam", "11.65 L"), ("Kandukur", "11.53 L"), ("Penukonda", "11.36 L"), ("Anaparthi", "11.02 L"), ("Pamuru", "10.53 L"), ("Parawada", "10.33 L"), ("Buchi", "9.38 L"), ("Giddalur", "9.1 L"), ("Kanigiri", "9.1 L"), ("Gooty", "9.09 L"), ("Pedagantyada", "8.92 L"), ("Kalyandurgam", "8.26 L"), ("Kota", "8.25 L"), ("Podili", "8.03 L"), ("Singarayakonda", "7.96 L"), ("Jammalamadugu", "7.59 L"), ("Gorantla", "7.44 L"), ("Badvel", "7.38 L"), ("Porumamilla", "6.32 L"), ("Pamidi", "6.2 L"), ("Uravakonda", "5.9 L"), ("Athmakur", "5.65 L"), ("Kothacheruvu", "5.57 L"), ("Chinamandem", "5.36 L"), ("Vemapalli", "5.15 L"), ("Mydukur", "4.57 L"), ("Vinjamur", "4.05 L"), ("Erraguntla", "2.65 L"), ("Kamalapuram", "1.88 L"), ("Duvvur", "1.19 L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>First Week Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(vs_first_week_gross, ["Center", "1st Week Gross"]), unsafe_allow_html=True)

        # 1Cr Centers of Vakeel Saab (First Week)
        st.markdown("<h4 style='color:#FFD700;'>1Cr Centers of Vakeel Saab (First Week)</h4>", unsafe_allow_html=True)
        centers_1cr = [
            "Tirupati",
            "Kurnool",
            "Anantapur",
            "Vizag",
            "Vizianagaram",
            "Kakinada",
            "Rajamundry",
            "Eluru",
            "Bhimavaram",
            "Vijayawada",
            "Guntur",
            "Ongole",
            "Nellore"
        ]
        st.markdown("<ul style='color:#FFD700; font-size:1.1em;'>" + ''.join([f"<li>{center}</li>" for center in centers_1cr]) + "</ul>", unsafe_allow_html=True)

    elif selected_centerwise_movie == "Bheemla Nayak":
        st.markdown("<h2 style='color:#FFD700;'>Bheemla Nayak - 1st Day Gross</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>Sh</b> = Share</div>", unsafe_allow_html=True)
        bn_day1_gross = [
            ("Khammam", "49.98L"), ("X- Roads", "39L"), ("Tirupathi", "36L"), ("Karimnagar", "31.58L"), ("Kurnool", "30.83L"), ("Kadapa", "30.5L"), ("Anantapur", "28.15L"), ("Bhimavaram", "27.67L"), ("Nizamabad", "25.16L"), ("Mahaboobnagar", "24L"), ("Eluru", "22L"), ("Vizianagaram", "19.79L"), ("Adoni", "14.37L"), ("Tadipatri", "13.72L"), ("Macherial", "13.5L"), ("Srikakulam", "13.27L"), ("Godavarikhani", "13L"), ("Gajuwaka", "12.14L"), ("Guntakal", "12L"), ("Miryalaguda", "12L"), ("Hindupur", "11.57L"), ("Kodad", "11.2L"), ("Shadnagar", "11L"), ("Satthupally", "9.86L"), ("Nandyala", "9.84L"), ("Amalapuram", "9.63L"), ("Kothagudem", "8.9L"), ("Dharmavaram", "8.5L"), ("Allagadda", "7.96L"), ("Kadiri", "7.02L"), ("Kavali", "6.75L"), ("Pithapuram", "6.12L"), ("Yemmiganur", "5.92L"), ("Palasa", "5.1L"), ("Nandikotkur", "4.5L"), ("Chirala", "5.44L"), ("Tangutur", "3.15L"), ("Bapatla", "3.05L"), ("Mandapeta", "12.63L (Sh)"),
            ("Nalgonda", "16L"), ("Wanaparthy", "5.3L"), ("Manugur", "5.28L")
        ]
        st.markdown(generate_centerwise_table(bn_day1_gross, ["Center", "1st Day Gross"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "Attarintiki Daredi":
        st.markdown("<h2 style='color:#FFD700;'>Attarintiki Daredi - Centerwise Records</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>Sh</b> = Share, <b>ATR</b> = All Time Record</div>", unsafe_allow_html=True)

        # First Week All Time Records
        ad_first_week = [
            ("Amp", "14.53L (Sh)"), ("KKD", "52.63L (Sh)"), ("RJY", "40.33L (Sh)"), ("PTP", "11.55L (Sh)"), ("Gudem", "20.30L (Sh)"), ("Nellore Town", "37.76L (Sh)"), ("Nandhyala", "23.52L (Sh)"), ("Kadapa District", "1.34Cr (Sh) [ATR]"), ("Chittoor District", "1.78Cr (Sh)"), ("Ananthapur District", "1.35Cr (Sh)"), ("DSNR", "72L (1Cr in 15 DAYS)")
        ]
        st.markdown("<h4 style='color:#FFD700;'>First Week All Time Records</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(ad_first_week, ["Center/District", "Share"]), unsafe_allow_html=True)

        # KPHB break-up
        ad_kphb = [
            ("Arjun", "10,64,000"), ("Sivaparvathi", "15,40,000"), ("Bramarambha", "13,20,760"), ("Mallikarjuna", "13,20,760"), ("Total (KPHB)", "52,45,520")
        ]
        st.markdown("<h4 style='color:#FFD700;'>KPHB (All Fulls) Break-up</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(ad_kphb, ["Theatre", "Collection"]), unsafe_allow_html=True)

        # 1Cr Gross Centers
        st.markdown("<h4 style='color:#FFD700;'>1Cr Gross Centers</h4>", unsafe_allow_html=True)
        ad_1cr_centers = [
            "RTC X-ROADS", "KUKATPALLY", "Kompally", "DSNR", "PRASAD'S IMAX", "BHIMAVARAM", "KURNOOL", "KAKINADA", "GUNTUR", "TIRUPATI", "Khammam", "VIZAG", "NELLORE", "KARIMNAGAR", "WARANGAL", "RAJHAMUNDRY", "ONGOLE", "VIJAYAWADA"
        ]
        st.markdown("<ul style='color:#FFD700; font-size:1.1em;'>" + ''.join([f"<li>{center}</li>" for center in ad_1cr_centers]) + "</ul>", unsafe_allow_html=True)

        # All Time Record Shares
        st.markdown("<h4 style='color:#FFD700;'>All Time Record Shares</h4>", unsafe_allow_html=True)
        ad_atr_shares = [
            "Hyderabad", "Vijayawada", "Guntur", "Kurnool", "Warangal", "Karimnagar", "Mahaboob Nagar", "Vizag", "Tirupati", "Nellore", "Ongole", "Chittor", "Medchal", "Nizamabad", "Vizianagaram", "Nandayala", "DSNR", "Guntakal", "Yelamanchili", "Allagadda", "Tagarapuvulasa", "Khammam", "Nirmal", "Kaavali", "Peddapuram"
        ]
        st.markdown("<ul style='color:#FFD700; font-size:1.1em;'>" + ''.join([f"<li>{center}</li>" for center in ad_atr_shares]) + "</ul>", unsafe_allow_html=True)

        # ATR Closing Few Centers
        st.markdown("<h4 style='color:#FFD700;'>ATR Closing Few Centers</h4>", unsafe_allow_html=True)
        ad_atr_few = [
            ("Khammam", "1.07Cr"), ("Guntakal", "26L"), ("Vijayawada", "1.80Cr"), ("Peddapuram", "12.24L (Sh)"), ("Kurnool", "77.58L"), ("Nellore", "86L"), ("Nandyal", "45.66L"), ("Guntur", "1.09Cr"), ("Tirupati", "93.30L (Sh)"), ("Nizamabad", "92L"), ("Hyd Cineplanet", "86.7L"), ("Vijayanagaram", "87.78L")
        ]
        st.markdown(generate_centerwise_table(ad_atr_few, ["Center", "Closing Share/Gross"]), unsafe_allow_html=True)

        # Top 3 Weekend Openers in India [2013]
        st.markdown("<h4 style='color:#FFD700;'>Top 3 Weekend Openers in India [2013]</h4>", unsafe_allow_html=True)
        ad_top3 = [
            ("Chennai Express", "$2.22M"), ("YJHD", "$1.56M"), ("AD", "$1.52M [$1.74M Incl Non Rentrak]")
        ]
        st.markdown(generate_centerwise_table(ad_top3, ["Movie", "Gross"]), unsafe_allow_html=True)

        # Closing gross/records as points
        st.markdown("<h4 style='color:#FFD700;'>Closing Gross/Records</h4>", unsafe_allow_html=True)
        st.markdown("""
        <ul style='color:#FFD700; font-size:1.1em;'>
            <li>AD Nizam closing gross <b>#39.50cr gross</b> &amp; Nett <b>#35cr</b> &amp; Share <b>#23.60cr</b></li>
            <li>AD Hyd City closing gross <b>21.60cr</b> &amp; Nett <b>18.60cr</b> &amp; Share around <b>11.25cr</b></li>
        </ul>
        """, unsafe_allow_html=True)

        # Ceeded Districts Closing Table
        st.markdown("<h4 style='color:#FFD700;'>Ceeded Districts Closing</h4>", unsafe_allow_html=True)
        ad_ceeded = [
            ("Kurnool", "3,86,48,880", "3,70,63,422", "2,74,58,753"),
            ("Anantapur", "3,00,43,220", "2,89,93,450", "2,20,38,653"),
            ("Bellary", "1,24,11,612", "1,13,74,314", "58,52,528"),
            ("Kadapa", "2,65,23,246", "2,64,38,502", "2,05,36,297"),
            ("Chittor", "3,98,45,045", "3,73,31,827", "2,87,62,560"),
            ("Total Ceeded", "14,74,72,003", "14,12,01,515", "10,46,48,791")
        ]
        st.markdown(generate_centerwise_table(ad_ceeded, ["District", "Gross", "Nett", "Share"]), unsafe_allow_html=True)

        # Nizam Closing Records Table
        st.markdown("<h4 style='color:#FFD700;'>Nizam Closing Records</h4>", unsafe_allow_html=True)
        ad_nizam = [
            ("Karimnagar", "1.11c", "63L"),
            ("Warangal", "1.85c", "98.1L"),
            ("Khammam", "1.06c", "72L"),
            ("Mahaboob Nagar", "56L", "38L")
        ]
        st.markdown(generate_centerwise_table(ad_nizam, ["City", "Gross", "Share"]), unsafe_allow_html=True)

        # KA Closing Break Up Table
        st.markdown("<h4 style='color:#FFD700;'>KA Closing Break Up</h4>", unsafe_allow_html=True)
        ad_ka_closing = [
            ("Bangalore", "3,587,347"),
            ("Kolar", "7,152,246"),
            ("Tumkur", "1,600,000"),
            ("Mysore", "2,018,641"),
            ("Mandya", "500,000"),
            ("Coorg", "75,000"),
            ("Hassan", "1,027,534"),
            ("Hosur", "1,120,000"),
            ("Bombay KA", "3,450,000"),
            ("C'durga-D'gere", "2,100,000"),
            ("Shimoga-M'lore", "650,000"),
            ("Hyderabad KA", "500,000"),
            ("Total KA", "56,067,268")
        ]
        st.markdown(generate_centerwise_table(ad_ka_closing, ["Area", "Final Share (in Rs.)"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "Gabbar Singh (Re-Release)":
        st.markdown("<h2 style='color:#FFD700;'>Gabbar Singh Re-Release - Center Wise Data</h2>", unsafe_allow_html=True)

        # West Godavari
        gs_west_godavari = [
            ("Eluru", "8.76L"), ("Tanuku", "4.97L"), ("BVRM", "4.84L"), ("Tpgudem", "2.12L"), ("Attili", "1.58L"), ("JGudem", "2.46L"), ("Kovvur", "3.02L"), ("NSP", "1.39L"), ("Ganapavaram", "1.21L"), ("Ndvole", "62K"), ("Akkiveedu", "1.03L"), ("Palakollu", "2.09L"), ("Nallajerla", "94K"), ("Chintalapudi", "37K"), ("Dvp", "27K")
        ]
        st.markdown("<h4 style='color:#FFD700;'>West Godavari (Day 1)</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_west_godavari, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # Guntur
        gs_guntur = [
            ("Narasaraopet", "2.03L"), ("Ponnur", "1.06L"), ("Repalle", "1.21L"), ("Addanki", "86K"), ("Macherla", "80K"), ("Piduguralla", "67K"), ("Guntur", "21.25L"), ("Ongole", "6.32L"), ("Vetapalem", "29K"), ("Tenali", "3.46L"), ("Sattenapalli", "1.70L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Guntur (Day 1)</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_guntur, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # Ceeded
        gs_ceeded = [
            ("Kadapa", "5.3L"), ("Adoni", "1.27L"), ("Atp", "3.54L"), ("Nandyal", "2.8L"), ("Mdp", "5.18L"), ("Pdtr", "1.6L"), ("Guntakal", "78K"), ("Kadiri", "52K"), ("Knl", "6.75L"), ("Tpt", "16.11L"), ("Penukonda", "44K"), ("Uravakonda", "18K"), ("Dharmavaram", "85K"), ("Pamidi", "18K"), ("Gooty", "29K"), ("KothaCheruvu", "25K"), ("Gorantla", "30K"), ("Tadipatri", "1L+"), ("Chittor", "4L"), ("Srikalahasti", "2L"), ("Porumamilla", "73,700"), ("Jammalamadugu", "55,500"), ("Bellary", "2.14L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Ceeded (Day 1)</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_ceeded, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # UA
        gs_ua = [
            ("Vizag city", "12,12,862"), ("Gajuwaka", "6,71,966"), ("Anakapalle", "2,14,440"), ("Srikakulam", "2,73,590"), ("Vizianagaram", "7,49,095"), ("Bobbili", "1,20,676")
        ]
        st.markdown("<h4 style='color:#FFD700;'>UA (Day 1)</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_ua, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # National Multiplexes 5 Days Nett
        gs_national_multiplexes = [
            ("Hyderabad", "11,25,477"), ("Vijayawada", "18,93,786"), ("Vizag", "10,89,290"), ("Vizianagaram", "1,45,322"), ("Bangalore", "2,81,146"), ("Chennai", "2,41,823"), ("Kakinada", "4,06,331"), ("Karimnagar", "57,577"), ("Warangal", "5,394"), ("Armoor", "8,912"), ("Nizamabad", "3,920"), ("Machilipatnam", "1,14,647"), ("Guntur", "1,79,925"), ("Kochi", "8,724"), ("Thiruvananthapuram", "3,829"), ("Coimbatore", "11,550"), ("Manipal", "35,969"), ("Mysore", "16,530"), ("Vellore", "15,921"), ("Aurangabad", "1,369"), ("Jaipur", "27,920"), ("Bhopal", "29,693"), ("Gwalior", "35,304"), ("Indore", "3,226"), ("Chandrapur", "2,025"), ("Bhilai", "5,516"), ("Raipur", "5,679"), ("Nagpur", "18,643"), ("Cuttack", "2,176"), ("Guwahati", "4,439"), ("Rourkela", "4,823"), ("Bhubaneswar", "42,378"), ("Ranchi", "3,911"), ("Dhanbad", "56,679"), ("Patna", "2,313"), ("Kolkata", "53,533"), ("Jalandhar", "7,711"), ("Mohali", "51,338"), ("Gurgaon", "26,683"), ("Dehradun", "11,059"), ("Lucknow", "8,736"), ("Ghaziabad", "4,241"), ("Noida", "13,379"), ("Delhi", "92,066"), ("Raichur", "78,648"), ("Dharwad", "8,115"), ("Goa", "1,956"), ("Nasik", "160"), ("Pune", "89,228"), ("Jamnagar", "6,068"), ("Baroda", "92,154"), ("Surat", "11,651"), ("Ahmedabad", "13,045"), ("Thane", "57,238"), ("Mumbai", "62,559")
        ]
        st.markdown("<h4 style='color:#FFD700;'>National Multiplexes 5 Days Nett</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(gs_national_multiplexes, ["Center", "5 Days Nett"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "CameraMan Gangatho Rambabu":
        st.markdown("<h2 style='color:#FFD700;'>CameraMan Gangatho Rambabu - First Week Centerwise Gross</h2>", unsafe_allow_html=True)
        cmgr_first_week = [
            ("Kakinada", "45,37,277/-"), ("Rajahmundry", "41,50,393/-"), ("Amalapuram", "8,88,618/-"), ("Pithapuram", "7,77,576/-"), ("Thatipaka", "6,43,969/-"), ("Peddapuram", "6,05,141/-"), ("Mandapeta", "5,82,545/-"), ("Malkipuram", "4,52,308/-"), ("RamaChandraPuram", "4,48,383/-"), ("Jaggampeta", "4,29,867/-"), ("Tuni", "3,95,518/-"), ("DrakshaRamam", "3,56,616/-"), ("Kothapeta", "3,44,829/-"), ("Samarlakota", "3,43,363/-"), ("Kadiam", "2,48,636/-"), ("Yeleswaram", "2,41,927/-"), ("Anaparthi", "1,32,718/-"), ("G.Mamidada", "1,01,210/-"), ("Namavaram", "96,280/-"), ("Gokavaram", "89,654/-")
        ]
        st.markdown(generate_centerwise_table(cmgr_first_week, ["Center", "First Week Gross"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "Kushi (Re-Release)":
        st.markdown("<h2 style='color:#FFD700;'>Kushi Re-Release - Center Wise Data</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>Gross</b> = Gross Collection, <b>Net</b> = Net Collection</div>", unsafe_allow_html=True)

        # Day 1 Gross - Nizam
        kushi_nizam = [
            ("Prasad's Multiplex", "12L"), ("Gpr Multiplex", "8.3L"), ("Laxmikala cinepride", "9.15L"), ("Amb cinemas", "4.60L"), ("KPHB", "12L"), ("X roads", "11,94,460"), ("INOX", "3,48,365"), ("CINEPOLIS", "2,34,410"), ("PVR", "11,25,835"), ("MIRAJ", "4,60,900"), ("Nizamabad", "2.12L"), ("Warangal", "5.97L"), ("Karimnagar", "2.89L"), ("Khammam", "2.07L"), ("Mahbubnagar", "2.66L"), ("Nalgonda", "1.13L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Nizam - Day 1 Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(kushi_nizam, ["Center", "Day 1 Gross"]), unsafe_allow_html=True)

        # Day 1 Gross - Ceeded
        kushi_ceeded = [
            ("KURNOOL", "6.38L"), ("ANANTHAPUR", "5.48L"), ("Proddatur", "1.32L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Ceeded - Day 1 Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(kushi_ceeded, ["Center", "Day 1 Gross"]), unsafe_allow_html=True)

        # Day 1 Gross - Guntur
        kushi_guntur = [
            ("Guntur City", "710K"),
            ("Ongole", "384K"),
            ("Tenali", "255K"),
            ("Npeta", "45K"),
            ("ChPeta", "82K"),
            ("Vinukonda", "42K"),
            ("Piduguralla", "28K"),
            ("Satenpalli", "102K"),
            ("Macherla", "70K"),
            ("Repalle", "76K"),
            ("Bapatla", "106K"),
            ("Mangalagiri", "92K"),
            ("Addanki", "32K"),
            ("Chimakurty", "38K"),
            ("Chebrolu", "120K")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Guntur - Day 1 Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(kushi_guntur, ["Center", "Day 1 Gross"]), unsafe_allow_html=True)

        # Day 1 Gross - UA
        kushi_ua = [
            ("Vizag City", "9.5L"), ("Vizianagaram", "3.17L"), ("Srikakulam", "1.85L"), ("Gajuwaka", "1.24L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>UA - Day 1 Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(kushi_ua, ["Center", "Day 1 Gross"]), unsafe_allow_html=True)

        # Day 1 Gross - West
        kushi_west = [
            ("Tadepalligudem", "57K")
        ]
        st.markdown("<h4 style='color:#FFD700;'>West - Day 1 Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(kushi_west, ["Center", "Day 1 Gross"]), unsafe_allow_html=True)

        # Nizam National Plex (6 days)
        st.markdown("<h4 style='color:#FFD700;'>Nizam National Plex (6 days)</h4>", unsafe_allow_html=True)
        st.markdown("<ul style='color:#FFD700; font-size:1.1em;'>"
            "<li><b>Total Gross:</b> 61.14L</li>"
            "<li><b>Total Net:</b> 51.81L</li>"
            "<li><b>Closing Net:</b> 54L</li>"
            "</ul>", unsafe_allow_html=True)
        kushi_national_plex = [
            ("Inox", "5.73L net"), ("Cinepolis", "4.35L net"), ("PVR", "26.91L net"), ("Miraj", "6.6L net"), ("Platinum", "8.15L net")
        ]
        st.markdown(generate_centerwise_table(kushi_national_plex, ["Theatre", "Net Collection"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "Annavaram":
        st.markdown("<h2 style='color:#FFD700;'>Annavaram - Center Wise Data</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>ATR</b> = All Time Record, <b>Sh</b> = Share</div>", unsafe_allow_html=True)

        # Day 1 Collections
        annavaram_day1 = [
            ("Eluru Town", "6L (sh)"),
            ("Ananthapur", "7L"),
            ("TPT", "11L (ATR)"),
            ("KURNOOL", "6.1L"),
            ("KADAPA", "6.18L"),
            ("Kandukur town", "1.65L sh (ATR)")
        ]
        st.markdown("<h4 style='color:#FFD700;'>Day 1 Collections</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(annavaram_day1, ["Center", "Day 1 Collection"]), unsafe_allow_html=True)

        # First Week Collections
        annavaram_first_week = [
            ("Vizianagaram", "5L (sh)"), ("Bobbili", "2.85L (sh)"), ("Parvathipuram", "2.47L (sh)"), ("Rajam", "2.80L (sh)"), ("Gajuwaka", "6.1L (sh)"), ("Chikalurpeta", "5.91L (ATR)"), ("Piduguralla", "4.6L (ATR)"), ("Addanki", "2.97L"), ("Chirala", "5.33L"), ("Guntur", "18.58L"), ("Magalagiri", "3.98L"), ("Macherla", "3.22L"), ("NarasaraoPeta", "7.29L"), ("Ongole", "6.13L"), ("Piduguralla", "4.60L"), ("Ponnuru", "4.60L"), ("Repalle", "4.74L"), ("Sattenapalli", "4.19L"), ("Tanguturu", "2.50L"), ("Tenali", "7.29L"), ("Vinukonda", "3.32L"), ("PTP", "5.13L"), ("PEDDAPURAM", "4.77L"), ("JAGGAMPET", "3.56L"), ("RAMACHANDRAPURAM", "4.19L"), ("TATIPAKA", "2.95L"), ("MALKIPURAM", "2.91L"), ("KOTHAPET", "1.84L"), ("RAVULAPALEM", "2.69L"), ("ANAPARTHI", "2.52L"), ("KADIYAM", "1.96L"), ("TUNI", "2.15L"), ("YANAM", "2.55L"), ("MANDAPET", "3.24L"), ("RJY", "12.5L"), ("AMP", "5.88L"), ("KKD", "15.03L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>First Week Collections</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(annavaram_first_week, ["Center", "First Week Collection"]), unsafe_allow_html=True)

        # 27 Days Gross
        annavaram_27days_gross = [
            ("RJY", "1824496"), ("KKD", "1565538"), ("AMP", "879236"), ("MANDAPETA", "882365"), ("PTP", "1282133"), ("PEDDAPURAM", "1084176"), ("JAGGAMPET", "867598"), ("RAMACHANDRAPURAM", "850500"), ("TATIPAKA", "556864"), ("MALKIPURAM", "493168"), ("KOTHAPET", "365573"), ("RAVULAPALEM", "512526"), ("ANAPARTHI", "558756"), ("ELESWARAM", "823683"), ("KADIYAM", "376004")
        ]
        st.markdown("<h4 style='color:#FFD700;'>27 Days Gross</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(annavaram_27days_gross, ["Center", "Gross (Rs.)"]), unsafe_allow_html=True)

        # 55 Days Shares (Approx)
        annavaram_55days_shares = [
            ("GUNTUR", "14.64L"), ("TENALI", "10.42L"), ("ONGOLE", "13.38L"), ("CHEERALA", "10.48L"), ("NSPTA", "13.3L"), ("REPALLE", "8.40L"), ("PIDUGURALLA", "8.66L"), ("VINUKONDA", "6.04L"), ("CHILAKALOORPET", "10.77L"), ("PONNURU", "8.66L"), ("SATTENAPALLY", "7.88L"), ("MANGALAGIRI", "6.46L"), ("MACHARLA", "5.02L"), ("TADEPALLY", "2.50L"), ("ADDANKI", "4.44L"), ("GUNTUR", "18.9L"), ("TENALI", "3.45L")
        ]
        st.markdown("<h4 style='color:#FFD700;'>55 Days Shares (Approx)</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table(annavaram_55days_shares, ["Center", "Share (Rs.)"]), unsafe_allow_html=True)

    elif selected_centerwise_movie == "Badri":
        st.markdown("<h2 style='color:#FFD700;'>Badri - Center Wise Data</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:1em; margin-bottom:10px;'>Legend: <b>Gross</b> = Gross Collection, <b>Share</b> = Share Collection, <b>HF</b> = House Full</div>", unsafe_allow_html=True)

        # Hyderabad - Sandhya 35MM
        st.markdown("<h4 style='color:#FFD700;'>Hyderabad : Sandhya 35MM</h4>", unsafe_allow_html=True)
        badri_hyd = [
            ("100 Days Gross", "73L"),
            ("100 Days Share", "44L"),
            ("156 Days Gross", "90L"),
            ("156 Days Share", "47L")
        ]
        st.markdown(generate_centerwise_table(badri_hyd, ["Period", "Amount"]), unsafe_allow_html=True)

        # Vijayawada - Raj 70MM
        st.markdown("<h4 style='color:#FFD700;'>Vijayawada : Raj 70MM</h4>", unsafe_allow_html=True)
        badri_vij = [
            ("100 Days Gross", "53L"),
            ("100 Days Share", "30L")
        ]
        st.markdown(generate_centerwise_table(badri_vij, ["Period", "Amount"]), unsafe_allow_html=True)

        # Vijayawada City Record
        st.markdown("<h4 style='color:#FFD700;'>Vijayawada City Record</h4>", unsafe_allow_html=True)
        badri_vij_city = [
            ("Full Run (141 Days) Gross", "62,56,007/-"),
            ("Record", "Theatre Record")
        ]
        st.markdown(generate_centerwise_table(badri_vij_city, ["Period/Note", "Amount"]), unsafe_allow_html=True)

        # Vizag - Jagadamba 70MM
        st.markdown("<h4 style='color:#FFD700;'>Vizag : Jagadamba 70MM</h4>", unsafe_allow_html=True)
        badri_vizag = [
            ("100 Days Gross", "62,55,382"),
            ("100 Days Share", "31.50L"),
            ("54 Days", "Non Stop all 4 shows HF everyday"),
            ("Full Run (113 Days Non)", "Gross - 65.80L"),
            ("Record", "Vizag city record for 70MM theatres")
        ]
        st.markdown(generate_centerwise_table(badri_vizag, ["Period/Note", "Amount"]), unsafe_allow_html=True)

        # Kakinada - Sri Devi Theatre
        st.markdown("<h4 style='color:#FFD700;'>Kakinada : Sri Devi Theatre</h4>", unsafe_allow_html=True)
        badri_kkd = [
            ("100 Days Gross", "28L"),
            ("100 Days Share", "17.60L"),
            ("Record", "Theatre Record")
        ]
        st.markdown(generate_centerwise_table(badri_kkd, ["Period/Note", "Amount"]), unsafe_allow_html=True)

        # Rajahmundry - Ashoka Theatre
        st.markdown("<h4 style='color:#FFD700;'>Rajahmundry : Ashoka Theatre</h4>", unsafe_allow_html=True)
        badri_rjy = [
            ("100 Days Gross", "31L"),
            ("100 Days Share", "18.20L"),
            ("Record", "Theatre Record")
        ]
        st.markdown(generate_centerwise_table(badri_rjy, ["Period/Note", "Amount"]), unsafe_allow_html=True)

        # Guntur - Liberty Theatres
        st.markdown("<h4 style='color:#FFD700;'>Guntur : Liberty Theatres</h4>", unsafe_allow_html=True)
        badri_guntur = [
            ("Full Run (119 Days) Gross", "27,91,214/-")
        ]
        st.markdown(generate_centerwise_table(badri_guntur, ["Period", "Amount"]), unsafe_allow_html=True)

        # RJY - Ashoka Theatre (120 days)
        st.markdown("<h4 style='color:#FFD700;'>Rajahmundry : Ashoka Theatre (120 Days)</h4>", unsafe_allow_html=True)
        badri_rjy_120 = [
            ("120 Days Gross", "33,77,065/-")
        ]
        st.markdown(generate_centerwise_table(badri_rjy_120, ["Period", "Amount"]), unsafe_allow_html=True)

        # Records Section
        st.markdown("<h3 style='color:#FFD700;'>Records</h3>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#FFD700;'>100 Days Direct Centers</h4>", unsafe_allow_html=True)
        st.markdown(generate_centerwise_table([
            ("Nizam", "8"),
            ("Ceeded", "2"),
            ("UA", "8"),
            ("Guntur", "5"),
            ("East Godavari", "6"),
            ("Krishna", "4"),
            ("West Godavari", "5"),
            ("Nellore", "1"),
            ("Total", "39 Centers")
        ], ["Area", "No. of Centers"]), unsafe_allow_html=True)

        st.markdown("<div style='color:#FFD700; font-size:1.1em; margin-bottom:10px;'>East Godavari Dist Only 8 Centers 100 Days Share: <b>78L+</b> Blockbuster Run</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 40px; color: #E0E0E0;'>
        <p>Powered by Streamlit | Data Source: PSPK BO Records Since 2006</p>
    </div>
""", unsafe_allow_html=True)
