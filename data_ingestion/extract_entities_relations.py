"""
Module to extract entities and relations from biomedical text using SciSpacy.
"""

import spacy
import json

nlp = spacy.load("en_core_sci_lg")

def extract_entities_and_relations(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    doc = nlp(text)
    triples = []
    for ent in doc.ents:
        for token in ent.subtree:
            if token.dep_ in ('prep', 'conj'):
                head = ent.text
                relation = token.text
                tail = ' '.join([t.text for t in token.subtree if t != token])
                triples.append((head, relation, tail))

    with open("data/processed/triples.json", "w") as f:
        json.dump(triples, f)
    
    return triples
