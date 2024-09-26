import streamlit as st
# Titre 
st.title("Mon formulaire")
# Texte 
st.write("Ceci est un formulaire de contact")
# Champ de saisi 
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)
# Image 
st.image("https://www.bing.com/images/search?view=detailV2&ccid=QU4hu4jf&id=EAC4710304CE3DE706BB8FEFED235C878B9C5BF4&thid=OIP.QU4hu4jfXbTgoFGCWX1VgAHaC3&mediaurl=https%3A%2F%2Fcuration.k.krugazor.eu%2Fcontent%2Fimages%2F2021%2F05%2Feemi-logo.png&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.414e21bb88df5db4e0a05182597d5580%3Frik%3D9Fuci4dcI%252b3vjw%26pid%3DImgRaw%26r%3D0&exph=619&expw=1600&q=eemi+image&simid=608046659916536381&form=IRPRST&ck=70733B17D2A435DD74E8EF00BA494E2B&selectedindex=1&itb=1&ajaxhist=0&ajaxserp=0&pivotparams=insightsToken%3Dccid_czf6PQ0K*cp_39AA80D898B6CFAE9953E5F30294EE94*mid_BFECD48DC600A7D8325FF156CF791CF831CD5249*simid_607997645781557491*thid_OIP.czf6PQ0Ke!_aKhq7jGcwM2wHaDm&vt=0&sim=11&iss=VSI&ajaxhist=0&ajaxserp=0")
