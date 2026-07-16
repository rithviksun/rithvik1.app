import streamlit as st

st.set_page_config(page_title="Rithvik AI Hub", page_icon="🚀", layout="wide")

st.title("🚀 Rithvik's AI App Hub")
st.write("Choose a tool below to open it directly from the main page.")

st.markdown(
    """
    <style>
    .app-card {
        border: 1px solid #dfe3e8;
        border-radius: 0.85rem;
        padding: 1rem;
        margin-bottom: 0.9rem;
        background: #f8fafc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

apps = [
    ("Story Generator", "📚", "Generate a custom story with GPT-2.", "pages/01_story_generator.py"),
    ("Language Translator", "🌐", "Translate English text into several languages.", "pages/02_language_translator.py"),
    ("Weather Bot", "⛅", "Check the weather and hear the forecast aloud.", "pages/03_weather_bot.py"),
    ("Intent Extractor", "🧠", "Extract intents and entities from your text.", "pages/04_intent_extractor.py"),
]

for title, icon, description, page_path in apps:
    st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
    st.subheader(f"{icon} {title}")
    st.write(description)
    if st.button(f"Open {title}", key=f"open_{title.replace(' ', '_').lower()}"):
        st.switch_page(page_path)
    st.markdown("</div>", unsafe_allow_html=True)

st.info("Each app also appears in the sidebar as its own Streamlit page URL.")
