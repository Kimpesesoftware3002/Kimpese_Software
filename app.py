#  PROPRIETARY NOTICE & COPYRIGHT LICENSE
#  Copyright © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved.
#  State of Registration: Wyoming, USA.
# ==============================================================================
import streamlit as st
import os
from datetime import datetime

# Configuration globale de la page
st.set_page_config(page_title="Kimpese Software | Global Pricing Intelligence", page_icon="🟢", layout="wide")

# --- DESIGN SILICON VALLEY NOIR ET VERT ---
st.markdown("""
<style>
    /* Fond noir profond universel */
    .stApp {
        background-color: #0A0E17 !important;
        color: #F3F4F6 !important;
    }
    
    /* Cartes de tarifs Silicon Valley */
    .sv-card {
        background: #111827 !important;
        border: 1px solid rgba(46, 204, 113, 0.2);
        border-radius: 16px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        transition: all 0.3s ease;
        margin-bottom: 5px;
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
    
    label, p, h3, span { color: #E5E7EB !important; }
    
    /* Zones de saisie noires */
    div[data-baseweb="input"], div[data-baseweb="base-input"], .stTextInput>div {
        background-color: #111827 !important;  
        border: 1px solid #374151 !important;  
        border-radius: 8px !important;
    }
    div[data-baseweb="input"] input, .stTextInput input {
        color: #FFFFFF !important;
        background-color: #111827 !important;
    }
    
    /* Éradication absolue de tous les blocs et lignes blanches résiduelles de Streamlit */
    div[data-testid="stVerticalBlock"] > div {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    .element-container, .stMarkdown, div[data-testid="stBlock"] {
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- COMPOSANT METEO HAUTE FIABILITE (IP-API + OPEN-METEO) ---
html_meteo_client = """
<div style="position: absolute; top: -50px; right: 10px; z-index: 9999;">
    <div id="weather-display" style="background: rgba(17, 24, 39, 0.9); border: 1px solid rgba(46, 204, 113, 0.2); padding: 10px 18px; border-radius: 12px; text-align: right; min-width: 160px; font-family: monospace;">
        <div style="font-size: 16px; font-weight: 700; color: #2ECC71;" id="wf-temp">☀️ 84°F</div>
        <div style="font-size: 11px; color: #9CA3AF; text-transform: uppercase;" id="wf-loc">MYRTLE BEACH, SC</div>
    </div>
</div>

<script>
    // 1. Détection des coordonnées géographiques du visiteur (Latitude / Longitude) via son IP
    fetch('https://ipapi.co')
        .then(response => response.json())
        .then(geo => {
            const city = geo.city || "Myrtle Beach";
            const region = geo.region_code || "SC";
            const lat = geo.latitude;
            const lon = geo.longitude;
            
            if(lat && lon) {
                // 2. Appel à Open-Meteo pour obtenir la vraie température en Fahrenheit de cette position
                fetch(`https://open-meteo.com{lat}&longitude=${lon}&current_weather=true&temperature_unit=fahrenheit`)
                    .then(res => res.json())
                    .then(weather => {
                        const tempF = Math.round(weather.current_weather.temperature);
                        document.getElementById('wf-temp').innerText = "☀️ " + tempF + "°F";
                        document.getElementById('wf-loc').innerText = city.toUpperCase() + ", " + region.toUpperCase();
                    });
            }
        })
        .catch(err => {
            // Sécurité par défaut (Fallback)
            document.getElementById('wf-temp').innerText = "☀️ 84°F";
            document.getElementById('wf-loc').innerText = "MYRTLE BEACH, SC";
        });
</script>
"""
st.markdown(html_meteo_client, unsafe_allow_html=True)

# --- EN-TÊTE DE PAGE : LOGO CENTRÉ ---
st.write("")
if os.path.exists("logo.png"):
    col_l1, col_l2, col_l3, col_l4, col_l5 = st.columns([1.5, 1, 1.2, 1, 1.5])
    with col_l3:
        st.image("logo.png", use_container_width=True)
else:
    st.markdown('<div style="text-align:center; padding:20px 0;"><h1 style="color:white; margin:0;">KIMPESE SOFTWARE</h1></div>', unsafe_allow_html=True)

st.markdown('<p style="text-align:center; color:#9CA3AF; font-size:16px; margin-top:15px; margin-bottom:30px;">Next-Gen Pricing Intelligence for Global Brands</p>', unsafe_allow_html=True)

# Détection pays via URL
query_params = st.query_params
client_country = query_params["country"].upper() if "country" in query_params else "US"

# Tarifs Premium ($99 / $249 / $499)
MATRICE_TARIFS = {
    "US": {"devise": "$", "starter": "99", "pro": "249", "enterprise": "499"},
    "UK": {"devise": "£", "starter": "79", "pro": "199", "enterprise": "399"},
    "CA": {"devise": "CA$", "starter": "139", "pro": "349", "enterprise": "699"},
    "AU": {"devise": "AU$", "starter": "149", "pro": "379", "enterprise": "749"}
}

if client_country not in MATRIFS_TARIFS:
    client_country = "US"

config = MATRICE_TARIFS[client_country]
devise = config["devise"]

if "step" not in st.session_state: st.session_state.step = "saisie"
if "choix_plan" not in st.session_state: st.session_state.choix_plan = None
if "liste_emails" not in st.session_state: st.session_state.liste_emails = []

st.write("---")

# --- CORE ENGINE INTERFACE ---
if st.session_state.step == "saisie":
    st.markdown(f"### 🌐 Market Analysis Engine • Country: {client_country}")
    categorie = st.radio("Select your industry vertical :", ["Pet Care / Animalier 🐶", "Pharmacy / Parapharmacie 💊"], horizontal=True)
    nom_entreprise = st.text_input("Enter your brand name to map competitor pricing gaps overnight :", placeholder="e.g. Acme Corporation")
    
    if st.button("Analyze My Market Now", type="primary"):
        if nom_entreprise.strip():
            st.session_state.nom_marque = nom_entreprise.strip()
            st.session_state.vertical = "Animalier" if "Animalier" in categorie else "Parapharmacie"
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
        if st.button("Launch Starter Trial", key="btn_str", use_container_width=True):
            st.session_state.choix_plan = "Starter"
        
    with col2:
        st.markdown(f"""
        <div class="sv-card" style="border-color: #2ECC71;">
            <div class="sv-badge">MOST POPULAR</div>
            <div style="font-size: 20px; font-weight:700; color:#2ECC71;">⚡ Pro Tracker</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{devise}{config['pro']}<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Track 500 active products<br>Instant stock & price alerts<br>Multi-country tracking</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Pro Trial", key="btn_pro", use_container_width=True):
            st.session_state.choix_plan = "Pro"
        
    with col3:
        st.markdown(f"""
        <div class="sv-card">
            <div style="font-size: 20px; font-weight:700; color:#FFFFFF;">👑 Enterprise</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{devise}{config['enterprise']}<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Unlimited products & stores<br>Custom API access<br>Dedicated Account Manager</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Contact Sales", key="btn_ent", use_container_width=True):
            st.session_state.choix_plan = "Enterprise"

    # --- ZONE FORMULAIRE BETA ---
    if st.session_state.choix_plan:
        st.write("---")
        st.info(f"🚀 **Kimpese Software is currently in Private Beta for the {st.session_state.choix_plan} Plan.**")
        email_beta = st.text_input("Enter your business email to request priority access credentials :", placeholder="ceo@yourbrand.com")
        if st.button("Submit Request", type="primary"):
            if email_beta.strip():
                nouvelle_entree = {
