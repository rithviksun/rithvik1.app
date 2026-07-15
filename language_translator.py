import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Ai Language Translator", page_icon="🌐",)

st.title("🌐 Ai Language Translator")
st.write("Translates English into different languages")

@st.cache_resource
def load_model():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-fr"
    )
translator = load_model()
languages = {
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Italian": "Helsinki-NLP/opus-mt-en-it",
}

language = st.selectbox(
    "Select Language",
    list(languages.keys())
)

text = st.text_area("Enter English text")

if st.button("Translate"):
    with st.spinner("Loading model..."):
        translator = pipeline(
            "translation",
            model=languages[language]
        )
        result = translator(text)

