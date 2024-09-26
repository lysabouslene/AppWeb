import streamlit as st
from openai import OpenAI
st.title("Dall-e 3")
# Champ de saisi 
user_input = st.text_input("Veuillez entré une description de l'image que vous souhaitez generer")
st.write(user_input)
# sidebare 
st.sidebar.title("Assistant")
user_notes = st.sidebar.text_input("Veuillez entrer la clé Open IA")

# Sélection de la taille de l'image dans la sidebar
image_size = st.sidebar.selectbox("Sélectionnez la taille de l'image :", ["256x256", "512x512", "1024x1024"])

# Bouton dans la sidebar pour générer l'image
if st.sidebar.button("Générer l'image"):

    if user_input:
        # Afficher un spinner pendant la génération de l'image
        with st.spinner("Génération de l'image en cours..."):
            try:
                # Appel à l'API OpenAI pour générer l'image avec DALL·E 2 ou DALL·E 3
                response = openai.Image.create(
                    prompt=user_input,
                    n=1,  # Générer une seule image
                    size=image_size  # Taille de l'image sélectionnée
                )
                
                # Récupérer l'URL de l'image générée
                image_url = response['data'][0]['url']
                
                # Afficher l'image générée
                st.image(image_url, caption=f"Image générée pour : '{user_input}'", use_column_width=True)
            except Exception as e:
                # En cas d'erreur
                st.error(f"Une erreur est survenue lors de la génération de l'image : {e}")
    else:
        # Si l'utilisateur n'a pas entré de prompt
        st.error("Veuillez entrer une description pour générer l'image.")

                
                # Récupérer l'URL de l'image générée
                image_url = response['data'][0]['url']
                
                # Afficher l'image générée
                st.image(image_url, caption=f"Image générée pour : '{user_input}'", use_column_width=True)
            except Exception as e:
                # En cas d'erreur
                st.error(f"Une erreur est survenue lors de la génération de l'image : {e}")
    else:
        # Si l'utilisateur n'a pas entré de prompt
        st.error("Veuillez entrer une description pour générer l'image.")
