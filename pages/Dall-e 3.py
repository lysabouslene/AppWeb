import streamlit as st
from openai import OpenAI
st.title("Dall-e 3")
# Champ de saisi 
user_input = st.text_input("Veuillez entré une description de l'image que vous souhaitez generer")
st.write(user_input)
# sidebare 
st.sidebar.title("Assistant")
user_notes = st.sidebar.text_input("Veuillez entrer la clé Open IA")

# Vérifiez si la clé API et la description de l'image sont fournies
if not api_key:
    st.sidebar.warning("Veuillez entrer votre clé API OpenAI pour générer une image.")
elif not user_input:
    st.warning("Veuillez entrer une description pour générer une image.")
else:
    # Si l'utilisateur a entré une clé et un texte, on lance la génération
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
