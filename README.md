# AskNotes — Your AI Study Buddy 📚

AskNotes is a simple little app that helps turn your long notes or PDFs into short summaries and quick quiz questions.
It was built during the **CloudCosmos Hackathon** to make studying faster and a bit more fun.

---

## ✨ What it does

* Upload a **PDF, DOCX, or TXT file**
* It reads the content and gives you:

  * Short, topic-wise summaries
  * A few key terms or keywords
  * A quick quiz (MCQs or short questions) for revision

It’s like having a friend who skims your notes and tells you the important parts before exams 😄

---

## ⚙️ How it works

* **FastAPI** handles the backend
* **Streamlit** provides a simple front-end interface
* **PyMuPDF** and **python-docx** extract text from uploaded files
* **Gemini AI (Google)** does the summarization and quiz generation
* **SQLite or in-memory storage** is used for temporary data

---

## 🖥️ How to Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AskNotes.git
cd AskNotes
```

### 2️⃣ Create and activate a virtual environment

#### 🪟 On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your API key

Create a `.env` file in the main folder and add:

```
GEMINI_API_KEY=your_google_api_key_here
```

(You can get one from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey))

### 5️⃣ Start the backend

```bash
uvicorn backend.main:app --reload
```

### 6️⃣ Run the frontend

In another terminal window:

```bash
streamlit run frontend/streamlit_app.py
```

Then open the link Streamlit gives you — usually `http://localhost:8501`.

---

## 💡 Why we built this

We wanted to make studying less painful.
Everyone’s got huge notes but no time to read them all. AskNotes makes that easier by summarizing and creating quick revision questions automatically.

---

## 🧩 Project Structure

```
AskNotes/
├── backend/
│   ├── ai_client.py
│   ├── main.py
│   └── parse_utils.py
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
