import streamlit as st
st.title("Assistant")
# Texte 
st.write("Veuillez entré une description de l'image que vous souhaitez generer")
# Champ de saisi 
user_input = st.text_input(" ")
st.write(user_input)
# sidebare 
st.sidebar.title("Assistant")
