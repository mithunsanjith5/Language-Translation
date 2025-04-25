import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import torch
st.set_page_config(page_title="Multilingual Translator", layout="centered")
LANG_CODE = {
    "English": "en", "French": "fr", "German": "de", "Spanish": "es", "Italian": "it",
    "Russian": "ru", "Chinese": "zh", "Japanese": "ja", "Korean": "ko", "Arabic": "ar",
    "Hindi": "hi", "Bengali": "bn", "Urdu": "ur", "Tamil": "ta", "Telugu": "te",
    "Marathi": "mr", "Gujarati": "gu", "Punjabi": "pa", "Malayalam": "ml", "Kannada": "kn",
    "Odia": "or", "Assamese": "as", "Portuguese": "pt", "Dutch": "nl", "Polish": "pl",
    "Swedish": "sv", "Turkish": "tr", "Vietnamese": "vi", "Thai": "th", "Indonesian": "id",
    "Greek": "el", "Hebrew": "he", "Czech": "cs", "Ukrainian": "uk"
}
@st.cache_resource
def load_model():
    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return tokenizer, model, device
st.title("🌍 Multilingual Translator")
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"
    st.session_state.target_lang = "French"
col1, col2 = st.columns([1, 1])
with col1:
    st.session_state.source_lang = st.selectbox("Source Language", list(LANG_CODE.keys()), index=list(LANG_CODE.keys()).index(st.session_state.source_lang))
with col2:
    st.session_state.target_lang = st.selectbox("Target Language", list(LANG_CODE.keys()), index=list(LANG_CODE.keys()).index(st.session_state.target_lang))
if st.button("🔄 Swap Languages"):
    st.session_state.source_lang, st.session_state.target_lang = st.session_state.target_lang, st.session_state.source_lang
    st.experimental_rerun()
text_to_translate = st.text_area("Enter text to translate", height=150)
st.caption(f"📝 Character count: {len(text_to_translate.strip())}")
with st.spinner("Loading model..."):
    tokenizer, model, device = load_model()
translation = ""
if st.button("Translate"):
    src_code = LANG_CODE.get(st.session_state.source_lang)
    tgt_code = LANG_CODE.get(st.session_state.target_lang)
    if src_code and tgt_code and text_to_translate.strip():
        tokenizer.src_lang = src_code
        encoded = tokenizer(text_to_translate, return_tensors="pt").to(device)
        generated_tokens = model.generate(
            **encoded,
            forced_bos_token_id=tokenizer.get_lang_id(tgt_code)
        )
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        st.success("✅ Translation:")
        st.text_area("Output", translation, height=150)

        st.download_button("📥 Download Translation", data=translation, file_name="translation.txt")
    else:
        st.error("Please enter valid input and select languages.")
st.markdown("---")
st.caption("Built with 🤗 Transformers + Streamlit")

