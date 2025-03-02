import streamlit as st
import pandas as pd

st.image("logostr.png",width=150)
st.title("Application de Gestion des Notes")
st.caption("Veuillez remplir le formulaire ci-dessous pour enregistrer une note.")

if "inscriptions" not in st.session_state:
    st.session_state.inscriptions = []

with st.form("liste_des_notes"):
    nom = st.text_input("Nom & Prenom")
    module = st.text_input("Module")
    note = st.number_input("Note Final" , min_value=0 , max_value=20)

    submit_button = st.form_submit_button("Enregistrer")

    if submit_button :
        if nom and module and note:
            st.session_state.inscriptions.append({
                "Nom & Prenom":nom,
                "Module":module,
                "Note Final":note,
            })
            st.success("Note enregistrée avec succés!")
        else:
            st.error("Veuillez remplir tous les champs requis et accepter les conditions.")

if st.session_state.inscriptions:
    df=pd.DataFrame(st.session_state.inscriptions)
    st.write("### Notes enregistrées")
    st.dataframe(df)





