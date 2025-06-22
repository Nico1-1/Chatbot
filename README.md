🤖 Chatbot Académico sobre Sedentarismo

Este repositorio contiene un chatbot personalizado desarrollado como parte de una actividad práctica universitaria. El objetivo fue construir un asistente virtual capaz de responder preguntas sobre un artículo científico en español, relacionado con los efectos del sedentarismo en la salud.

📄 Documento base

El chatbot se entrenó con el artículo:
> López-Valenciano, A., Mayo, X., & Casajús, J.A. (2019). *Conducta sedentaria: Definición, prevalencia, riesgos y estrategias de intervención*. **Clínica e Investigación en Arteriosclerosis, 31(5)**, 233–240.  
Disponible en: [Elsevier](https://www.sciencedirect.com/science/article/pii/S2529912319300658)


🧠 ¿Qué hace este chatbot?

Este chatbot responde a preguntas en español utilizando como contexto fragmentos relevantes del artículo mencionado. Su comportamiento está personalizado para actuar como tutor académico, respondiendo de forma clara, directa y con base en el contenido real del PDF.

Características destacadas:

- 🗂️ Utiliza `FAISS` para recuperar los fragmentos más similares a la pregunta.
- 🔍 Genera embeddings con `sentence-transformers`.
- 🧠 Responde con el modelo Deepseek Instruct usando Ollama.
- 🇪🇸 Diseñado para interactuar en español.
- 🎓 Ajustado para comportarse como asistente académico.

🛠️ Requisitos

- Python 3.10 o superior
- Ollama instalado: https://ollama.com/
- Modelo Deepseek Instruct instalado:  
  ```bash
  ollama run deepseek-coder:6.7b-instruct
Bibliotecas Python necesarias:
pip install -r requirements.txt

Contenido sugerido para requirements.txt:

faiss-cpu
sentence-transformers
numpy
PyPDF2

📁 Archivos importantes

Archivo	Descripción
extraer_texto.py	Procesa el PDF, genera fragmentos y los embeddings con FAISS.
chatbot.py	Carga el índice FAISS y responde preguntas usando Ollama.
1-s2.0-S2529912319300658-main.pdf	Artículo original en PDF usado como base de conocimiento.
fragmentos.pkl	Fragmentos del PDF tokenizados y almacenados para recuperación.
indice.faiss	Índice de búsqueda para recuperar contenido relevante.

¿Cómo ejecutar el chatbot?

Clona el repositorio:
git clone https://github.com/Nico1-1/Chatbot.git
cd Chatbot
Crea y activa un entorno virtual:
python -m venv mi_entorno
source mi_entorno/bin/activate  # En Windows: mi_entorno\Scripts\activate
Instala las dependencias:
pip install -r requirements.txt
Descarga e instala el modelo en Ollama:
ollama run deepseek-coder:6.7b-instruct
Procesa el PDF (solo la primera vez):
python extraer_texto.py
Ejecuta el chatbot:
python chatbot.py

Ejemplo de uso

❓ Haz tu pregunta sobre el PDF: ¿Qué es el sedentarismo?
💬 Respuesta del chatbot:
El sedentarismo se refiere a un estilo de vida con bajos niveles de movimiento físico...

Sobre este proyecto

Este proyecto fue realizado como parte de una actividad práctica de la asignatura de Inteligencia Artificial aplicada a documentos académicos, donde se solicitó crear un chatbot personalizado que simulara el comportamiento de un tutor o asistente académico en un tema específico.




