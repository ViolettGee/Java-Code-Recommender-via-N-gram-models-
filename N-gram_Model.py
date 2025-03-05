#initialize libraries
import math
import javalang
import csv
import pickle

#class containing the n-gram model
class Ngram:
    
    #initialize the n-gram model with the data
    def __init__(self, n, training_data, test_data):
        self.n = n
        self.train = training_data
        self.test = test_data

        self.n_gram = self.__initiailize()

    #return n_value
    def get_n(self):
        return(self.n)
        
    #determine the probability of the n grams occurrences
    def __initialize(self, data = self.train):
        
        #initialize dictionary for the count of the given occurrences
        dict_given = {}
        
        #initialize the dictionary for the probability of a token given the n with a set of data
        output = {}
        
        #iterate through the methods in the data
        total = 0
        for method in data:
            #iterate through the tokens in the data
            for i in range(len(method)):

                #check if n is 1
                if self.n == 1:
                    #check if the token exists in the dictionary
                    if str(method[i]) in output:
                        output[method[i]] = outpu[method[i]] + 1
                    else:
                        output[method[i]] = 1
                    
                    dict_given = {"this":0}
                    total = total + 1

                else:
                    #check if the number of tokens is greater than n
                    if (i+1) >= self.n:
                        
                        #check if the sequence of tokens exists
                        if str(method[(i-self.n):i]) in dict_given:
                            #increment the number of occurrences
                            dict_given[str(method[(i-self.n)])] = dict_given[str(method[(i-self.n)])]

                            #check if the sequence of tokens n exists **ending should be its own occurence as well
                            if str(method[i]) in output[str(method[(i-self.n):i])]:
                                #increment the number of occurrences
                                output[str(method[(i-self.n):i])][method[i]] = output[str(method[(i-self.n):i])][method[i]] + 1
                                
                            else:
                                #initialize the occurence of the sequence of tokens n exists
                                output[str(method[(i-self.n):i])][method[i]] = 1
                        else:
                            #initialize the occurences of the sequence of tokens n exists
                            dict_given[str(method[(i-self.n):i])] = 1
                            output[str(method[(i-self.n):i])] = {method[i]:1}

                        total = total + 1

        #iterate through keys in the occurrence count dictionary
        for occurrence in dict_given:
            #iterate through keys in the conditional count dictionary
            for conditional in output:
                    
                #check if n equals 1
                if self.n == 1:
                        
                    #divide each of the values by the total
                    output[conditional] = output[conditional]/total

                else:
                    
                    #divide occurences by total
                    dict_given[occurrence] = dict_given[occurrence]/total
                    #divide conditional by total
                    output[occurrence][conditional] = output[occurrence][conditional]/total

                    #divide condtional by the occurences
                    output[occurrence][conditional] = output[occurrence][conditional]/dict_given[occurrence]

        return(output)

    #function for evaluating the model perplexity
    def find_perplexity(self, data = self.test):
        
        #initialize the dictionary for test data
        test = self.__initialize(data)

        product = 1
        summation = 0
        #iterate through the dictionary
        for value in test.values:
            
            #check if n is equal to 1
            if self.n == 1:
                #product each probability
                product = value * product
                #sum the number of probabilities
                summation = value + summation

            else:
                #iterate through the iternal dictionary
                for val in value.value:
                    
                    #product each probability
                    product = val * product
                    #sum the number of probabilities
                    summation = val + summation

        #inverse the product
        product = 1/product
        #exponent of the product by the sum
        perplexity = math.pow(product, (1/summation))

        #return the perplexity
        return(perplexity)
    
    #create function for predicting the next word in a sequence
    def __predict_next_word(self, sequence = ''):

        #initialize max value
        max_val = 0
        
        #check if n equals 1
        if self.n == 1:
            for key in self.n_gram:
                if self.n_gram[key] > max_val:
                    max_val = self.n_gram[key]
                    word = key
        
        #look for sequence in data
        elif sequence in self.n_gram:
            
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
            if random.randint(1,10) == 1,2:
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
        
        #initialize the model for that n value
        model = Ngram(i, train, test)
        #evaluate the model for that n value
        perplexity = model.find_perplexity()
        
        #pick the current best n value or this n value based on the evaluation metric
        if best_p > perplexity:

            best_m = model
            best_p = perplexity

with open('model.pkl', 'w') as file:
    pickle.dump(model, file)