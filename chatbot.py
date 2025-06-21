import subprocess
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os

# Configuración inicial
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Cargar los fragmentos de texto y el índice FAISS
with open("fragmentos.pkl", "rb") as f:
    fragmentos = pickle.load(f)

index = faiss.read_index("indice.faiss")
modelo = SentenceTransformer("all-MiniLM-L6-v2")

def buscar_similaridad(index, embedding_pregunta, k=3):
    embedding_pregunta = np.array(embedding_pregunta, dtype="float32").reshape(1, -1)
    distancias, indices = index.search(embedding_pregunta, k)
    return [fragmentos[i] for i in indices[0]]

def consultar_ollama(pregunta, contexto):
    prompt = f"""
Eres un asistente académico. Usa el siguiente contexto extraído de un artículo científico para responder con precisión.
Si la pregunta está en español, responde en español.

Contexto:
{contexto}

---

Usuario: {pregunta}
Asistente:"""

    resultado = subprocess.run(
        ["ollama", "run", "deepseek-coder:6.7b-instruct"],
        input=prompt.encode(),
        capture_output=True
    )
    print("\n💬 Respuesta del chatbot:\n")
    print(resultado.stdout.decode())

def main():
    print("✅ Todo cargado. Listo para preguntar.")
    pregunta = input("❓ Haz tu pregunta sobre el PDF: ")
    print("📝 Enviando el siguiente prompt a Ollama...")
    embedding_pregunta = modelo.encode([pregunta])[0]
    fragmentos_relevantes = buscar_similaridad(index, embedding_pregunta)
    contexto = "\n---\n".join(fragmentos_relevantes)
    consultar_ollama(pregunta, contexto)

if __name__ == "__main__":
    main()