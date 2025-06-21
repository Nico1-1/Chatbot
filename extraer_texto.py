import fitz  # PyMuPDF
import pickle
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Ruta absoluta del archivo PDF
RUTA_PDF = "/Users/nicorivera/Documents/GitHub/1/1-s2.0-S2529912319300658-main.pdf"

# Paso 1: Extraer texto del PDF
def extraer_texto_pdf(ruta):
    doc = fitz.open(ruta)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

# Paso 2: Dividir el texto en fragmentos solapados
def dividir_en_chunks(texto, tamano=500, solapamiento=100):
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano
        chunk = texto[inicio:fin]
        chunks.append(chunk)
        inicio += tamano - solapamiento
    return chunks

# Paso 3: Crear vectores de embedding para los fragmentos
def crear_embeddings(fragmentos, modelo):
    return modelo.encode(fragmentos)

# Paso 4: Crear índice FAISS
def crear_indice_faiss(vectores):
    dim = len(vectores[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectores, dtype='float32'))
    return index

# Ejecutar el proceso completo
def preparar_chatbot():
    print("✅ Extrayendo texto del PDF...")
    texto = extraer_texto_pdf(RUTA_PDF)
    print("✅ Dividiendo en fragmentos...")
    fragmentos = dividir_en_chunks(texto)

    print("✅ Cargando modelo de embeddings...")
    modelo = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ Generando embeddings...")
    vectores = crear_embeddings(fragmentos, modelo)

    print("✅ Creando índice FAISS...")
    index = crear_indice_faiss(vectores)

    # Guardar resultados
    with open("fragmentos.pkl", "wb") as f:
        pickle.dump(fragmentos, f)
    faiss.write_index(index, "indice.faiss")
    print("✅ Archivos guardados correctamente: fragmentos.pkl, indice.faiss")

if __name__ == "__main__":
    preparar_chatbot()
