import csv
import javalang
import Data_Tokenization
from NgramModel import Ngram
import pandas as pd
import math


with open("Professor_Data/training.txt", 'r', encoding = "utf-8") as file:
    reader = csv.reader(file)

    with open("Professor_tokenized_data.csv", 'w', encoding = "utf-8", newline = '') as f:
        writer = csv.writer(f)
        
        for row in reader:
            method = ' '.join(list(row))
            method = Data_Tokenization.method_tokenization(method)

            for i in range(len(method)):
                if type(method[i]) == type(javalang.tokenizer.Identifier(method[i])):
                    method[i] = 'insert_identifier'
                else:
                    method[i] = method[i].value

            writer.writerow(method)

test = []
train = []

with open('Professor_tokenized_data.csv', 'r', encoding = "utf-8") as file:

    reader = csv.reader(file)

    count = 0
    for row in reader:
        row = list(row)

        if count % 5 == 0:
            test.append(row)
        else:
            train.append(row)
        count = count + 1

with open('Professor_test.csv', 'w', encoding = "utf-8", newline = '') as file:

    #initialize writer object using csv module
    writer = csv.writer(file)
    
    for data in test:
        writer.writerow(data)

with open('Professor_train.csv', 'w', encoding = "utf-8", newline = '') as file:

    #initialize writer object using csv module
    writer = csv.writer(file)

    for data in train:
        writer.writerow(data)

best_m = []
best_p = math.inf
n = 0
    
for i in range(7):
        
    #initialize the model for that n value
    model = Ngram(i+1, train)
    #evaluate the model for that n value
    perplexity = model.find_perplexity()
        
    #pick the current best n value or this n value based on the evaluation metric
    if best_p > perplexity:

        best_m = model
        best_p = perplexity
        n = i + 1

print(f"model: {n} \nperplexity: {best_p}")

df = pd.DataFrame(columns = ["Actual", "Predicted", "Accuracy"])
for i in range(len(test)):

    prompt = ' '.join(test[i])
    prompt = list(javalang.tokenizer.tokenize(prompt))

    for j in range(len(prompt)):
        prompt[j] = prompt[j].value

    trial = best_m.write_method(prompt)

    accuracy = 0
    if len(test[i]) >= len(trial):
        for x in range(len(test_data[i])):
            if (len(trial) > x):
                if (trial[x] == test[i][x]):
                    accuracy = accuracy + 1
        accuracy = accuracy / len(test[i])
    else:
        for x in range(len(trial)):
            if (len(test[i]) > x):
                if (trial[x] == test[i][x]):
                    accuracy = accuracy + 1
        accuracy = accuracy / len(trial)

    test[i] = ' '.join(test[i])
    trial = ' '.join(trial)

    df.loc[-1] = [test, trial, accuracy]
    df.index = df.index + 1
    df = df.sort_index()

    if i == 99:
        print(df)
        df.to_csv('Professor_validation_set.csv')

print(f"perplexity: {best_m.find_perplexity(test)} \naverage accuracy: {df['Accuracy'].mean()}")
