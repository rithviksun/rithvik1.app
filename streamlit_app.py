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
    ("Story Generator", "📚", "Generate a custom story with GPT-2.", "#story-generator"),
    ("Language Translator", "🌐", "Translate English text into several languages.", "#language-translator"),
    ("Weather Bot", "⛅", "Check the weather and hear the forecast aloud.", "#weather-bot"),
    ("Intent Extractor", "🧠", "Extract intents and entities from your text.", "#intent-extractor"),
]

for title, icon, description, page_hash in apps:
    st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
    st.subheader(f"{icon} {title}")
    st.write(description)
    st.markdown(f"[Open {title}]({page_hash})")
    st.markdown("</div>", unsafe_allow_html=True)

st.info("Each app is also listed in the sidebar as its own Streamlit page URL.")
