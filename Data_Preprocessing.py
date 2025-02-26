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
def filet_ascii_methods(data):

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
    return data[(method_lengths >= lowe_bound) & (method_lengths <= upper_bound)]
    
#function that removes boilerplate patterns
def remove_boilerplate_methods(data):
    return #placeholder
#initialize regex string

#removes sections of text that apply to the regex string

#function that removes comments from methods
def remove_comments(data):
    return #placeholder
#initialize regex string

#removes sections of text that apply to the regex string

#function that retrieves methods from a file
def parse_java_methods(file):
    return #placeholder
#open and read the content from a file

#initialize a list with the text and initialize a method container

#iterate through the sections of the file text

#check if that section of the data is a method

#initialize the position of the file where the method starts

#check for if there is a body to the method

#initialize the position of the file where the method ends

#use the method start and end to get the text from the method

#add method information to the method container


#main section that calls the functions to preprocess the data in the data frame

#initialize the folder path using the Path module

#initialize the empty data frame for file data to be added to

#iterate through files in the folder

#check if the file is actulaly a file

#call to the java method parse function to collect data from the file

#iterate through the function call output

#add the method data to the data frame

#call the remove duplicates function on the data frame

#call the remove non-ascii characters function on the data frame

#call the remove outliers function on the data frame

#call the remove boilerplate function on the data frame

#call the remove commments function on the data frame

#write the data frame to a new csv file
