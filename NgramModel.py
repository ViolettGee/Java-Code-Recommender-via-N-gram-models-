#initialize libraries
from decimal import Decimal
import javalang
import csv
import math

#class containing the n-gram model
class Ngram:
    
    #initialize the n-gram model with the data
    def __init__(self, n, training_data):
        self.n = n
        self.train = training_data

        self.n_gram = self.__initialize()

    #return n_value
    def get_ngram(self):
        return(self.n)
        
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
                            if str(method[i]) in output['']:
                                
                                #increment the number of occurrences
                                output[''][str(method[i])] = output[''][str(method[i])] + 1

                            else:
                                #initialize the dictionary for the word after the sequence
                                output[''][str(method[i])] = 1

                    else:
                        #initialize the outer dictionary and inner dictionary
                        output[''] = {str(method[i]) : 1}

                #check if the sequence of tokens exists in the current dictionary
                if str(method[(i - self.n) : (i - 1)]) in output:
                
                    #check if the current token exists for the current key value
                    if str(method[i]) in output[str(method[(i - self.n) : (i - 1)])]:
                        
                        #increment the number of occurrences
                        output[str(method[(i - self.n) : (i - 1)])][str(method[i])] = output[str(method[(i - self.n) : (i - 1)])][str(method[i])] + 1

                    else:
                        #initialize the dictionary for the word after the sequence
                        output[str(method[(i - self.n) : (i - 1)])][str(method[i])] = 1

                else:
                    #initialize the outer dictionary and inner dictionary
                    output[str(method[(i - self.n) : (i - 1)])] = {str(method[i]) : 1}

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
        for section in test.values():
            
            #sum ngram overall dictionary
            total = [x for x in section.values()]
            total_sum = sum(total)

            #iterate through the values within the ngram dictionary
            for token in section.values():
                
                #divide each value by that sum
                prob = token / total_sum

                #compute the logarithm for that probability
                log_prob = math.log(prob)

                #sum each of the logarithms
                log_prob_sum = log_prob_sum + log_prob
        
        #divide the logarithmic sum by the negative n value
        perplexity = (log_prob_sum / (-self.n))

        #compute the e to the divisible
        perplexity = pow(Decimal(math.e), Decimal(perplexity))

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
        #determine the last n tokens
        prompt = text[-(self.n-1):]
        #initialize placeholders
        next_word = 'a'
        output = text
        
        #do while loop for predicting the next word until the sequence ends        
        while (next_word != ''):
            #determine the next word
            if self.n == 1:
                next_word = self.__predict_next_word()
            else:
                next_word = self.__predict_next_word(str(prompt))
                
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

        #initialize counter
        count = 0
        for row in reader:
            row = list(row)[1:]
            
            #seperate the data into two sections: training and testing
            if (count % 5) == 0:
                test.append(row)
            else:
                train.append(row)
            count = count + 1

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
