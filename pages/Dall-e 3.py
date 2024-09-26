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
        # Afficher l'image dans l'application Streamlit
        st.image(image_url, caption="Image générée", use_column_width=True)
    except Exception as e:
        st.error(f"Erreur lors de la génération de l'image : {e}")
