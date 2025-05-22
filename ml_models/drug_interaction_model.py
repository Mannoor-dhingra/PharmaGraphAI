"""
Trains a simple traditional ML model (e.g., logistic regression) on features extracted from the knowledge graph.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_graph_features():
    # Placeholder: In practice, extract features from Neo4j and label data.
    data = pd.DataFrame({
        'feature1': [0.1, 0.3, 0.4, 0.7],
        'feature2': [1.1, 0.2, 0.9, 0.4],
        'label': [0, 1, 0, 1]
    })
    return data

def train_model():
    data = load_graph_features()
    X_train, X_test, y_train, y_test = train_test_split(data[['feature1', 'feature2']], data['label'], test_size=0.25)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))