import csv
import pandas as pd
import javalang
from NgramModel import Ngram

#set n to the model determination by perplexity fit
n = 7

#initialize data from test set
with open('test.csv', encoding = 'utf-8', newline = '') as f:
    reader = csv.reader(f)
    test_data = list(reader)

#initialize data from training set
with open('train.csv', encoding = 'utf-8', newline = '') as f:
    reader = csv.reader(f)
    train_data = list(reader)

#initialize N gram model
n_gram = Ngram(n, train_data)

df = pd.DataFrame(columns = ["Actual","Predicted","Accuracy"])

#iterate throught test data
for i in range(len(test_data)):
    
    #initialize current test
    test = ' '.join(test_data[i])
    test = list(javalang.tokenizer.tokenize(test))
    
    for j in range(len(test)):
        test[j] = test[j].value

    trial = n_gram.write_method(test)
    
    accuracy = 0
    if len(test_data[i]) >= len(trial):
        for x in range(len(test_data[i])):
            if (len(trial) > x):
                if (trial[x] == test_data[i][x]):
                    accuracy = accuracy + 1
        accuracy = accuracy / len(test_data[i])
    else:
        for x in range(len(trial)):
            if(len(test_data[i]) > x) and (trial[x] == test_data[i][x]):
                accuracy = accuracy + 1
        accuracy = accuracy / len(trial)

    test = ' '.join(test_data[i])
    trial = ' '.join(trial)

    df.loc[-1] = [test, trial, accuracy]
    df.index = df.index + 1
    df = df.sort_index()

    if i == 99: 
        print(df)
        df.to_csv('validation_set.csv')

print(f"perplexity: {n_gram.find_perplexity(test_data)}")
print(f"average accuracy: {df['Accuracy'].mean()}")
