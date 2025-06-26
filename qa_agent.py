# Placeholder for qa_agent.py
from transformers import pipeline # type: ignore

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")

def answer_question(context, question):
    prompt = f"Context:\\n{context}\\n\\nQuestion: {question}\\nAnswer:"
    result = qa_pipeline(prompt, max_length=150)
    return result[0]['generated_text']