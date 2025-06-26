# Placeholder for export_utils.py
import os
from datetime import datetime

def export_qa_log(question, answer, log_dir='logs'):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    with open(os.path.join(log_dir, f"log_{timestamp}.txt"), 'w') as f:
        f.write(f"Question: {question}\\n")
        f.write(f"Answer: {answer}\\n")