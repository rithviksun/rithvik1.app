import streamlit as st

st.set_page_config(page_title="Ai Language Translator", page_icon="🌐")

st.title("🌐 Ai Language Translator")
st.write("Translates English into different languages")

try:
    from transformers import pipeline
except Exception as exc:
    pipeline = None
    MODEL_IMPORT_ERROR = str(exc)
else:
    MODEL_IMPORT_ERROR = None


languages = {
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Italian": "Helsinki-NLP/opus-mt-en-it",
}


@st.cache_resource
def load_model(model_name: str):
    if pipeline is None:
        raise RuntimeError(MODEL_IMPORT_ERROR or "Transformers is not available.")
    return pipeline("translation", model=model_name)


if pipeline is None:
    st.error("Translation is unavailable because the Hugging Face model dependencies are not installed.")
    st.stop()

language = st.selectbox("Select Language", list(languages.keys()))
text = st.text_area("Enter English text")

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text to translate.")
        st.stop()

    with st.spinner("Loading model..."):
        try:
            translator = load_model(languages[language])
            result = translator(text)
        except Exception as exc:
            st.error(f"Translation failed: {exc}")
            st.stop()

    st.success(result[0]["translation_text"])
