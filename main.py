"""
PharmGraphIQ: A knowledge-graph enhanced drug interaction risk predictor combining GenAI and ML.
Entrypoint for the project pipeline.
"""

from data_ingestion.extract_entities_relations import extract_entities_and_relations
from knowledge_graph.kg_builder import build_knowledge_graph
from genai_module.graph_qna_pipeline import answer_query_with_graph
from ml_models.drug_interaction_model import train_model
from app import launch_ui


def main():
    print("[Step 1] Extracting entities and relations from biomedical documents...")
    triples = extract_entities_and_relations("data/raw/pubmed_sample.txt")

    print("[Step 2] Building knowledge graph in Neo4j...")
    build_knowledge_graph(triples)

    print("[Step 3] Training machine learning model on graph-based features...")
    train_model()

    print("[Step 4] Launching Streamlit UI for GenAI QnA...")
    launch_ui()


if __name__ == "__main__":
    main()
