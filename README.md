# App Multi-IA 

## Descripción del proyecto

Aplicación desarrollada con Python y Gradio que integra diferentes herramientas de Inteligencia Artificial en una única interfaz interactiva.

La aplicación permite:

- Analizar el sentimiento de un texto
- Generar resúmenes automáticos
- Traducir contenido a diferentes idiomas

El objetivo del proyecto es aplicar los conocimientos aprendidos durante el módulo de IA utilizando modelos preentrenados y APIs modernas de Inteligencia Artificial.

---

## Tecnologías utilizadas

- Python
- Gradio
- HuggingFace Transformers
- Google Gemini API
- python-dotenv

### Modelos utilizados

#### Análisis de sentimiento
```python
pysentimiento/robertuito-sentiment-analysis
```

#### Resumen y traducción
```python
Gemini 1.5 Flash
```

---

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/AlexJ222/app-multi-ia.git
```

---

### 2. Entrar en la carpeta

```bash
cd app-multi-ia
```

---

### 3. Crear entorno virtual

```bash
python3 -m venv venv
```

---

### 4. Activar entorno virtual

```bash
source venv/bin/activate
```

---

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 6. Crear archivo `.env`

```env
GOOGLE_API_KEY=TU_API_KEY
```

---

## Link a la app desplegada

```bash
python3 app.py
```

---

## Link a la app desplegada

https://huggingface.co/spaces/Glacesito/app-multi-ia

## Capturas de pantalla

---

### 1. Análisis de sentimiento

<img width="1327" height="563" alt="Captura de pantalla 2026-05-11 a las 22 15 56" src="https://github.com/user-attachments/assets/0de4a800-e606-49f6-b5e9-a46400c7fc20" />

<img width="1328" height="585" alt="Captura de pantalla 2026-05-11 a las 22 16 36" src="https://github.com/user-attachments/assets/efa3a36a-8b42-4b9a-9926-fc56110a46fc" />

<img width="1279" height="555" alt="Captura de pantalla 2026-05-11 a las 22 17 04" src="https://github.com/user-attachments/assets/a1a05b9e-d52d-49d3-a16b-1849a7ce3969" />

---

### 2. Resumen

<img width="1414" height="661" alt="Captura de pantalla 2026-05-11 a las 22 30 01" src="https://github.com/user-attachments/assets/2eb931d2-152e-4a70-b0c5-2e582603be51" />

<img width="1390" height="747" alt="Captura de pantalla 2026-05-11 a las 22 31 18" src="https://github.com/user-attachments/assets/bf23e398-5a49-48cd-a783-d629cd6cbe47" />

<img width="1398" height="756" alt="Captura de pantalla 2026-05-11 a las 22 31 56" src="https://github.com/user-attachments/assets/2455903d-4804-4b43-b740-39ef0da64f5e" />


---


### 3. Traductor

<img width="1409" height="664" alt="Captura de pantalla 2026-05-11 a las 22 32 51" src="https://github.com/user-attachments/assets/c32623af-2f28-4ad6-9605-fb50c10322f6" />

<img width="1262" height="812" alt="Captura de pantalla 2026-05-11 a las 22 19 23" src="https://github.com/user-attachments/assets/ecc0038b-c3e1-4838-9258-73e94254134e" />

<img width="1417" height="660" alt="Captura de pantalla 2026-05-11 a las 22 33 48" src="https://github.com/user-attachments/assets/8b7bd632-9d91-4f3d-8419-ebecff04b6d2" />
