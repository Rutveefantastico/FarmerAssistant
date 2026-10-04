from flask import Flask, render_template, request, send_from_directory, url_for
from langdetect import detect
from dotenv import load_dotenv
import os
import google.generativeai as genai

# For Hindi transliteration
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Secure filename
from werkzeug.utils import secure_filename


app = Flask(__name__)

load_dotenv()


# =========================================================
# Initialize Gemini
# =========================================================

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


# =========================================================
# Upload folder
# =========================================================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# =========================================================
# Serve uploaded images
# =========================================================

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# =========================================================
# Main route
# =========================================================

@app.route("/", methods=["GET", "POST"])
def index():

    user_question = None
    final_answer = None
    image_url = None
    location = ""

    if request.method == "POST":

        user_question = request.form.get("question", "")
        location = request.form.get("location", "").strip()

        # =================================================
        # Handle image upload
        # =================================================

        uploaded_file = request.files.get("image")

        image_path = None

        if uploaded_file and uploaded_file.filename:

            # Secure the filename
            filename = secure_filename(uploaded_file.filename)

            # Full path
            image_path = os.path.join(UPLOAD_FOLDER, filename)

            # Save image
            uploaded_file.save(image_path)

            # URL for displaying image in browser
            image_url = url_for(
                "uploaded_file",
                filename=filename
            )

        try:

            # =================================================
            # Detect language
            # =================================================

            try:
                detected_lang = detect(user_question)

            except Exception:
                detected_lang = "en"


            # =================================================
            # Convert Hindi to Devanagari
            # =================================================

            if detected_lang == "hi":

                user_question = transliterate(
                    user_question,
                    sanscript.ITRANS,
                    sanscript.DEVANAGARI
                )


            # =================================================
            # Prepare prompt
            # =================================================

            prompt = f"""
You are an AI agriculture assistant.

Format the answer in clean HTML using:

- <h3> for headings
- <b> for bold text
- <ul><li> for bullet points
- <p> for paragraphs

Do not include Markdown such as ** or ##.

Keep the answer short, clear, practical, and farmer-friendly.

Farmer's Question:
{user_question}

Location:
{location}
"""


            # =================================================
            # Generate Gemini response
            # =================================================

            if image_path:

                with open(image_path, "rb") as img_file:

                    image_data = img_file.read()


                # Detect uploaded image MIME type
                mime_type = uploaded_file.mimetype


                # Normalize JPG MIME type
                if mime_type == "image/jpg":
                    mime_type = "image/jpeg"


                # Supported image formats
                allowed_types = [
                    "image/png",
                    "image/jpeg",
                    "image/webp"
                ]


                if mime_type not in allowed_types:

                    raise ValueError(
                        "Unsupported image format. "
                        "Please upload PNG, JPG/JPEG, or WebP."
                    )


                response = model.generate_content(
                    contents=[
                        {
                            "mime_type": mime_type,
                            "data": image_data
                        },
                        prompt
                    ]
                )

            else:

                response = model.generate_content(
                    contents=prompt
                )


            # =================================================
            # Get response
            # =================================================

            final_answer = response.text


        except Exception as e:

            final_answer = f"""
            <p><b>⚠ Error:</b> {str(e)}</p>
            """


    # =========================================================
    # Render page
    # =========================================================

    return render_template(
        "index.html",
        question=user_question,
        answer=final_answer,
        image=image_url
    )


# =========================================================
# Run Flask
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )