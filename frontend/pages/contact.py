"""
Contact Page
"""

import streamlit as st
import requests
from frontend.config import API_CONFIG

def main():
    st.set_page_config(page_title="Contact", page_icon="📞")
    
    st.title("📞 Contact")
    st.markdown("Contactez-nous pour toute question ou demande.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Localisation")
        st.write("""
        **Institut Polytechnique de l'Université Gamal Abdel Nasser**
        
        Adresse: XXX Conakry, Guinée
        
        Tél: +224 XXX XXX XXX
        
        Email: contact@ip-uganc.edu.gn
        """)
    
    with col2:
        st.subheader("✉️ Formulaire de Contact")
        
        with st.form("contact_form"):
            name = st.text_input("Nom complet")
            email = st.text_input("Adresse email")
            subject = st.text_input("Sujet")
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Envoyer")
            
            if submitted:
                if name and email and message:
                    st.success("Merci! Votre message a été envoyé.")
                else:
                    st.error("Veuillez remplir tous les champs.")

if __name__ == "__main__":
    main()
