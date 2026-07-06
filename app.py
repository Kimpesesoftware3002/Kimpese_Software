#  PROPRIETARY NOTICE & COPYRIGHT LICENSE
#  Copyright © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved.
#  State of Registration: Wyoming, USA.
# ==============================================================================
import streamlit as st
import sqlite3
import os
from datetime import datetime

DB_NAME = "database.db"

# Configuration de la page
st.set_page_config(page_title="Kimpese Software | Global Pricing Intelligence", page_icon="🟢", layout="wide")

# --- DESIGN SILICON VALLEY NOIR ET VERT ---
st.markdown("""
<style>
    .stApp {
        background-color: #0A0E17 !important;
        color: #F3F4F6 !important;
    }
    .logo-container {
        text-align: center;
        padding: 20px 0;
    }
    .brand-title {
        font-size: 42px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #FFFFFF !important;
        margin-top: 15px;
        margin-bottom: 0px;
    }
    .brand-subtitle {
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #9CA3AF !important;
        margin-top: 5px;
    }
    .sv-card {
        background: rgba(17, 24, 39, 0.8);
        border: 1px solid rgba(46, 204, 113, 0.2);
        border-radius: 16px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }
    .sv-card:hover {
        border-color: #2ECC71;
        box-shadow: 0 0 25px rgba(46, 204, 113, 0.3);
        transform: translateY(-5px);
    }
    .sv-badge {
        background: linear-gradient(90deg, #2ECC71, #27AE60);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    label, p, h3 { color: #E5E7EB !important; }
    div[data-baseweb="input"] { background-color: #1F2937 !important; border: 1px solid #374151 !important; }
    div[data-baseweb="input"] input { color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- AFFICHAGE DU LOGO ---
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
if os.path.exists("logo.png"):
    st.image("logo.png", width=200)
else:
    st.markdown('<div class="brand-title">KIMPESE</div><div class="brand-subtitle">SOFTWARE</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#9CA3AF; font-size:16px; margin-top:-10px; margin-bottom:30px;">Next-Gen Pricing Intelligence for Global Brands</p>', unsafe_allow_html=True)

# Détection pays via URL
query_params = st.query_params
client_country = query_params["country"].upper() if "country" in query_params else "US"

# 📊 MATRICE CORRIGÉE AVEC VOS TARIFS PREMIUM US
MATRICE_TARIFS = {
    "US": {"devise": "$", "starter": "99", "pro": "249", "enterprise": "499"},
    "UK": {"devise": "£", "starter": "79", "pro": "199", "enterprise": "399"},
    "CA": {"devise": "CA$", "starter": "139", "pro": "349", "enterprise": "699"},
    "AU": {"devise": "AU$", "starter": "149", "pro": "379", "enterprise": "749"}
}

if client_country not in MATRICE_TARIFS:
    client_country = "US"

config = MATRICE_TARIFS[client_country]
devise = config["devise"]

if "step" not in st.session_state:
    st.session_state.step = "saisie"

st.write("---")

# --- INTERFACE ---
if st.session_state.step == "saisie":
    st.markdown(f"### 🌐 Market Analysis Engine • Country: {client_country}")
    categorie = st.radio("Select your industry vertical :", ["Pet Care / Animalier 🐶", "Pharmacy / Parapharmacie 💊"], horizontal=True)
    nom_entreprise = st.text_input("Enter your brand name to map competitor pricing gaps overnight :", placeholder="e.g. Acme Corporation")
    
    if st.button("Analyze My Market Now", type="primary"):
        if nom_entreprise.strip():
            st.session_state.nom_marque = nom_entreprise.strip()
            st.session_state.vertical = "Animalier" if "Animalier" in categorie else "Parapharmacie"
            try:
                conn = sqlite3.connect(DB_NAME)
                cur = conn.cursor()
                cur.execute("INSERT INTO clients_saas (nom_marque, email_client, date_inscription, statut) VALUES (?, ?, ?, 'ESSAI')", 
                            (st.session_state.nom_marque, f"contact@{st.session_state.nom_marque.lower().replace(' ', '')}.com", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
                conn.close()
            except: pass
            st.session_state.step = "verrouille"
            st.rerun()

elif st.session_state.step == "verrouille":
    st.markdown(f"### 🧬 Scanner Status: <span style='color:#2ECC71;'>Active Tracking Enabled for {st.session_state.nom_marque} ({st.session_state.vertical})</span>", unsafe_allow_html=True)
    st.write(f"Our tracking bot is currently mapping your retail competitors in the {st.session_state.vertical} sector. Choose a plan to unlock your intelligence dashboard.")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="sv-card">
            <div style="font-size: 20px; font-weight:700; color:#FFFFFF;">🌱 Starter</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{devise}{config['starter']}<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Track 50 active products<br>Daily price updates<br>Single country analytics</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Starter Trial", key="btn_str", use_container_width=True)
        
    with col2:
        st.markdown(f"""
        <div class="sv-card" style="border-color: #2ECC71;">
            <div class="sv-badge">MOST POPULAR</div>
            <div style="font-size: 20px; font-weight:700; color:#2ECC71;">⚡ Pro Tracker</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{devise}{config['pro']}<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Track 500 active products<br>Instant stock & price alerts<br>Multi-country tracking</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Pro Trial", key="btn_pro", use_container_width=True)
        
    with col3:
        st.markdown(f"""
        <div class="sv-card">
            <div style="font-size: 20px; font-weight:700; color:#FFFFFF;">👑 Enterprise</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{devise}{config['enterprise']}<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Unlimited products & stores<br>Custom API access<br>Dedicated Account Manager</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Contact Sales", key="btn_ent", use_container_width=True)

st.write("---")
st.markdown("<p style='color:#4B5563; font-size:12px; text-align:center;'>© 2026 KIMPESE SOFTWARE L.L.C. All rights reserved. Secured under Wyoming LLC Proprietary Laws.</p>", unsafe_allow_html=True)
