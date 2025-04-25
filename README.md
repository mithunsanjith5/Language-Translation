# 🌍 Multilingual Translator

Translate text between 35+ languages using Facebook's M2M100 model — all in a simple Streamlit web app.

## 🚀 Features

- 🔤 Translate between English, French, German, Hindi, Chinese, Arabic, and many more
- 🤗 Uses `facebook/m2m100_418M` from Hugging Face Transformers
- 🔄 One-click language swap
- ✍️ Text input with live character count
- 📥 Download translation as `.txt`
- ⚡ GPU support + model caching for performance

## 🖥️ Run Locally

```bash
# Clone the repo
git clone https://github.com/mithunsanjith5/multilingual-translator.git
cd multilingual-translator

# Install dependencies
pip install streamlit torch transformers

# Start the app
streamlit run app.py
