#import necessary libraries
import time
import requests
import csv

#function that retrieves url info for each of the repositories based on a csv file row
def parse_row_info (row):
    #repository owner name and repository name initialization
    repo_owner = row[0]
    repo = row[1]
    
    #initialize path string
    path = ""
    
    #iterate through remaining columns within the row
    for i in range(len(row) - 2):
    
        #check object is a string type
        if (type(row[i+2]) == type('str')) & (row[i+2] != ''):
            
            #add object content to current string path
            path = path + row[i+2] + '/'
            
    #return relevant data about repository
    return(repo_owner, repo, path)

#function that creates a text file with the data collected
def java_to_text (repo_owner, repo, file_name, file_path):
    #initialize url
    url = f"https://raw.githubusercontent.com/{repo_owner}/{repo}/master/{file_path}"
    
    #retrieve response with request module
    response = requests.get(url)

    print(url)
    print(response)
    
    #check success of request
    if response.status_code == 200:
        
        with open(f"./Raw_Data/{repo}{file_name}.txt", 'a', encoding = 'utf8') as file:
            file.write(response.text)

    elif response.status_code != 404:

        input()
        java_to_text(repo_owner, repo, file_path)
          
#function that retrieves all the types of a specific file in a section of a repository
def get_files (repo_owner, repo, path, file_extension):
    #initialize url
    url = f"https://api.github.com/repos/{repo_owner}/{repo}/contents/{path}"

    #retrieve response with request module
    response = requests.get(url)
    
    print(url)
    print(response)
    
    #check success of request
    if response.status_code == 200:

        #initialize tree data
        tree = response.json()
    
        #iterate through all files/folders within the tree
        for file in tree:
            #check if file name ends with the correct file extension
            if file['name'].endswith(file_extension):
        
                #call file write function
                java_to_text(repo_owner, repo,file['name'], file['path'])

    elif response.status_code != 404:

        input()
        get_files(repo_owner, repo, path, file_extension)
  
#main section running through the csv file with repository data
#initialize from csv file
with open('Assignment1Data.csv', 'r') as f:
    reader = csv.reader(f)
    
    #iterate through rows within the file
    for row in reader:
        
        #call row parsing information
        repo_owner, repo, path = parse_row_info(row)
        #call file retrieving function
        get_files(repo_owner, repo, path, '.java')
