import streamlit as st
from openai import OpenAI
st.title("Dall-e 3")
# Champ de saisi 
user_input = st.text_input("Veuillez entré une description de l'image que vous souhaitez generer")
st.write(user_input)
# sidebare 
st.sidebar.title("Assistant")
user_notes = st.sidebar.text_input("Veuillez entrer la clé Open IA")

# Si l'utilisateur a entré une clé et un texte, on lance la génération
if api_key and user_input:
    # Initialisation de l'API avec la clé entrée
    openai.api_key = api_key

    # Appel à l'API DALL-E pour générer une image
    try:
        response = openai.Image.create(
            prompt=user_input,
            n=1,
            size="512x512"
        )

        # Extraire l'URL de l'image
        image_url = response['data'][0]['url']

        # Afficher l'image dans l'application Streamlit
        st.image(image_url, caption="Image générée", use_column_width=True)
    except Exception as e:
        st.error(f"Erreur lors de la génération de l'image : {e}")
