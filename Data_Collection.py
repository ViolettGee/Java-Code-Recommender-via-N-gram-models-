#import necessary libraries
import requests
import pandas as pd

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
    if type(row[i+2]) == type('str'):
      #add object content to current string path
      path = path + '/' + row[i+2]

  #return relevant data about repository
  return(repo_owner, repo, path)

#function that creates a text file with the data collected
def java_to_text (repo_owner, repo, file_name, file_path):
  #initialize url
  url = f"https://raw.githubusercontent.com/{repo_owner}/{repo}/master/{file_path}"

  #retrieve response with request module
  response = requests.get(url)

  #check success of request
  if response.status_code == 200:

    #write file text to new file in current repo
    with open(f"Raw_Data/{repo}{file_name}.txt", 'w') as file:
      file.write(response.text)
  
#function that retrieves all the types of a specific file in a section of a repository
def get_files (repo_owner, repo, path, file_extension):
  #initialize url
  url = f"https://api.github.com/repos/{repo_owner}/{repo}/contents/{path}"
  
  #retrieve response with request module
  response = requests.get(url)
  
  #check success of request
  if response.status_code == 200:
    #initialize tree data
    tree = response.json()
    
    #iterate through all files/folders within the tree
    for file in tree:
      #check if file name ends with the correct file extension
      if file['name'].endswith(file_extension):
        #call file write function
        java_to_text(repo_owner, repo, file['name'], file['path'])
  
#main section running through the csv file with repository data
#initialize data frame from csv file
df = pd.read_csv('Assignment1Data.csv')

#iterate through rows within the data frame
i = 0
while i < df.shape[0]:
  
  #call row parsing information
  repo_owner, repo, path = parse_row_info(df.iloc[i])
  #call file retrieving function
  get_files(repo_owner, repo, path, '.java')

  i = i + 1
