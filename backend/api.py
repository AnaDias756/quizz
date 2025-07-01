from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import sqlite3
import os

app = FastAPI()

# Habilita CORS para acesso externo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Corrigir caminho da pasta static no Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Redirecionar / para o HTML
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

@app.get("/quiz")
def get_questions():
    db_path = os.path.join(BASE_DIR, "..", "quiz_questions.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, question_number, statement, option_a, option_b, option_c, option_d, option_e FROM questions LIMIT 10")
    rows = cursor.fetchall()
    conn.close()

    quiz_data = []
    for row in rows:
        quiz_data.append({
            "id": row[0],
            "question": row[2],
            "options": {
                "a": row[3],
                "b": row[4],
                "c": row[5],
                "d": row[6],
                "e": row[7],
            },
            "correct": None
        })

    return quiz_data