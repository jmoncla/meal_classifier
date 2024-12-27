 Meal Classifier

## Overview
This project is built with Django, and is hosted by Heroku and serves as a demonstration of a machine learning model that can process text input and return a classification. 
Below you will find links to key components of the project, including visuals, accuracy scores, and main application logic.

---

## Clickable Links

- [VISUALS](#visuals)
- [ACCURACY SCORE](#accuracy-score)
- [MAIN APPLICATION LOGIC](#main-application-logic)

---

## VISUALS
![Confusion Matrix](path/to/confusion_matrix.png)

This section contains a visual representation of the confusion matrix generated by the application. It highlights the accuracy and precision of the classification model.

---

## ACCURACY SCORE

The accuracy score of the machine learning model is calculated using the `accuracy_score` function from `sklearn.metrics`. Below is a snippet of the relevant code:

```python
accuracy = accuracy_score(labels, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
```

For more details, view the complete metrics in [metrics.py](path/to/metrics.py).

---

## MAIN APPLICATION LOGIC

The main application logic involves training the model and vectorizing text data using the following key functions:

```python
def train_model():
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(descriptions)

    model = MultinomialNB()
    model.fit(X, labels)

    return model, vectorizer
```

To review the full application logic, visit the [main logic file](path/to/main_logic.py)
