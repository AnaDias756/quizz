# main.py
from utils.parser import extract_text_from_pdf, extract_questions, save_to_sqlite

pdf_path = "questions.pdf"  # Altere para o nome do seu PDF
db_path = "quiz_questions.db"

# Etapas
texto = extract_text_from_pdf(pdf_path)
questoes = extract_questions(texto)
save_to_sqlite(questoes, db_path)

print("Questões extraídas e salvas com sucesso!")
