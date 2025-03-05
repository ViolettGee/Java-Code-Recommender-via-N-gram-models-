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
with open('preprocessed_data.csv', 'r') as file:
    
    #initialize the reader object for the file using the csv module
    reader = csv.reader(file)
    
    #initialize the output lists
    method_names = [0]*(len(reader)-1)
    method_texts = [0]*(len(reader)-1)
    
    #iterate through the rows of the file using the reader object
    for index in range(len(reader)-1):
        
        #save the method name to the output list
        method_names[index] = reader[index+1][1]
        
        #save the tokenization from the method call to the output list
        method_texts[index] = method_tokenization(reader[index+1][2])

#call the function to write the output to a csv file
write_rows(method_names, method_texts)