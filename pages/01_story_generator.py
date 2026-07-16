import streamlit as st

st.set_page_config(page_title="Ai Story Generator", page_icon="📚")

st.title("📚 Ai Story Generator")
st.write("Generate creative stories using GPT-2")

try:
    from transformers import pipeline
except Exception as exc:
    pipeline = None
    MODEL_IMPORT_ERROR = str(exc)
else:
    MODEL_IMPORT_ERROR = None


@st.cache_resource
def load_model():
    if pipeline is None:
        raise RuntimeError(MODEL_IMPORT_ERROR or "Transformers is not available.")
    return pipeline("text-generation", model="gpt2")


if pipeline is None:
    st.error("Story generation is unavailable because the Hugging Face model dependencies are not installed.")
    st.stop()


topic = st.text_input("Story Topic:", placeholder="A dragon that loves pizza")
genre = st.selectbox("Select Genre:", ["Adventure", "Fantasy", "Sci-Fi", "Mystery", "Comedy", "Horror"])
length = st.slider("Story Length", 100, 400, 200, step=50)

if st.button("Generate Story"):
    if topic.strip() == "":
        st.warning("Please enter a story topic.")
        st.stop()

    prompt = f"""
Title: {topic}
Genre: {genre}
Once upon a time
"""

    with st.spinner("Ai is writing your story..."):
        try:
            generator = load_model()
            result = generator(
                prompt,
                max_new_tokens=length,
                temperature=0.9,
                do_sample=True,
                top_p=0.95,
                repetition_penalty=1.2,
                pad_token_id=50256,
            )
        except Exception as exc:
            st.error(f"Model generation failed: {exc}")
            st.stop()

    story = result[0]["generated_text"].replace(prompt, "").strip()
    st.subheader("Your Story:")
    st.write(story)
