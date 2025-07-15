import streamlit as st
import pyttsx3
from googletrans import Translator

st.set_page_config(page_title="Translator", page_icon="🌍")

st.title("Multilingual Text-to-Speech Translator")
st.subheader("Translate and listen to text in multiple languages")
st.markdown("Type your sentence below and hear it translated.")

user_input = st.text_input("Enter text to translate:")

language_map = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "English": "en"
}

selected_language = st.selectbox("Translate to:", list(language_map.keys()))

def translate_and_speak(text, target_lang):
    translator = Translator()
    
    st.markdown(f"**You entered:** {text}")

    lang_code = language_map[target_lang]

    try:
       result = translator.translate(text, dest=lang_code)
       print(result)
       st.markdown(f"**Translation in {target_lang}:** {result.text}")

       engine = pyttsx3.init()
       st.success("Speaking the translated text...")

       engine.say(result.text)

       engine.runAndWait()
      
    except Exception as e:
        st.error(f"Error during translation: {e}")
      

if st.button("🔊 Translate & Speak"):
    user_input = user_input.strip()
    if user_input == "":
        st.warning("Please enter some text to translate.")
    else:
        translate_and_speak(user_input, selected_language)
