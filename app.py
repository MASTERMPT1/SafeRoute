import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# --- CONFIGURATION & DESIGN (UX/UI) ---
st.set_page_config(page_title="SafeRoute | Sécurité MEL", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #f0ead6; }
    .main-title { font-size: 45px; font-weight: bold; color: #ffd700; text-align: center; }
    .stButton>button { border-radius: 20px; background: #ffd700; color: #1a1a2e; font-weight: bold; width: 100%; }
    .safe-card { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 15px; border-left: 5px solid #ffd700; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (OBS & ÉQUIPE) ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/shield.png", width=100)
    st.markdown("## 🛡️ SAFEROUTE")
    st.caption("Projet M1 Management Touristique")
    st.write("---")
    menu = st.radio("Navigation", ["🗺️ Carte Safe", "🤝 Matching Trajet", "🚨 SOS & Alerte", "📂 Infos Projet"])
    st.write("---")
    st.markdown("**Responsable Planification :** Kamélia")

# --- CONFORMITÉ RGPD (FSC1) ---
if 'gdpr' not in st.session_state:
    with st.warning("🔐 **Conformité RGPD** : SafeRoute protège vos données. Acceptez-vous le suivi GPS pour votre sécurité ?"):
        if st.button("Accepter et continuer"):
            st.session_state['gdpr'] = True
            st.rerun()
    st.stop()

# --- 1. CARTE INTERACTIVE (GÉOLOCALISATION) ---
if menu == "🗺️ Carte Safe":
    st.markdown("<p class='main-title'>Zones Éclairées & Refuges</p>", unsafe_allow_html=True)
    
    # Carte centrée sur la MEL
    m = folium.Map(location=[50.6292, 3.0573], zoom_start=13, tiles="CartoDB dark_matter")
    
    # Points basés sur tes "FSP" (Fonctions de Service)
    folium.Marker([50.633, 3.060], popup="Grand Place - Zone Vidéoprotégée", icon=folium.Icon(color='green', icon='eye', prefix='fa')).add_to(m)
    folium.Marker([50.627, 3.058], popup="Safe Haven : Bar Solférino (Ouvert)", icon=folium.Icon(color='blue', icon='shop', prefix='fa')).add_to(m)
    
    st_folium(m, width="100%", height=500)
    st.info("💡 Les zones en surbrillance indiquent un éclairage public renforcé.")

# --- 2. MATCHING INTELLIGENT (ALGORITHME DE CORRESPONDANCE) ---
elif menu == "🤝 Matching Trajet":
    st.header("Rompre l'isolement (FSP2)")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Algorithme de Matching")
        dep = st.text_input("Point de départ")
        arr = st.text_input("Destination")
        if st.button("Chercher des partenaires"):
            st.success("Recherche en cours selon l'algorithme de proximité...")
            st.balloons()

    with col2:
        st.subheader("Groupes disponibles")
        st.markdown("""
        <div class='safe-card'>
            <b>👤 Alice (Persona)</b><br>Lille Flandres ➔ Vauban<br>Départ : 23:45
        </div>
        <div class='safe-card'>
            <b>👥 Groupe Étudiants</b><br>Solférino ➔ Cité Scientifique<br>Départ : 00:15
        </div>
        """, unsafe_allow_html=True)

# --- 3. SOS & ALERTE (FSP1) ---
elif menu == "🚨 SOS & Alerte":
    st.header("Système d'Alerte Instantané")
    st.markdown("En cas de danger, ce bouton prévient vos contacts d'urgence et les SafeRoutes à proximité.")
    
    if st.button("🔴 DÉCLENCHER LE SOS"):
        st.error("🚨 ALERTE ENVOYÉE ! Votre position est partagée avec les autorités et vos proches.")
        st.toast("Localisation envoyée...")

# --- 4. INFOS PROJET (WBS / PBS) ---
elif menu == "📂 Infos Projet":
    st.title("Structure du Projet")
    tab1, tab2 = st.tabs(["L'Équipe (OBS)", "Objectifs"])
    with tab1:
        st.write("**Chef de Projet :** Lisa Marie")
        st.write("**Adjoint :** Zélie")
        st.write("**Planification :** Kamélia")
        st.write("**RH :** Tingyu")
        st.write("**Qualité :** Nematullah")
    with tab2:
        st.write("**Finalité :** Améliorer l'image de la MEL et renforcer le lien social.")
