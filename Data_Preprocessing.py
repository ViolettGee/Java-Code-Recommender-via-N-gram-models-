#import necessary libraries
from pathlib import Path
import pandas as pd
import javalang
import re

#function that removes duplicates from the data
def remove_duplicates(data):

    #removes verbatim duplicates from the data
    return data.drop_duplicates(keep = "first")
    
#function that removes all none ASCII characters
def filter_ascii_methods(data):

    #searches column and removes non ASCII characters
    data = data[data["Method Text"].apply(lambda x: all(ord(char) < 128 for char in x))]
    data = data[data["Method Names"].apply(lambda x: all(ord(char) < 128 for char in x))]

    return data
    
#function that removes outlier methods
def remove_outliers(data, lower_percentile = 5, upper_percentile = 95):

    #determine the method lengths of a column
    method_lengths = data["Method Text"].apply(len)
    
    #calculate lower and upper bounds
    lower_bound = method_lengths.quantile(lower_percentile / 100)
    upper_bound = method_lengths.quantile(upper_percentile / 100)
    
    #filters out all methods not within the calculated bounds
    return data[(method_lengths >= lower_bound) & (method_lengths <= upper_bound)]
    
#function that removes boilerplate patterns
def remove_boilerplate_methods(data):

    #initialize regex string
    boilerplate_patterns = [ r"\bset[A-Z][a-zA-Z0-9_]*\(.*\)\s*{",
                             r"\bget[A-Z][a-zA-Z0-9_]*\(.*\)\s*{", ]
    boilerplate_regex = re.compile("|".join(boilerplate_patterns))
    
    #removes sections of text that apply to the regex string
    data = data[~data["Method Text"].apply(lambda x: bool(boilerplate_regex.search(x)))]

    return data
    
#function that removes comments from methods
def remove_comments(data):

    #initialize regex string
    comment_patterns = [ r"//.*$", r"/\*[\s\S]*?\*/", r"//.*", ]
    comment_regex = re.compile("|".join(comment_patterns))
    
    #removes sections of text that apply to the regex string
    data = data[~data["Method Text"].apply(lambda x: bool(comment_regex.search(x)))]

    return data
    
#function that retrieves methods from a file
def parse_java_methods(file):

    #open and read the content from a file
    with open(file, 'r', encoding = "utf8") as f:
        content = f.read()
        
    #initialize a list with the text
    try: 
        tree = javalang.parse.parse(content)
        
    #catch error thats generated from bad java code
    except javalang.parser.JavaSyntaxError:
        return []

    #initialize a method container
    methods = []
    
    #iterate through the sections of the file text
    for path, node in tree:
        
        #check if that section of the data is a method
        if isinstance(node, javalang.tree.MethodDeclaration):
            
            #initialize the position of the file where the method starts
            method_start = node.position.line

            #check for if there is a body to the method
            if node.body:
                #initialize the positon of the file where the method ends
                method_end = node.position.line + len(node.body)
            else:
                method_end = method_start

            #use the method start and end to get the text from the method
            method_text = '\n'.join(content.splitlines()[method_start-1:method_end])
            
            #add method information to the method container
            methods.append((node.name, method_text))
            
    return methods
    

#main section that calls the functions to preprocess the data in the data frame

#initialize the folder path using the Path module
folder_path = Path("Raw_Data")

#initialize the empty data frame for file data to be added to
df = pd.DataFrame(columns = ["Method Names", "Method Text"])

#iterate through files in the folder
for file_path in folder_path.iterdir():
    
    #check if the file is actulaly a file
    if file_path.is_file():
        
        #call to the java method parse function to collect data from the file
        data = parse_java_methods(file_path)
        
        #iterate through the function call output
        for method in data:
            
            #add the method data to the data frame
            df.loc[-1] = [method[0], method[1]]
            df.index = df.index + 1
            df = df.sort_index()
            
#call the remove duplicates function on the data frame
df = remove_duplicates(df)

#call the remove non-ascii characters function on the data frame
df = filter_ascii_methods(df)

#call the remove outliers function on the data frame
df = remove_outliers(df)

#call the remove boilerplate function on the data frame
df = remove_boilerplate_methods(df)

#call the remove commments function on the data frame
df = remove_comments(df)

#write the data frame to a new csv file
df.to_csv('preprocessed_data.csv')
