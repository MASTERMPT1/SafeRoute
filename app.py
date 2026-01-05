import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# --- CONFIGURATION UX/UI ---
st.set_page_config(page_title="SafeRoute | Sécurité MEL", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #f5f5dc; }
    .main-title { font-size: 40px; font-weight: bold; color: #ffd700; text-align: center; }
    .stButton>button { border-radius: 20px; background: #ffd700; color: #1a1a2e; font-weight: bold; }
    .safe-card { background: rgba(255, 255, 255, 0.07); padding: 15px; border-radius: 15px; border-left: 5px solid #ffd700; margin-bottom: 10px; }
    .danger-card { background: rgba(255, 0, 0, 0.1); padding: 15px; border-radius: 15px; border-left: 5px solid #ff4b4b; margin-bottom: 10px; }
    .insta-link { color: #E1306C; font-weight: bold; text-decoration: none; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (ORGANIGRAMME & SOCIALS) ---
with st.sidebar:
    st.markdown("<h1 style='color: #ffd700;'>🛡️ SafeRoute</h1>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("MENU", ["📍 Carte Safe & Zones", "🤝 Co-Walking", "🚨 SOS", "👥 Notre Équipe"])
    
    st.write("---")
    st.markdown("### 📱 Suivez-nous")
    st.markdown("📸 [Instagram @SafeRoute_MEL](https://instagram.com/saferoute_mel)", unsafe_allow_html=True)
    st.write("---")
    st.caption("Projet M1 Management Touristique")

# --- 1. CARTE AVEC LIEUX SAFE & DANGEREUX ---
if menu == "📍 Carte Safe & Zones":
    st.markdown("<p class='main-title'>Cartographie de la Métropole</p>", unsafe_allow_html=True)
    
    # Carte centrée sur la MEL
    m = folium.Map(location=[50.6292, 3.0573], zoom_start=12, tiles="CartoDB dark_matter")
    
    # --- LIEUX SAFE (Vert/Bleu) ---
    safe_locations = [
        [50.633, 3.060, "Grand Place (Lille) - Très éclairé"],
        [50.637, 3.064, "Gare Lille Flandres - Présence agents"],
        [50.612, 3.076, "Cité Scientifique - Points SOS"],
        [50.691, 3.174, "Grand Place (Roubaix) - Safe Haven"],
        [50.723, 3.161, "Centre Tourcoing - Zone caméra"]
    ]
    for loc in safe_locations:
        folium.Marker([loc[0], loc[1]], popup=loc[2], icon=folium.Icon(color='green', icon='shield', prefix='fa')).add_to(m)

    # --- LIEUX DANGEREUX / VIGILANCE (Rouge) ---
    danger_zones = [
        [50.634, 2.964, "Ennetières-en-Weppes - Manque d'éclairage"],
        [50.618, 3.045, "Zone Sud - Travaux / Éclairage HS"],
        [50.678, 3.189, "Zone Industrielle - Très isolée la nuit"]
    ]
    for loc in danger_zones:
        folium.Circle([loc[0], loc[1]], radius=500, color="red", fill=True, popup=loc[2]).add_to(m)
    
    st_folium(m, width="100%", height=550)

# --- 2. CO-WALKING ---
elif menu == "🤝 Co-Walking":
    st.header("🤝 Rompre l'isolement dans le trajet")
    st.info("Utilisez le système de matching pour ne plus rentrer seul(e).")
    st.markdown("""
    <div class='safe-card'><b>🟢 Alice</b> : Gare Lille Flandres ➔ Vauban (Départ : 23h30)</div>
    <div class='danger-card'>⚠️ <b>Alerte</b> : Éclairage signalé HS rue Solférino.</div>
    """, unsafe_allow_html=True)

# --- 3. SOS ---
elif menu == "🚨 SOS":
    st.header("Système d'Alerte SOS")
    if st.button("🔴 ACTIVER LE SIGNAL SOS"):
        st.error("ALERTE ENVOYÉE AUX CONTACTS D'URGENCE.")

# --- 4. L'ÉQUIPE (OBS) ---
elif menu == "👥 Notre Équipe":
    st.markdown("<p class='main-title'>Organigramme du Projet</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Direction")
        st.write("👑 **Lisa Marie** - Chef de projet")
        st.write("🥈 **Zélie** - Chef de projet adjoint")
        st.write("📅 **Kamélia** - Responsable planification")
    
    with col2:
        st.subheader("Pôles Opérationnels")
        st.write("💰 **Hala** - Responsable financier")
        st.write("🤝 **Tingyu** - Responsable RH")
        st.write("🛠️ **Nematullah Hussaini** - Responsable ressource matérielle/qualité")
    
    st.write("---")
    st.image("https://img.icons8.com/clouds/200/group.png", width=150)
    st.info("SafeRoute est un projet collaboratif visant à améliorer l'image de la MEL et le lien social.")
