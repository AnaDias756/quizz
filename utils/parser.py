# utils/parser.py
import fitz  # PyMuPDF
import re
import sqlite3

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_questions(text):
    question_blocks = re.findall(r"(Questão\s+\d+.*?)(?=Questão\s+\d+|\Z)", text, re.DOTALL)
    questions = []

    for block in question_blocks:
        match = re.search(r"(Questão\s+\d+)", block)
        number = match.group(1) if match else "?"
        enunciado = re.split(r"[a-e]\.\s", block)[0]
        enunciado = re.sub(r"Questão\s+\d+\s*\(.*?\)", "", enunciado).strip()
        alternativas = re.findall(r"([a-e]\.)\s*(.*?)\s*(?=[a-e]\.|$)", block, re.DOTALL)

        q = {
            "question_number": number,
            "statement": enunciado,
            "options": {alt[0]: alt[1].strip() for alt in alternativas}
        }
        questions.append(q)
    return questions

def save_to_sqlite(questions, db_path="quiz_questions.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_number TEXT,
        statement TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        option_e TEXT
    )
    """)

    for q in questions:
        opts = q["options"]
        cursor.execute("""
        INSERT INTO questions (question_number, statement, option_a, option_b, option_c, option_d, option_e)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            q["question_number"],
            q["statement"],
            opts.get("a.", ""),
            opts.get("b.", ""),
            opts.get("c.", ""),
            opts.get("d.", ""),
            opts.get("e.", "")
        ))

    conn.commit()
    conn.close()