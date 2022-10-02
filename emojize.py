
import numpy as np
import os
import csv
import urllib.request
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer

# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary

mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/emoji/mapping.txt"

class Emojize:
    def __init__(self, model):
        self.model = AutoModelForSequenceClassification.from_pretrained(model)
        self.tokenizer = AutoTokenizer.from_pretrained(model)

        if not os.path.isdir("cardiffnlp"):
            self.model.save_pretrained(model)
            self.tokenizer.save_pretrained(model)
            
        self.labels=[]

        with urllib.request.urlopen(mapping_link) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')

        self.labels = [row[1] for row in csvreader if len(row) > 1]

    def emojize(self, text):
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        rankings = np.argsort(scores)[::-1]
        ret = ""
        for i in range(2):
            ret += self.labels[rankings[i]]
        return ret



if __name__ == "__main__":
    emojizer = Emojize("cardiffnlp/twitter-roberta-base-emoji")
    print(emojizer.emojize("deal deal"))


