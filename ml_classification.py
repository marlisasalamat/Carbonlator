import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

def ml_classification():
    # Load the data
    data = pd.read_csv('data.csv')
    X = data[['Energy Efficiency Rating (E)', 'Resource Consumption (E)',
              'Data Center Location (E)', 'Maintenance Cost (C)',
              'Obsolete Functionality (U)', 'Redundancy (U)', 'Low Usage (U)',
              'User Impact (C)', 'Business Value (C)',
              'Compliance and Regulatory (U)']]
    y = data['TARGET']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train the model
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    # Save the model as a pickle file
    with open('knn_model.pkl', 'wb') as file:
        pickle.dump(model, file)

    # Save the scaler as a pickle file
    with open('scaler.pkl', 'wb') as file:
        pickle.dump(scaler, file)

    return accuracy, report, matrix, y_test, y_pred
