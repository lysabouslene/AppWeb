import streamlit as st
st.title("dall-e 3")
# Texte 
st.write("Veuillez entré une description de l'image que vous souhaitez generer")
# Champ de saisi 
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)
