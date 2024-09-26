import streamlit as st
st.title("Dall-e 3")
# Texte 
st.write("Veuillez entré une description de l'image que vous souhaitez generer")
# Champ de saisi 
user_input = st.text_input("Veuillez entré une description de l'image que vous souhaitez generer")
st.write(user_input)
# sidebare 
st.sidebar.title("Assistant")
