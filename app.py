"""
Streamlit UI for querying the knowledge graph using GenAI.
"""

import streamlit as st
from genai_module.graph_qna_pipeline import answer_query_with_graph

def launch_ui():
    st.set_page_config(page_title="PharmGraphIQ - Drug Risk Advisor")
    st.title("💊 PharmGraphIQ: AI-driven Drug Interaction Risk Advisor")

    question = st.text_input("Enter your biomedical question:")

    if st.button("Ask") and question:
        with st.spinner("Querying Neo4j and LLaMA..."):
            answer = answer_query_with_graph(question)
        st.success("Answer:")
        st.write(answer)