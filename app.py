import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# --- CONFIGURATION UX/UI ---
st.set_page_config(page_title="SafeRoute | Sécurité & Solidarité MEL", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #f5f5dc; }
    .main-title { font-size: 45px; font-weight: bold; color: #ffd700; text-align: center; margin-bottom: 10px; }
    .stButton>button { border-radius: 25px; background: linear-gradient(90deg, #ffd700 0%, #ffae00 100%); color: #1a1a2e; font-weight: bold; border: none; height: 50px; }
    .safe-card { background: rgba(255, 255, 255, 0.08); padding: 20px; border-radius: 15px; border-left: 5px solid #ffd700; margin-bottom: 15px; }
    .review-card { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 10px; border: 1px solid #ffd700; margin-bottom: 10px; font-style: italic; }
    .badge-verified { background-color: #4cd137; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: bold; }
    .badge-angel { background-color: #6c5ce7; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: bold; }
    .insta-link { color: #E1306C; font-weight: bold; font-size: 18px; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color: #ffd700; text-align: center;'>🛡️ SafeRoute</h1>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("MENU", ["📍 Carte & Zones", "🤝 Co-Walking & Matching", "🚨 SOS & Sécurité", "⭐ Avis & Communauté", "👥 L'Équipe Projet"])
    st.write("---")
    st.markdown("📸 **Suis-nous sur Insta :**")
    st.markdown("<a href='https://instagram.com' class='insta-link'>@SafeRoute_MEL</a>", unsafe_allow_html=True)
    st.write("---")
    st.caption("M1 Management de Projet Touristique")

# --- 1. CARTE ---
if menu == "📍 Carte & Zones":
    st.markdown("<p class='main-title'>Lieux Safe & Vigilance</p>", unsafe_allow_html=True)
    col_map, col_legend = st.columns([3, 1])
    with col_map:
        m = folium.Map(location=[50.6292, 3.0573], zoom_start=12, tiles="CartoDB dark_matter")
        # SAFE HAVENS & ZONES
        for p in [[50.633, 3.060, "Grand Place"], [50.636, 3.062, "Safe Haven: Bar Windsor"], [50.637, 3.064, "Gare Lille Flandres (Open Data: Bus 2 min)"]]:
            folium.Marker([p[0], p[1]], popup=p[2], icon=folium.Icon(color='green', icon='shield', prefix='fa')).add_to(m)
        # VIGILANCE
        for p in [[50.634, 2.964, "Ennetières (Pas d'éclairage)"], [50.618, 3.045, "Zone Sud (Isolement)"]]:
            folium.Circle([p[0], p[1]], radius=600, color="red", fill=True, popup=p[2]).add_to(m)
        st_folium(m, width="100%", height=500)
    with col_legend:
        st.subheader("Légende Pro")
        st.write("🟢 **Safe Haven** : Commerce refuge.") [cite: 77]
        st.write("🟠 **Open Data** : Transports en direct.") [cite: 26, 78]
        st.write("🔴 **Vigilance** : Zones sombres.") [cite: 30, 116]

# --- 2. CO-WALKING & MATCHING ---
elif menu == "🤝 Co-Walking & Matching":
    st.markdown("<p class='main-title'>Matching Intelligent</p>", unsafe_allow_html=True)
    role = st.segmented_control("Tu es :", ["🎓 Étudiant", "🌍 Touriste", "🏠 Habitant"]) [cite: 16, 17, 18, 19]
    col_search, col_results = st.columns([1, 1.5])
    with col_search:
        st.markdown("### 🔍 Ton trajet") [cite: 78, 131]
        with st.container(border=True):
            st.text_input("Départ")
            st.text_input("Arrivée")
            st.time_input("Heure prévue")
            if st.button("Lancer le Matching"):
                st.success("Algorithme actif (FSP3)...") [cite: 73, 78]
        st.markdown("### 🏆 Ton Parrainage") [cite: 36, 42, 48]
        st.info("Rang : **Ange Gardien** ✨")
        st.progress(0.7)

    with col_results:
        st.markdown("### 👥 Personnes à proximité") [cite: 49, 129]
        users = [
            {"name": "Alice", "role": "Étudiante", "txt": "Gare ➔ Vauban | 23:45", "v": True, "r": "Protecteur"}, [cite: 138]
            {"name": "Mark", "role": "Touriste", "txt": "Rihour ➔ Centre | 00:10", "v": False, "r": "Nouveau"} [cite: 17, 24]
        ]
        for u in users:
            verif = "<span class='badge-verified'>VÉRIFIÉ</span>" if u['v'] else ""
            st.markdown(f"<div class='safe-card'><b>👤 {u['name']} {verif}</b> ({u['role']})<br>📍 {u['txt']}</div>", unsafe_allow_html=True)

# --- 3. SOS & SÉCURITÉ ---
elif menu == "🚨 SOS & Sécurité":
    st.markdown("<p class='main-title'>Sécurité Totale</p>", unsafe_allow_html=True) [cite: 130, 132]
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 👮 Urgence")
        if st.button("📞 Appeler le 17"):
            st.toast("Appel d'urgence...") [cite: 77]
        if st.button("🔴 SOS GÉNÉRAL"):
            st.error("Position GPS partagée !") [cite: 75, 78, 132]
    with c2:
        st.markdown("### 📱 Angel Shot")
        if st.button("Simuler un Appel"):
            st.success("Appel entrant simulé...") [cite: 77]
        if st.button("🏠 BIEN ARRIVÉ.E"):
            st.balloons()

# --- 4. AVIS ---
elif menu == "⭐ Avis & Communauté":
    st.markdown("<p class='main-title'>Avis des SafeRouters</p>", unsafe_allow_html=True) [cite: 50, 134]
    reviews = [{"u": "Alice", "n": "⭐⭐⭐⭐⭐", "c": "Trop rassurant !"}, {"u": "Yasmine", "n": "⭐⭐⭐⭐⭐", "c": "Top !"}] [cite: 134, 138]
    for r in reviews:
        st.markdown(f"<div class='review-card'><b>{r['u']}</b> {r['n']}<br>'{r['c']}'</div>", unsafe_allow_html=True)
    if st.button("Publier l'avis"):
        st.success("Merci !") [cite: 134]

# --- 5. ÉQUIPE (OBS) ---
elif menu == "👥 L'Équipe Projet":
    st.markdown("<p class='main-title'>L'Équipe SafeRoute</p>", unsafe_allow_html=True) [cite: 114]
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='safe-card'>👑 <b>Lisa Marie</b><br>Chef de projet</div>", unsafe_allow_html=True) [cite: 2]
        st.markdown("<div class='safe-card'>📅 <b>Kamélia</b><br>Resp. Planification</div>", unsafe_allow_html=True) [cite: 4]
        st.markdown("<div class='safe-card'>💰 <b>Hala</b><br>Resp. Financier</div>", unsafe_allow_html=True) [cite: 5]
    with c2:
        st.markdown("<div class='safe-card'>🥈 <b>Zélie</b><br>Chef de projet adjoint</div>", unsafe_allow_html=True) [cite: 3]
        st.markdown("<div class='safe-card'>🤝 <b>Tingyu</b><br>Resp. RH</div>", unsafe_allow_html=True) [cite: 6]
        st.markdown("<div class='safe-card'>🛠️ <b>Nematullah Hussaini</b><br>Resp. Qualité</div>", unsafe_allow_html=True) [cite: 7]
