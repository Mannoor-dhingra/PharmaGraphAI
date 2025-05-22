# 💊 PharmaGraphAI: Knowledge Graph-Enhanced Drug Interaction Risk Predictor

PharmaGraphAI is an AI-powered pipeline that combines the interpretability of knowledge graphs with the reasoning capabilities of Generative AI (FireworksAI LLaMA models) and the precision of traditional machine learning. The goal: **to identify and predict potentially dangerous drug interactions** using structured biomedical data.

## 🚀 Project Highlights

- 🧠 **Entity & Relationship Extraction** from biomedical datasets
- 🔗 **Knowledge Graph Construction** using Neo4j
- 📊 **Risk Prediction Engine** trained on labeled drug interaction data
- 🤖 **Generative AI Layer** (LLaMA) for reasoning and natural language explanation
- 🌐 **Interactive Frontend** built with Streamlit for clinicians and researchers

## 🗂️ Project Structure

```
PharmaGraphAI/
├── data/
│ ├── sample_data.csv
├── data_ingestion/
│ ├── extract_entities_relations.py # Extracts biomedical triples
├── genai_module/
│ ├── graph_qna_pipeline.py # Uses FireworksAI LLaMA to answer questions
├── knowledge_graph/
│ ├── kg_builder.py # Builds graph in Neo4j
├── ml_models/
│ ├── drug_interaction_model.py # ML-based risk predictor
├── .env
├── app.py # Streamlit app
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PharmaGraphAI.git
cd PharmaGraphAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Neo4j (ensure it's running on bolt://localhost:7687) and update credentials in kg_builder.py if needed.

4. Get access to FireworksAI and set your API key in environment variables or within .env file.

## 🧠 Technologies Used

- Neo4j – Graph DB for modeling drug interactions
- FireworksAI (LLaMA) – Natural language reasoning & explanations
- Scikit-learn – Traditional ML models (XGBoost, RandomForest)
- Streamlit – UI for interaction and decision support
- SciSpacy – Biomedical NER

