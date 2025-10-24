# AskNotes — Your AI Study Buddy 📚

AskNotes is a simple little app that helps turn your long, messy notes or PDFs into short, easy summaries and quick quiz questions.
It was built during the **CloudCosmos Hackathon** to make studying faster and a bit more fun.

## What it does ✨

* You can upload a **PDF, Word, or text file**
* It reads the content and gives you:

  * Short topic-wise summaries
  * A list of key terms or concepts
  * A quick quiz (MCQs or short questions) for revision

It’s like having a friend who reads your notes and tells you the important bits before exams 😄

## How it works ⚙️

* **FastAPI** runs the backend
* **Streamlit** gives a simple web interface
* **PyMuPDF** and **python-docx** handle text extraction
* **Gemini AI (Google)** is used for summarizing and quiz generation
* Data is stored in memory (or SQLite if needed)

## How to run locally 🖥️

1. Clone or download this project
2. Install all packages

   ```bash
   pip install -r requirements.txt
   ```
3. Create a file called `.env` in the main folder and add your API key:

   ```
   GEMINI_API_KEY=your_google_api_key_here
   ```
4. Start the backend:

   ```bash
   uvicorn backend.main:app --reload
   ```
5. In another terminal, run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

That’s it! Open the link Streamlit gives you and start uploading your notes.

## Why we built this 💡

During the hackathon, we wanted to help students save time while revising. Everyone’s got tons of notes but no time to go through them. AskNotes makes that easier by letting AI do the boring part for you.
