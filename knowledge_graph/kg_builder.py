"""
Creates a Neo4j graph database from biomedical entity-relation triples.
"""

from neo4j import GraphDatabase
import json

uri = "bolt://localhost:7687"
username = "neo4j"
password = "your_password"

driver = GraphDatabase.driver(uri, auth=(username, password))

def build_knowledge_graph(triples):
    with driver.session() as session:
        for head, relation, tail in triples:
            session.run(
                """
                MERGE (h:Entity {name: $head})
                MERGE (t:Entity {name: $tail})
                MERGE (h)-[r:RELATION {type: $relation}]->(t)
                """,
                head=head, tail=tail, relation=relation
            )
