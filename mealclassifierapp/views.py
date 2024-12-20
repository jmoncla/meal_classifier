import os

import pandas as pd
from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from meal_classifier2.settings import BASE_DIR


# Train the model and vectorizer once
def train_model():
    # Read CSV file
    file_path = os.path.join(BASE_DIR, 'mealclassifierapp', 'data', 'meal_data.csv')
    data = pd.read_csv(file_path)  # Adjust path as needed
    descriptions = data['description']
    labels = data['category']

    # Vectorize data
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(descriptions)

    # Train a model
    model = MultinomialNB()
    model.fit(X, labels)

    return model, vectorizer

# Load model and vectorizer globally
model, vectorizer = train_model()

# View for displaying the form page
def form_page(request):
    github_repo_url =  "https://github.com/jmoncla/meal_classifier.git"
    return render(request, 'mealclassifierapp/form_page.html', {'github_repo_url': github_repo_url})

# View for processing input and displaying prediction
def predict_meal(request):
    prediction = None
    if request.method == 'POST':
        # Get user input from the form
        user_input = request.POST.get('meal_input', '')

        if user_input:
            # Vectorize the input
            input_vector = vectorizer.transform([user_input])
            # Make a prediction
            prediction = model.predict(input_vector)[0]

    return render(request, 'mealclassifierapp/result_page.html', {'prediction': prediction})
