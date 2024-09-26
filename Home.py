import streamlit as st
# Titre 
st.title("Mon formulaire")
# Texte 
st.write("Ceci est un formulaire de contact")
# Champ de saisi 
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)
# Image 
st.image("https://th.bing.com/th/id/OIP.QU4hu4jfXbTgoFGCWX1VgAHaC3?rs=1&pid=ImgDetMain")
# sidebare 
st.sidebar.title("Lysa Bouslene")
#Video 
st.sidebar.video("https://youtu.be/kK3gGPkO9L8")
