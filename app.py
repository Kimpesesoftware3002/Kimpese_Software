import streamlit as st
import re
import os
import pandas as pd
from datetime import datetime

# Configuration de la page Streamlit
st.set_page_config(page_title="Kimpese Software", page_icon="💻", layout="centered")

# Nom du fichier de stockage permanent
FICHIER_CSV = "prospects.csv"

# Fonction pour initialiser le fichier CSV avec des en-têtes s'il n'existe pas
def initialiser_csv():
    if not os.path.exists(FICHIER_CSV):
        df_initial = pd.DataFrame(columns=["Date d'inscription", "Emails Collectés"])
        df_initial.to_csv(FICHIER_CSV, index=False, encoding="utf-8")

# Fonction pour ajouter un e-mail dans le fichier CSV
def enregistrer_email_csv(email):
    initialiser_csv()
    date_actuelle = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nouvelle_ligne = pd.DataFrame([[date_actuelle, email]], columns=["Date d'inscription", "Emails Collectés"])
    nouvelle_ligne.to_csv(FICHIER_CSV, mode='a', header=False, index=False, encoding="utf-8")

# Fonction pour lire les e-mails enregistrés
def lire_emails_csv():
    initialiser_csv()
    try:
        return pd.read_csv(FICHIER_CSV, encoding="utf-8")
    except Exception:
        return pd.DataFrame(columns=["Date d'inscription", "Emails Collectés"])

# Fonction pour supprimer un e-mail spécifique du fichier CSV
def supprimer_email_csv(email_a_supprimer):
    df = lire_emails_csv()
    # On garde toutes les lignes SAUF celle contenant l'e-mail à supprimer
    df_filtre = df[df["Emails Collectés"] != email_a_supprimer]
    df_filtre.to_csv(FICHIER_CSV, index=False, encoding="utf-8")

# =====================================================================
# SECTION 1 : LOGO & TITRE CENTRÉ
# =====================================================================
st.markdown("<h3 style='text-align: center;'>KIMPESE SOFTWARE</h3>", unsafe_allow_html=True)

# =====================================================================
# SECTION 2 : ZONE PUBLIQUE (Capture, validation et stockage des e-mails)
# =====================================================================
st.write("---")
st.write("**Enter your business email to request priority access credentials:**")

with st.form(key="email_form", clear_on_submit=True):
    email_saisi = st.text_input("Business Email :", placeholder="name@company.com")
    submit_button = st.form_submit_button(label="Submit Request")

if submit_button:
    if email_saisi.strip() == "":
        st.error("❌ Le champ ne peut pas être vide.")
    
    # Validation du format de l'e-mail
    elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_saisi):
        
        # STOCKAGE DIRECT ET PERMANENT DANS LE FICHIER CSV
        enregistrer_email_csv(email_saisi)
        st.success("✅ Request saved! Our deployment team will email your secure credentials within 24 hours.")
        
        # Force l'application à se rafraîchir pour mettre à jour le panneau admin si besoin
        st.rerun()
    else:
        st.error("❌ Please enter a valid business email address (e.g., name@company.com).")

# =====================================================================
# SECTION 3 : ESPACE ADMINISTRATEUR SÉCURISÉ (Modification en direct)
# =====================================================================
st.write("---")
st.markdown("### 🔒 Administration Panel")

# Formulaire dédié à l'administration pour éviter les rechargements intempestifs
with st.form(key="admin_form"):
    mot_de_passe = st.text_input("Enter Admin Password to view prospects:", type="password")
    valider_admin = st.form_submit_button(label="🔑 Connexion Admin")

# Accès au panneau si le mot de passe est bon
if valider_admin or mot_de_passe == "KimpeseAdmin2026":
    if mot_de_passe == "KimpeseAdmin2026":
        st.markdown("#### 👥 Captured Prospect Emails")
        
        # Lecture en temps réel du fichier CSV
        df_prospects = lire_emails_csv()
        
        if not df_prospects.empty:
            # 1. Affichage du tableau des prospects
            st.dataframe(df_prospects, use_container_width=True)
            
            # 2. Zone d'action pour modifier/supprimer une entrée
            st.markdown("##### ⚙️ Gestion des données")
            
            # Liste déroulante contenant tous les e-mails collectés pour en choisir un à supprimer
            liste_emails = df_prospects["Emails Collectés"].tolist()
            email_selectionne = st.selectbox("Sélectionnez un e-mail à supprimer du fichier CSV :", options=liste_emails)
            
            if st.button("🗑️ Supprimer définitivement cet e-mail"):
                supprimer_email_csv(email_selectionne)
                st.success(f"L'e-mail '{email_selectionne}' a bien été retiré du fichier.")
                st.rerun() # Recharge l'application pour mettre à jour le tableau affiché
            
            st.write("")
            # 3. Bouton pour télécharger directement le fichier CSV sur votre ordinateur
            csv_data = df_prospects.to_csv(index=False, encoding="utf-8")
            st.download_button(
                label="📥 Télécharger le fichier CSV complet",
                data=csv_data,
                file_name="liste_prospects_export.csv",
                mime="text/csv"
            )
        else:
            st.info("Aucun e-mail n'a encore été enregistré dans le fichier.")
        
    elif mot_de_passe != "":
        st.error("❌ Mot de passe administrateur incorrect.")
else:
    st.info("Le tableau des prospects est masqué. Saisissez le mot de passe pour y accéder.")

# =====================================================================
# SECTION 4 : MENTION DE COPYRIGHT (Tout en bas)
# =====================================================================
st.write("") 
st.write("") 
st.write("---")
st.markdown(
    """
    <div style='text-align: center; color: #888888; font-size: 14px;'>
        © 2026 Kimpese Software. All rights reserved.
    </div>
    """, 
    unsafe_allow_html=True
)
