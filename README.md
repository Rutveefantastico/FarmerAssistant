# 🌾 AI Farmer Assistant

An AI-powered web application built with **Flask** and **Google Gemini**
that helps farmers get simple, practical answers to agriculture-related
questions.

The application supports: - 🌱 Agriculture-related questions - 📍
Location-based answers - 🖼️ Image-based agriculture queries - 🇮🇳 Hindi /
English language handling - 🔤 Hindi transliteration - 🤖 AI-generated
farmer-friendly responses using Gemini

## ✨ Features

### 1. AI Farmer Assistant

Farmers can ask agriculture-related questions in a simple interface. The
application sends the question to Google Gemini and returns a concise,
farmer-friendly answer.

### 2. Image Analysis

Users can upload an agricultural image and ask questions about it.

Supported image formats: - PNG - JPG / JPEG - WebP

For example, users can upload an image of a crop, leaf, disease symptom,
or agricultural problem and ask the AI for guidance.

### 3. Location Support

Users can provide their location along with their question so that the
AI can consider the location while generating its response.

### 4. Hindi Language Support

The application uses `langdetect` to detect the language and
`indic-transliteration` to handle Hindi transliteration.

### 5. Simple HTML Responses

Gemini responses are requested in clean HTML format using headings,
paragraphs, bold text, and bullet points for easy reading.

## 🛠️ Technologies Used

-   **Python**
-   **Flask**
-   **Google Gemini API**
-   **Gemini 2.5 Flash**
-   **LangDetect**
-   **Indic Transliteration**
-   **HTML/CSS**
-   **python-dotenv**

## 📁 Project Structure

``` text
AI-Farmer-Assistant/
│
├── templates/
│   └── index.html
│
├── uploads/
│ 
├── app.py
├── test_env.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR-USERNAME/AI-Farmer-Assistant.git
cd AI-Farmer-Assistant
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

``` env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit the real API key to GitHub.

### 5. Run the application

``` bash
python app.py
```

Open:

``` text
http://127.0.0.1:5000
```

## 🔑 Environment Variable

The application requires:

``` text
GEMINI_API_KEY
```

You can use `.env.example` as a template:

``` env
GEMINI_API_KEY=your_api_key_here
```

## 🖼️ Image Upload

The application can process uploaded agricultural images.

Recommended formats:

``` text
PNG
JPG / JPEG
WebP
```

The uploaded image is sent to Gemini together with the farmer's
question.

## 💡 Example Questions

-   What disease is affecting this crop?
-   Why are the leaves turning yellow?
-   What fertilizer should I use for this crop?
-   How can I control pests on my plants?
-   What could be the problem with this leaf?
-   What should I do to improve crop growth?

## 🔒 Security

Important:

-   Never upload `.env` to GitHub.
-   Never expose your Gemini API key in source code.
-   Do not commit private credentials or tokens.
-   Uploaded images should normally not be committed to the repository.

## 🚀 Future Improvements

Possible future enhancements include:

-   🌦️ Weather API integration
-   🌱 Crop recommendation
-   🦠 Advanced crop disease detection
-   📍 GPS-based location detection
-   🗣️ Voice input
-   🔊 Text-to-speech responses
-   🌐 More Indian language support
-   📊 Farmer history and analytics
-   📱 Mobile-friendly/PWA version

## 👨‍💻 My Team

**1.Yashika Mathur**
**2.Aarzoo Rawat**
**3.Megha Chauhan**
**4.Rutvee Yadav**


Focused on building practical AI and data-driven applications.

## 📄 License

This project is available for educational and portfolio purposes.
