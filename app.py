import os
import gradio as gr
from transformers import pipeline
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv(dotenv_path=".env")
print(os.listdir())
print("ENV EXISTE:", os.path.exists(".env"))
print("API:", os.getenv("GOOGLE_API_KEY"))

api_key = os.getenv("GOOGLE_API_KEY")


if not api_key:
    raise ValueError("No se ha encontrado GOOGLE_API_KEY. Revisa el archivo .env")

genai.configure(api_key=api_key)

modelo_gemini = genai.GenerativeModel("gemini-2.5-flash")


# =========================
# 1. ANALIZADOR DE SENTIMIENTO
# =========================

clasificador_sentimiento = pipeline("sentiment-analysis")

def analizar_sentimiento(texto: str):
    if not texto.strip():
        return "Introduce un texto para analizar."

    resultado = clasificador_sentimiento(texto)[0]

    etiqueta = resultado["label"]
    confianza = round(resultado["score"] * 100, 2)

    return f"Resultado: {etiqueta}\nConfianza: {confianza}%"


# =========================
# 2. RESUMIDOR CON GEMINI
# =========================

def resumir_texto(texto: str, nivel: str):

    if not texto.strip():
        return "Introduce un texto para resumir."

    # Configuración según nivel
    if nivel == "Corto":
        instrucciones = """
        Haz un resumen MUY breve.
        Máximo 3-4 líneas.
        Solo las ideas más importantes.
        """

    elif nivel == "Medio":
        instrucciones = """
        Haz un resumen equilibrado.
        Explica las ideas principales de forma clara.
        """

    else:  # Detallado
        instrucciones = """
        Haz un resumen detallado y académico.
        Conserva conceptos importantes, ejemplos e ideas secundarias relevantes.
        """

    prompt = f"""
    {instrucciones}

    Texto:
    {texto}
    """

    respuesta = modelo_gemini.generate_content(prompt)

    return respuesta.text


# =========================
# 3. TRADUCTOR CON GEMINI
# =========================

def traducir_texto(texto: str, idioma_destino: str):
    if not texto.strip():
        return "Introduce un texto para traducir."

    prompt = f"""
    Traduce el siguiente texto al idioma {idioma_destino}.
    Devuelve únicamente la traducción.

    Texto:
    {texto}
    """

    respuesta = modelo_gemini.generate_content(prompt)
    return respuesta.text


# =========================
# INTERFAZ GRADIO CON TABS
# =========================

with gr.Blocks(title="App Multi-IA") as app:

    gr.Markdown("# App Multi-IA con HuggingFace y Gemini")
    gr.Markdown(
        "Esta aplicación permite analizar sentimiento, resumir textos y traducir contenido usando IA."
    )

    with gr.Tab("Análisis de Sentimiento"):
        entrada_sentimiento = gr.Textbox(
            label="Texto a analizar",
            placeholder="Escribe una reseña, comentario o frase..."
        )

        salida_sentimiento = gr.Textbox(
            label="Resultado"
        )

        boton_sentimiento = gr.Button("Analizar sentimiento")

        boton_sentimiento.click(
            fn=analizar_sentimiento,
            inputs=entrada_sentimiento,
            outputs=salida_sentimiento
        )

    with gr.Tab("Resumen de Texto"):
        entrada_resumen = gr.Textbox(
            label="Texto largo",
            placeholder="Pega aquí el texto que quieres resumir...",
            lines=8
        )

        nivel_resumen = gr.Radio(
            choices=["Corto", "Medio", "Detallado"],
            value="Medio",
            label="Nivel de resumen"
        )

        salida_resumen = gr.Textbox(
            label="Resumen",
            lines=6
        )

        boton_resumen = gr.Button("Generar resumen")

        boton_resumen.click(
            fn=resumir_texto,
            inputs=[entrada_resumen, nivel_resumen],
            outputs=salida_resumen
        )


    with gr.Tab("Traducción"):
        entrada_traduccion = gr.Textbox(
            label="Texto a traducir",
            placeholder="Escribe el texto que quieres traducir...",
            lines=5
        )

        idioma = gr.Dropdown(
            choices=["inglés", "español", "francés", "alemán", "italiano", "portugués"],
            value="inglés",
            label="Idioma destino"
        )

        salida_traduccion = gr.Textbox(
            label="Traducción",
            lines=5
        )

        boton_traduccion = gr.Button("Traducir")

        boton_traduccion.click(
            fn=traducir_texto,
            inputs=[entrada_traduccion, idioma],
            outputs=salida_traduccion
        )


# =========================
# LANZAR APP
# =========================

app.launch(share=True)
