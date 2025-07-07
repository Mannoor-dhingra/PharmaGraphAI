"""
Uses FireworksAI's LLaMA model to answer biomedical questions using the Neo4j knowledge graph.
"""

from langchain_fireworks import ChatFireworks
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_neo4j import Neo4jGraph

# Setup Neo4j Graph
graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="password"
)

llm= ChatFireworks(model="accounts/fireworks/models/llama-v3p1-8b-instruct", temperature=0)

prompt_template="""
    Context: {context}
    Question: {question}
    Answer:
    """


prompt=PromptTemplate.from_template(prompt_template)

chain = prompt | llm | StrOutputParser()

def answer_query_with_graph(question):
    context = graph.query("MATCH (n)-[r]->(m) RETURN n.name, type(r), m.name LIMIT 10")
    flat_context = "; ".join([f"{n} -[{r}]-> {m}" for n, r, m in context])
    return chain.invoke({"context": flat_context, "question": question})