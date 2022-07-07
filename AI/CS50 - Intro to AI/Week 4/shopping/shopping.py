import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size = TEST_SIZE
    )
    
    models = {"nn", "knn", "svm", "pct"}
    
    for model in models:
        # Train model and make predictions
        if model == "nn":
            model = train_model(X_train, y_train)
        elif model == "knn":
            model = train_model_knn(X_train, y_train)
        elif model == "svm":
            model = train_model_svm(X_train, y_train)
        else:
            model = train_model_pct(X_train, y_train)
    
        predictions = model.predict(X_test)
        sensitivity, specificity = evaluate(y_test, predictions)
    
        # Print results
        print(f"Results for model {type(model).__name__}")
        print(f"Correct: {(y_test == predictions).sum()}")
        print(f"Incorrect: {(y_test != predictions).sum()}")
        print(f"Accuracy: {100 * ((y_test == predictions).sum() / ((y_test == predictions).sum() + (y_test != predictions).sum())):.2f}%")
        print(f"True Positive Rate: {100 * sensitivity:.2f}%")
        print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - 0 Administrative, an integer
        - 1 Administrative_Duration, a floating point number
        - 2 Informational, an integer
        - 3 Informational_Duration, a floating point number
        - 4 ProductRelated, an integer
        - 5 ProductRelated_Duration, a floating point number
        - 6 BounceRates, a floating point number
        - 7 ExitRates, a floating point number
        - 8 PageValues, a floating point number
        - 9 SpecialDay, a floating point number
        - 10 Month, an index from 0 (January) to 11 (December)
        - 11 OperatingSystems, an integer
        - 12 Browser, an integer
        - 13 Region, an integer
        - 14 TrafficType, an integer
        - 15 VisitorType, an integer 0 (not returning) or 1 (returning)
        - 16 Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        
        data = []
        for row in reader:
            data.append({
                "evidence": [
                    int(row[0]), 
                    float(row[1]), 
                    int(row[2]),
                    float(row[3]), 
                    int(row[4]),
                    float(row[5]),
                    float(row[6]),
                    float(row[7]),
                    float(row[8]),
                    float(row[9]),
                    0 if row[10] == "Jan" else 1 if row[10] == "Feb" else 2 if row[10] == "Mar" else 3 if row[10] == "Apr" else 4 if row[10] == "May" else 5 if row[10] == "Jun" else 6 if row[10] == "Jul" else 7 if row[10] == "Aug" else 8 if row[10] == "Sep" else 9 if row[10] == "Oct" else 10 if row[10] == "Nov" else 11,
                    int(row[11]),
                    int(row[12]),
                    int(row[13]),
                    int(row[14]),
                    1 if row[15] == "Returning_Visitor" else 0,
                    1 if row[16] == "TRUE" else 0
                ],
                "label": 1 if row[17] == "TRUE" else 0
            })
        
        return ([row["evidence"] for row in data], [row["label"] for row in data])


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors = 1)
    
    model.fit(evidence, labels)
    
    return model

def train_model_knn(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=5) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors = 5)
    
    model.fit(evidence, labels)
    
    return model

def train_model_svm(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=5) trained on the data.
    """
    model = SVC()
    
    model.fit(evidence, labels)
    
    return model

def train_model_pct(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=5) trained on the data.
    """
    model = Perceptron()
    
    model.fit(evidence, labels)
    
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    actual_positive = 0
    actual_positive_correct = 0
    actual_negative = 0
    actual_negative_correct = 0
    
    for row in range(len(labels)):
        if labels[row] == 1:
            actual_positive += 1
            if predictions[row] == 1:
                actual_positive_correct += 1
        else:
            actual_negative += 1
            if predictions[row] == 0:
                actual_negative_correct += 1
    
    sensitivity = actual_positive_correct / actual_positive
    specificity = actual_negative_correct / actual_negative
    
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
