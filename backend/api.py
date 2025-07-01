# backend/api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste para segurança em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quiz")
def get_questions():
    conn = sqlite3.connect("quiz_questions.db")
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
            "correct": None  # opcional, se quiser validar resposta
        })

    return quiz_data