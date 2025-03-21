# Java-Code-Recommender-via-N-gram-models-
* [1 Introduction](#1-introduction)  
* [2 Getting Started](#2-getting-started)  
  * [2.1 Preparations](#21-preparations)  
  * [2.2 Install Packages](#22-install-packages)  
  * [2.3 Run N-gram](#23-run-n-gram)  
* [3 Report](#3-report)  

---

# **1. Introduction**  
This project explores **code completion in Java**, leveraging **N-gram language modeling**. The N-gram model predicts the next token in a sequence by learning the probability distributions of token occurrences in training data. The model selects the most probable token based on learned patterns, making it a fundamental technique in natural language processing and software engineering automation.  

---

# **2. Getting Started**  

This project is implemented in **Python 3.9+** and is compatible with **macOS, Linux, and Windows**.  

## **2.1 Preparations**  

(1) Clone the repository to your workspace:  
```shell
~ $ git clone https://github.com/ViolettGee/Java-Code-Recommender-via-N-gram-models-.git
```

## **2.1 Install Packages**

Install the required dependencies:

(venv) $ pip install requests
       $ pip install pandas
       $ pip install javalang
       $ pip install numpy

## **2.3 Run N-gram**

The scripts should be run in the as described below if you are completely re-initializing the model with the data or if you are using the model with your own data. However, as the files are all included in the repository all files should be runnable following cloning the repository. 

1. "Data_Collection.py"
This file collects data from github repositories based off the entered data in "Assignment1Data.csv". The file is in the format: repository owner, repository name, and file path with each folder having tabs between them. This file is used to formulate the urls of each of the specific folders which are pulled using the request module. Each file within the folder is then expected to dertmine if the file is a Java file. If the file is a Java file, the request module is used to request the text that is then saved to a file in the "Raw_Data" folder.

2. "Data_Preprocessing.py"
This file iterates through each of the files in the "Raw_Data" folder, extracting the methods from each of the files using the javalang module. Once all files in the folder have been analyzed, the pandas data frame containing the Java methods is further analyzed eliminating sections based on the preprocessing specifications as described in the report. The remaining Java methods are extracted into the "preprocessing_data.csv" file.

3. "Data_Tokenization.py"
This file iterates through each of the Java methods within the "preprocessing_data.csv" file. Each method is tokenized using the javalang module. The tokens of each Java method are then extracted into the "tokenized_data.csv" file.

4. "NgramModel.py"
This file seperates the data in the "tokenized_data.csv" file into the training data in "train.csv" and the testing data in "test.csv". The model then iterates through various context window sizes to find the most optimal for the data based on perplexity.

5. "Test.py"
The file goes through each of the tokenized methods in "test.csv" and prompts the Ngram model to complete the method using the first n tokens equivalent to the optemized context window. Each output is compared to the actual method to generate an accuracy score, and the first 100 test cases are exported to "validation_set.csv". The accuracy score is then averaged and displyed, and the perplexity is computed for the test data.

6. "Professor_Processing.py"
The file computes the same processes as above on the data provided by the professor saving checkpoints in the following files: "Professor_tokenized_data.csv", "Professor_test.csv", "Professor_train.csv", and "Professor_validation_set.csv".

## 3. Report

The assignment report is available in the file Assignment_Report.pdf.



