import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Intent Extractor", page_icon="🧠")

st.title("🧠 Intent and Entity Extractor")
st.write("Extract intents and entities from a sentence using OpenAI.")

try:
    client = OpenAI(api_key=st.secrets["OpenAI_Key"])
except Exception:
    client = None


def extract_and_categorize(text: str):
    if client is None:
        raise RuntimeError("OpenAI credentials are not configured in Streamlit secrets.")

    prompt = f"""
    Extract and categorize the intents and entities from the following text:

    Text: "{text}"

    Provide the result in the following JSON format:
    {{
        "intents": [
            {{"intent": "<intent>", "category": "<category>"}}
        ],
        "entities": [
            {{"entity": "<entity>", "category": "<category>"}}
        ]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()


user_input = st.text_input("Enter your query:")

if st.button("Extract"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
        st.stop()

    try:
        result = extract_and_categorize(user_input)
        st.write("Extracted and Categorized Intents and Entities:")
        st.json(result)
    except Exception as exc:
        st.error(f"Intent extraction failed: {exc}")
