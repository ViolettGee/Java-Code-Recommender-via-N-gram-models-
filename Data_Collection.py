#import necessary libraries
import requests
import pandas as pd

#function that retrieves url info for each of the repositories based on a csv file row
def parse_row_info(row):
  return #placeholder
  
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
        java_to_txt(repo_owner, repo, file['name'], file['path'])
  
#function that creates a text file with the data collected
def java_to_text(repo_owner, repo, file_name, file_path):
  #initialize url

  #retrieve response with request module

  #check success of request

    #write file text to new file in current repo
  return #placeholder
  
#main section running through the csv file with repository data
