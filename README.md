# Multi-Model Recipe Bot

## Overview
This project is a Multi-Model Recipe Bot built using **LangChain** and **Streamlit**. It generates structured JSON recipes using multiple LLMs, including **Google Gemini** and **Groq**.

Users can enter a recipe topic or ingredients, select a model, and view the structured recipe output. The app also allows **comparing Gemini vs Groq** outputs with timing information.

---

## Features
- Input any recipe topic or ingredients
- Select between **Google Gemini** or **Groq**
- Generate structured recipe JSON:
  - `recipe_name`
  - `ingredients`
  - `steps`
  - `cooking_time`
  - `difficulty_level`
  - `nutrition_facts` 

---

## Model Comparison

**What I learned:**  
- Google Gemini is fast and fluent but struggles with **nested dictionary fields** like `nutrition_facts`.
- Groq is slightly slower but consistently generates complete structured JSON, including nested dictionaries.

**Performance:**  
| Model          | Strengths                            | Limitations                     |
|----------------|-------------------------------------|--------------------------------|
| Groq           | Reliable structured JSON output      | Slightly slower                 |
| Google Gemini  | Fast, fluent language generation     | Nested dictionaries often empty |

**Conclusion:**  
For tasks requiring strict JSON output, especially with nested structures, **Groq performs better**. Gemini is better suited for simpler or flattened fields.

---

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <project-folder>

2. Create a virtual environment (recommended):

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Upgrade pip
pip install --upgrade pip

4.Install dependencies

All required packages are listed in requirements.txt:

pip install -r requirements.txt

Packages included:

# Core packages
streamlit
python-dotenv
pydantic

# LangChain packages
langchain
langchain-core
langchain-google-genai
langchain-groq


5. Set up environment variables

Create a .env file in the project folder and add your API keys:

GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key

6. Run the Streamlit app

streamlit run app.py

