from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42) # Splitting data into train and test
    
    model = RandomForestClassifier(n_estimators=100, random_state=42) # Building a Random Forest
    model.fit(X_train, y_train)
    
    # Model Evaluation
    predictions = model.predict(X_test)
    result = classification_report(y_test, predictions, output_dict=True)
    
    return model, result

