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
    m = folium.Map(location=[50.6292, 3.0573], zoom_start=12, tiles="CartoDB dark_matter")
    # SAFE
    for p in [[50.633, 3.060, "Grand Place"], [50.637, 3.064, "Gare Lille Flandres"], [50.691, 3.174, "Roubaix Centre"]]:
        folium.Marker([p[0], p[1]], popup=f"SAFE: {p[2]}", icon=folium.Icon(color='green', icon='shield', prefix='fa')).add_to(m)
    # DANGER
    for p in [[50.634, 2.964, "Ennetières (Pas d'éclairage)"], [50.618, 3.045, "Zone Sud (Isolement)"]]:
        folium.Circle([p[0], p[1]], radius=600, color="red", fill=True, popup=p[2]).add_to(m)
    st_folium(m, width="100%", height=500)

# --- 2. CO-WALKING (PLUS DE MONDE) ---
elif menu == "🤝 Co-Walking & Matching":
    st.markdown("<p class='main-title'>Matching Intelligent</p>", unsafe_allow_html=True)
    role = st.segmented_control("Tu es :", ["🎓 Étudiant", "🌍 Touriste", "🏠 Habitant"])
    
    col_search, col_results = st.columns([1, 1.5])
    with col_search:
        st.markdown("### 🔍 Ton trajet")
        with st.container(border=True):
            st.text_input("Départ")
            st.text_input("Arrivée")
            st.time_input("Heure prévue")
            st.button("Lancer le Matching")

    with col_results:
        st.markdown("### 👥 Personnes à proximité")
        users = [
            {"name": "Alice", "role": "Étudiante", "txt": "Vieux-Lille ➔ Vauban | 23:45", "verified": True},
            {"name": "Mark", "role": "Touriste", "txt": "Citadelle ➔ Centre | 00:10", "verified": False},
            {"name": "Léo", "role": "Étudiant", "txt": "Lille Flandres ➔ Hellemmes | 23:55", "verified": True},
            {"name": "Sarah", "role": "Habitante", "txt": "Gambetta ➔ Wazemmes | 00:30", "verified": True},
            {"name": "Yassine", "role": "Étudiant", "txt": "Rihour ➔ Solférino | 23:20", "verified": True}
        ]
        for u in users:
            verif = "<span class='badge-verified'>VÉRIFIÉ</span>" if u['verified'] else ""
            st.markdown(f"<div class='safe-card'><b>👤 {u['name']} {verif}</b> ({u['role']})<br>📍 {u['txt']}</div>", unsafe_allow_html=True)


# --- 3. SOS & SÉCURITÉ (FSP1 - SÉCURITÉ RENFORCÉE) ---
elif menu == "🚨 SOS & Sécurité":
    st.markdown("<p class='main-title'>Assistance & Urgence</p>", unsafe_allow_html=True)
    
    st.warning("⚠️ Ces fonctionnalités sont à utiliser en cas de danger réel ou de sentiment d'insécurité imminent.")
    
    # Ligne 1 : Boutons d'appel immédiat
    col_pol, col_pomp = st.columns(2)
    with col_pol:
        st.markdown("### 👮 Police / Secours")
        if st.button("📞 Appeler le 17 (ou 112)"):
            st.info("Appel d'urgence en cours... (Simulation)")
            
    with col_pomp:
        st.markdown("### 🚑 SAMU / Pompiers")
        if st.button("📞 Appeler le 15 (ou 18)"):
            st.info("Appel secours en cours... (Simulation)")

    st.write("---")

    # Ligne 2 : Alertes communautaires et proches
    col_sos, col_contact = st.columns(2)
    with col_sos:
        st.markdown("### 🚨 Alerte SafeRoute")
        if st.button("🔴 SOS : ALERTE GÉNÉRALE"):
            st.error("🚨 SOS ACTIVÉ ! Votre position GPS est partagée avec les SafeRouters à moins de 500m.")
            st.toast("Signal envoyé à la communauté...")

    with col_contact:
        st.markdown("### 📱 Mes Proches")
        if st.button("💬 PRÉVENIR MES CONTACTS"):
            st.success("✅ SMS envoyé : 'Je ne me sens pas en sécurité, suis mon trajet sur SafeRoute'.")

    st.write("---")

    # Options de prévention (Mode Discret & Arrivée)
    st.subheader("⚙️ Options de protection")
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        if st.toggle("🔕 Mode Discret (Écran noir)"):
            st.info("L'application reste active mais l'écran est assombri pour plus de discrétion.")
            
    with col_opt2:
        if st.button("🏠 JE SUIS BIEN ARRIVÉ.E"):
            st.balloons()
            st.success("Trajet terminé! Vos proches ont été rassurés grâce à une notification.")

# --- 4. AVIS & NOTES (NOUVEAU) ---
elif menu == "⭐ Avis & Communauté":
    st.markdown("<p class='main-title'>Avis des SafeRouters</p>", unsafe_allow_html=True)
    st.subheader("Note moyenne : ⭐ 4.8/5")
    
    reviews = [
        {"user": "Alice", "note": "⭐⭐⭐⭐⭐", "comm": "Grâce à SafeRoute, je ne stresse plus pour rentrer après la BU le soir !"},
        {"user": "Adam", "note": "⭐⭐⭐⭐", "comm": "Very helpful for a tourist who doesn't know the safe areas of Lille."},
        {"user": "Yasmine", "note": "⭐⭐⭐⭐⭐", "comm": "Le système de matching est top, j'ai rencontré des gens super sympas."},
        {"user": "Thomas", "note": "⭐⭐⭐⭐⭐", "comm": "Rassurant de voir les zones éclairées sur la carte."}
    ]
    for r in reviews:
        st.markdown(f"<div class='review-card'><b>{r['user']}</b> {r['note']}<br>'{r['comm']}'</div>", unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("Laisser une note sur ton dernier trajet")
    st.select_slider("Ta note", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    st.text_area("Ton avis")
    if st.button("Publier l'avis"):
        st.success("Merci ! Ton avis renforce la confiance de la communauté.")

# --- 5. L'ÉQUIPE PROJET (OBS) ---
elif menu == "👥 L'Équipe Projet":
    st.markdown("<p class='main-title'>Qui sommes nous?</p>", unsafe_allow_html=True)
    st.markdown("### 👑 Direction")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='safe-card'><b>Lisa Marie</b><br>Chef de projet</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'><b>Kamélia</b><br>Responsable planification</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'><b>Hala</b><br>Responsable financier</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='safe-card'><b>Zélie</b><br>Chef de projet adjoint</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'><b>Tingyu</b><br>Responsable RH</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'><b>Nematullah Hussaini</b><br>Responsable Qualité</div>", unsafe_allow_html=True)
