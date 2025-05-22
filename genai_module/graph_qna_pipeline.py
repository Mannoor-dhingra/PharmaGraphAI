"""
Uses FireworksAI's LLaMA model to answer biomedical questions using the Neo4j knowledge graph.
"""

from langchain.llms import Fireworks
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.graphs.neo4j_graph import Neo4jGraph

# Setup Neo4j Graph
graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="your_password"
)

# LLM setup
llm = Fireworks(model="accounts/fireworks/models/llama-v2-13b-chat")

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Context: {context}
    Question: {question}
    Answer:
    """
)

chain = LLMChain(llm=llm, prompt=prompt)

def answer_query_with_graph(question):
    context = graph.query("MATCH (n)-[r]->(m) RETURN n.name, type(r), m.name LIMIT 10")
    flat_context = "; ".join([f"{n} -[{r}]-> {m}" for n, r, m in context])
    return chain.run({"context": flat_context, "question": question})
