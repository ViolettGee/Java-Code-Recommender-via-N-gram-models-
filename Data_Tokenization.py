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
def write_rows(method_names, method_texts):
    
    #open the output file for the tokenization data
    with open('tokenized_data.csv', 'w') as f:
        
        #initialize the writer object for the file using the csv module
        writer = csv.writer(f, delimiter = '\t')
        
        #iterate through the methods
        for i in range(len(method_names)-1):
            
            #initialize the row of using that particular method's name and tokenized text
            row = [0]*(len(method_texts[i]) + 1)
            row[0] = method_names[i]
            for j in range(len(row)-1):
                row[j] = method_texts[i][j+1]
            
            #write to the file using the writer object
            writer.rightrow(row)
            
#main code that reads the preprocessed data and calls the above methods to tokenize the data
#open the preprocessed data file for tokenization

    #initialize the reader object for the file using the csv module

    #initialize the output lists

    #iterate through the rows of the file using the reader object

        #save the method name to the output list

        #save the tokenization from the method call to the output list

#call the data writing functio