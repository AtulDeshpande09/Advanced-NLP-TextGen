import json
import random
import ast

# tokenize method
def tokenize(sentence:str):
    sentence = sentence.lower()
    tokens = sentence.split()

    return tokens



# Import Ngrams with probabilities
with open("/home/atul/projects/Advanced-NLP-TextGen/models/ngram.json","r") as file:
    data = json.load(file)

# function to store it in dictionary , the keys have tuple data type
def load_ngrams():
    new_probability = {}
    
    for key ,value in data.items():
        new_key = ast.literal_eval(key)

        new_probability[new_key] = value
    
    return new_probability

# Load data 
new_probability = load_ngrams()

# Predict next word based on the last word
def predict_next_word(sentence:str):

    last_word = tokenize(sentence)[-1]

    selected_sequence_list = [(sequence,new_probability[sequence]) for sequence in new_probability if sequence[0]==last_word]
    sequence_list = [ p[0] for p in selected_sequence_list]
    probability_list = [ p[1] for p in selected_sequence_list]

    next_word = random.choices(sequence_list,weights = probability_list)[0][1]
    
    return next_word

# Generate Sentence
def generate_sentences(number_of_sentences : int):
    sentence = []
    
    for _ in range(number_of_sentences) :

        word = "<s>"
        
        while word != "</s>":
            if word == "</s>" or word =="<s>":
                sentence.append(".")
                word = predict_next_word(word)
            else:
                sentence.append(word)
                word = predict_next_word(word)
    del sentence[0]
    response = " ".join(sentence)
    return response


sentence = generate_sentences(4)
print(sentence)
