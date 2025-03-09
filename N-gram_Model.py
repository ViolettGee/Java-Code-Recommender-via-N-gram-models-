#initialize libraries
import numpy as np
from decimal import Decimal
import javalang
import csv
import pickle
import random
import sys

#class containing the n-gram model
class Ngram:
    
    #initialize the n-gram model with the data
    def __init__(self, n, training_data, test_data):
        self.n = n
        self.train = training_data
        self.test = test_data

        self.n_gram = self.__initialize()

    #return n_value
    def get_ngram(self):
        return(self.n_gram)
        
    #determine the probability of the n grams occurrences
    def __initialize(self, data = ''):
        #update data for if no input
        if data == '':
            data = self.train
                
        #initialize the dictionary for the probability of a token given the n with a set of data
        output = {}
        
        #iterate through the methods in the data
        for method in data:
            #iterate through the tokens in the data
            for i in range(len(method)):
                
                #check if number of tokens is greater than n
                if i > self.n:
        
                    #if n is 1 check that the empty token exists in the current dictionary
                    if self.n == 1:

                        #check if the current token exists for the empty key value
                        if '' in output:

                            #check if the token exists in the dictionary
                            if method[i] in output['']:
                                
                                #increment the number of occurrences
                                output[''][method[i]] = output[''] + 1

                            else:
                                #initialize the dictionary for the word after the sequence
                                output[''][method[i]] = 1

                    else:
                        #initialize the outer dictionary and inner dictionary
                        output[''] = {method[i] : 1}

                #check if the sequence of tokens exists in the current dictionary
                if method[(i - self.n) : (i - 1)] in output:
                
                    #check if the current token exists for the current key value
                    if method[i] in output[method[(i - self.n) : (i - 1)]]:
                        
                        #increment the number of occurrences
                        output[method[(i - self.n) : (i - 1)][method[i]] = output[method[(i - self.n) : (i - 1)]][method[i]] + 1

                    else:
                        #initialize the dictionary for the word after the sequence
                        output[method(i - self.n) : (i - 1)][method[i]] = 1

                else:
                    #initialize the outer dictionary and inner dictionary
                    output[method[(i - self.n) : (i - 1)]] = {method[i] : 1}

        return(output)

    #function for evaluating the model perplexity
    def find_perplexity(self, data = ''):
        #update data for if no input
        if data == '':
            data = self.train
            test = self.n_gram

        else:
            #initialize the dictionary for test data
            test = self.__initialize(data)

        #initialize containers
        log_prob_sum = 0
        
        #iterate through the ngram dictionary values
        for section in data.values():
            
            #sum ngram overall dictionary
            total = [x.values() for x in section]
            total_sum = sum(total)

            #iterate through the values within the ngram dictionary
            for token in section:
                
                #divide each value by that sum
                prob = token.values() / total_sum

                #compute the logarithm for that probability
                log_prob = math.log(prob)

                #sum each of the logarithms
                log_prob_sum = log_prob_sum + log_prob
        
        #divide the logarithmic sum by the negative n value
        perplexity = (log_prob_sum / (-self.n))

        #compute the e to the divisible
        perplexity = math.e(perplexity)

        #return the perplexity
        return(perplexity)
    
    #create function for predicting the next word in a sequence
    def __predict_next_word(self, sequence = ''):

        #initialize max value
        max_val = 0
        
        #look for sequence in data
        if sequence in self.n_gram:
            
            #determine most likely occurence based on n gram
            for key in self.n_gram[sequence]:
                if self.n_gram[sequence][key] > max_val:
                    max_val = self.n_gram[sequence][key]
                    word = key

        #if sequence hasn't been seen
        else:
            word = ''

        return(word)

    #function for predicting sequence based on a sequence
    def write_method(self, text):
        #tokenize the prompt
        tokens = list(javalang.tokenizer.tokenize(text))
        token_vals = [0]*len(tokens)
        for i in range(len(tokens)):
            token_vals = tokens[i].value
            
        #determine the last n tokens
        prompt = token_vals[-(self.n-1):]

        #initialize placeholders
        next_word = 'a'
        output = []
        
        #do while loop for predicting the next word until the sequence ends        
        while (next_word != ''):
            #determine the next word
            if self.n == 1:
                next_word = self.__predict_next_word()
            else:
                next_word = self.__predict_next_word(prompt)
                
                #determine the tokens of the next occurrence
                prompt.append(next_word)
                prompt = prompt[1:]

            #add words to output
            output.append(next_word)

        return(output)

#check if this file specificially is run
if __name__ == "__main__":

    #initialize containers
    test = []
    train = []
    
    #pull out the tokenized data
    with open('tokenized_data.csv', 'r', encoding = "utf-8") as file:
        
        #initialize reader object using csv module
        reader = csv.reader(file)

        for row in reader:
            row = list(row)[1:]
            
            #seperate the data into two sections: training and testing
            if random.randint(1,5) == 1:
                test.append(row)
            else:
                train.append(row)

    #save test and train data to respective files
    with open('test.csv', 'w', encoding = "utf-8", newline = '') as file:

        #initialize writer object using csv module
        writer = csv.writer(file)

        for data in test:
            writer.writerow(data)

    with open('train.csv', 'w', encoding = "utf-8", newline = '') as file:

        #initialize writer object using csv module
        writer = csv.writer(file)

        for data in train:
            writer.writerow(data)
                
    #iterate through different values of n to find the best
    best_m = []
    best_p = 99999
    
    for i in range(7):

        print(i+1)
        
        #initialize the model for that n value
        model = Ngram(i+1, train, test)
        #evaluate the model for that n value
        perplexity = model.find_perplexity()

        print(perplexity)
        
        #pick the current best n value or this n value based on the evaluation metric
        if best_p > perplexity:

            best_m = model
            best_p = perplexity

pickle.dump(best_m, open('model.pkl', 'wb'))