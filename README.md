# Mango Guru AI (NLP Chatbot)
![License](https://img.shields.io/aur/license/apache-spark)
[![Follow](https://img.shields.io/github/followers/UrMango?label=Follow%20Me&style=social)](https://github.com/UrMango)
### A simple NLP AI mango bot built in python built for the Great Mango website.

This repository contains a mango chatbot built using a combination of natural language processing (NLP) techniques and machine learning. The mangobot is trained on a dataset of pre-defined intents and their corresponding patterns and tags. The chatbot is able to classify the user's input into one of the pre-defined intents, and respond with a pre-defined message corresponding to the classified intent.

## Dependencies
- **nltk (Natural Language Toolkit):** This module is used for a variety of natural language processing tasks, including tokenization (breaking up a string into individual words) and lemmatization (reducing a word to its base form).
- **numpy:** This module is used to store and manipulate the training data in the form of arrays.
- **tensorflow:** This module is used to build and train the chatbot's neural network model. It provides tools for defining the model architecture, compiling the model, and fitting the model to the training data.

## Usage
To use train and run the mangobot by yourself, run the following command:

```python
model, words, classes = initialize()
```

This will initialize the chatbot by loading the dataset, preprocessing it, and training a neural network model on it.

To classify the user's input and generate a response, run the following command:

```python
classify(model, words, classes, user_input)
```

Replace `user_input` with the desired user input. This will return the classified intent and corresponding response.

## Data
The chatbot is trained on the `intents.json` file, which contains a list of pre-defined intents. Each intent consists of a list of patterns and a tag. The patterns are used to train the chatbot to classify user inputs into the corresponding intent, while the tag is used to determine the response to generate for each intent.

## Model
The chatbot uses a neural network model with three dense layers and dropout layers in between to classify user inputs into the pre-defined intents. The model is trained using the Adam optimization algorithm and categorical cross-entropy loss. The accuracy of the model is also tracked during training.
