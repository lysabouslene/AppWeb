import streamlit as st
from openai import OpenAI
st.title("Dall-e 3")
# Champ de saisi 
user_input = st.text_input("Veuillez entré une description de l'image que vous souhaitez generer")
st.write(user_input)
# sidebare 
st.sidebar.title("Assistant")
user_notes = st.sidebar.text_input("Veuillez entrer la clé Open IA")

# Testez ici plusieurs variation du prompte
prompt = "A cute baby sea otter"



image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)

                
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
