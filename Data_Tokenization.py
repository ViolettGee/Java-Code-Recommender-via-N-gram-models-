#initialize the necessary imports
import javalang
import csv

#function that tokenizes methods
def method_tokenization(text):
    
    #create tokens using javalang library
    tokens = list(javalang.tokenizer.tokenize(text))
    
    #return tokens in list format
    return(tokens)

#function that writes to an output csv the tokenization data

    #open the output file for the tokenization data

        #initialize the writer object for the file using the csv module

        #iterate through the methods

            #initialize the row of using that particular method's name and tokenized text

            #write to the file using the writer object

#main code that reads the preprocessed data and calls the above methods to tokenize the data
