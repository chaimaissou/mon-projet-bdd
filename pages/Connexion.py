import streamlit as st
from services.auth_service import AuthService
from utils.styles import get_custom_css
from utils.helpers import init_session_state

st.set_page_config(
    page_title="Connexion - Exam Scheduler",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

init_session_state()

# Style global de la page
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f8fc 0%, #e8f0ff 50%, #f0f5ff 100%);
        min-height: 100vh;
    }
    
    .login-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
        border-radius: 20px;
        padding: 2rem 3rem;
        box-shadow: 0 20px 60px rgba(91, 125, 214, 0.15);
        border: 1px solid rgba(127, 168, 232, 0.2);
        backdrop-filter: blur(10px);
        max-width: 100%;
        width: 100%;
    }
    
    .login-header {
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    .login-icon {
        font-size: 3rem;
        margin-bottom: 0.4rem;
        display: block;
    }
    
    .login-title {
        color: #2c3e50;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    
    .login-subtitle {
        color: #7c8fa3;
        font-size: 1rem;
        font-weight: 400;
        margin: 0;
    }
    
    .login-divider {
        height: 3px;
        width: 60px;
        background: linear-gradient(90deg, #7fa8e8 0%, #5b7dd6 100%);
        margin: 0.8rem auto 1.2rem auto;
        border-radius: 2px;
    }
    
    .login-form {
        margin-bottom: 2rem;
    }
    
    .input-group {
        margin-bottom: 1.2rem;
    }
    
    .input-label {
        color: #2c3e50;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.6rem;
        display: block;
        letter-spacing: 0.3px;
    }
    
    .login-button {
        margin-top: 0.3rem;
        margin-bottom: 1rem;
    }
    
    .footer-text {
        text-align: center;
        color: #a0adb6;
        font-size: 0.85rem;
    }
    
    .demo-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #f8fafc 100%);
        border-left: 4px solid #7fa8e8;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    
    .demo-item {
        margin-bottom: 0.8rem;
        font-size: 0.85rem;
    }
    
    .demo-item:last-child {
        margin-bottom: 0;
    }
    
    .demo-item-label {
        color: #5b7dd6;
        font-weight: 600;
        display: block;
        margin-bottom: 0.2rem;
    }
    
    .demo-item-value {
        color: #475569;
        font-family: 'Courier New', monospace;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.5, 2.5, 0.5])

with col2:
    st.markdown("""
    <div class="login-card">
        <div class="login-header">
            <span class="login-icon">📚</span>
            <h1 class="login-title">Exam Scheduler</h1>
            <p class="login-subtitle">Gestion Intelligente des Examens</p>
            <div class="login-divider"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="login-form">', unsafe_allow_html=True)
    
    st.markdown('<label class="input-label">👤 Matricule</label>', unsafe_allow_html=True)
    matricule = st.text_input(
        "Matricule",
        placeholder="Ex: ADM001, PROF001, ETU001",
        key="login_matricule",
        label_visibility="collapsed"
    )
    
    st.markdown('<label class="input-label">👤 Nom et Prénom</label>', unsafe_allow_html=True)
    nom_prenom = st.text_input(
        "Nom et Prénom",
        placeholder="Ex: Durand Robert",
        key="login_nom_prenom",
        label_visibility="collapsed"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="login-button">', unsafe_allow_html=True)
    if st.button("🔓 Se Connecter", use_container_width=True, type="primary"):
        if not matricule or not nom_prenom:
            st.error("⚠️ Veuillez remplir tous les champs")
        else:
            with st.spinner("⏳ Vérification des identifiants..."):
                user = AuthService.login(matricule, nom_prenom)
                
                if user:
                    st.session_state.user = user
                    st.success(f"✅ Bienvenue {user['prenom']} {user['nom']} !")
                    st.balloons()
                    
                    import time
                    time.sleep(1)
                    
                    if user['role'] == 'Administrateur':
                        st.switch_page("pages/Admin.py")
                    elif user['role'] == 'Professeur':
                        st.switch_page("pages/Chef_Dept.py")
                    else:
                        st.switch_page("pages/Consultation.py")
                else:
                    st.error("❌ Identifiants incorrects. Veuillez réessayer.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.expander("💡 Comptes de démonstration disponibles"):
        st.markdown("""
        <div class="demo-box">
            <div class="demo-item">
                <span class="demo-item-label">👨‍💼 Administrateur</span>
                <span class="demo-item-value">ADM001 / Durand Robert</span>
            </div>
            <div class="demo-item">
                <span class="demo-item-label">👔 Décideur</span>
                <span class="demo-item-value">ADM002 / Lefevre Catherine</span>
            </div>
            <div class="demo-item">
                <span class="demo-item-label">👨‍🏫 Chef Département</span>
                <span class="demo-item-value">PROF001 / Martin Jean</span>
            </div>
            <div class="demo-item">
                <span class="demo-item-label">👨‍🎓 Étudiant</span>
                <span class="demo-item-value">ETU001 / Dupont Jean</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer-text">
        <p>© 2026 Exam Scheduler - Plateforme Universitaire</p>
    </div>
    """, unsafe_allow_html=True)