import streamlit as st
# Titre 
st.title("Mon formulaire")
# Texte 
st.write("Ceci est un formulaire de contact")
# Champ de saisi 
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)
# Image 
st.video("https://youtu.be/kK3gGPkO9L8")
# sidebare 
st.sidebar.title("Lysa Bouslene")
#Video 
st.sidebar.image("https://th.bing.com/th/id/OIP.QU4hu4jfXbTgoFGCWX1VgAHaC3?rs=1&pid=ImgDetMain")
# Select Bar
student_grad = st.selectbox("Selectionnez votre niveau d'etude",["Bac","Bac+2","Bac+5"])
# select slider 
age = st.select_slider("Quel est votre age ?", range(0, 99))
if age >= 18: 
  st.write("Vous etes majeur")
else:
  st.write("Vous etes mineur")
