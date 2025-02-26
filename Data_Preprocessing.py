#import necessary libraries

#function that removes duplicates from the data

#removes verbatim duplicates from the data

#function that removes all none ASCII characters

#searches column and removes non ASCII characters

#function that removes outlier methods

#determine the mehtod lengths of a column

#calculate lower and upper bounds

#filters out all methods not within the calculated bounds

#function that removes boilerplate patterns

#initialize regex string

#removes sections of text that apply to the regex string

#function that removes comments from methods

#initialize regex string

#removes sections of text that apply to the regex string

#function that retrieves methods from a file

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
