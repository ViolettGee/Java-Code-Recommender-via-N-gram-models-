#initialize the necessary imports
import javalang
import csv

#function that tokenizes methods
def method_tokenization(text):
    
    #create tokens using javalang library
    try:
        tokens = list(javalang.tokenizer.tokenize(text))
    except:
        return('')

    #return tokens in list format    
    return(tokens)

#function that writes to an output csv the tokenization data
def write_rows(method_names, method_texts):
    
    #open the output file for the tokenization data
    with open('tokenized_data.csv', 'w', encoding = "utf-8", newline = '') as f:
        
        #initialize the writer object for the file using the csv module
        writer = csv.writer(f)
        
        #iterate through the methods
        for i in range(len(method_names)-1):
            
            #initialize the row of using that particular method's name and tokenized text
            row = [0]
            row[0] = method_names[i+1]
            for token in method_texts[i+1]:
                row.append(token.value)
            
            #write to the file using the writer object
            writer.writerow(row)
            
#main code that reads the preprocessed data and calls the above methods to tokenize the data
#open the preprocessed data file for tokenization
with open('preprocessed_data.csv', 'r', encoding = "utf-8") as file:
    
    #initialize the reader object for the file using the csv module
    reader = csv.reader(file)
    
    #initialize the output lists
    method_names = []
    method_texts = []
    
    #iterate through the rows of the file using the reader object
    for row in reader:
        
        #save the tokenization from the method call to the output list
        text = method_tokenization(row[2])
        if not (text == ''):
            method_texts.append(method_tokenization(row[2]))
        else:
            continue

        #save the method name to the output list
        method_names.append(row[1])
        
#call the function to write the output to a csv file
write_rows(method_names, method_texts)