🌍 Multilingual Translator
A simple yet powerful multilingual translation app built with Streamlit and Hugging Face Transformers. Translate text between 35+ languages using Facebook's M2M100 model, all within an intuitive web interface.

🚀 Features
🔤 Translate between 35+ popular languages

🌐 Powered by the M2M100 multilingual model from Facebook

🔄 One-click language swapping

✏️ Live character count

📥 Downloadable translations

⚡ GPU acceleration support (if available)

🔒 Efficient model caching with @st.cache_resource

🖥️ Demo
"Translate once, understand everywhere."
Try it locally or deploy to the cloud with ease!

🧩 Supported Languages
English, French, German, Spanish, Italian, Russian, Chinese, Japanese, Korean, Arabic, Hindi, Bengali, Urdu, Tamil, Telugu, Marathi, Gujarati, Punjabi, Malayalam, Kannada, Odia, Assamese, Portuguese, Dutch, Polish, Swedish, Turkish, Vietnamese, Thai, Indonesian, Greek, Hebrew, Czech, Ukrainian

📦 Installation
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/multilingual-translator.git
cd multilingual-translator
2. Set up the environment
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt doesn't exist yet, use:

bash
Copy
Edit
pip install streamlit torch transformers
3. Run the app
bash
Copy
Edit
streamlit run app.py
🧠 Model Info
Model: facebook/m2m100_418M

Architecture: Fully multilingual, many-to-many translation support

Uses language tokens for controlled translation directions

📸 Screenshots

Input & Language Selection	Output with Download Option
Add your screenshots under a /screenshots folder for better visuals.

💡 Future Enhancements
 Auto language detection

 Translation history panel

 Audio input/output support

 Dark mode toggle

🤝 Contributions
Contributions, issues, and feature requests are welcome!

Fork the repo

Create a new branch (git checkout -b feature/new-feature)

Commit changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/new-feature)

Open a Pull Request

📜 License
This project is licensed under the MIT License.

🛠 Built With
Streamlit

Transformers

PyTorch

✨ Acknowledgements
Hugging Face 🤗 for the M2M100 model

Facebook AI Research

Streamlit community
