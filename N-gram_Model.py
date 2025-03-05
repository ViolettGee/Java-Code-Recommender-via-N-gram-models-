#initialize libraries

#class containing the n-gram model

    #initialize the n-gram model with the data

    #determine the probability of the n grams occurrences

        #initialize dictionary for the count of the n occurrences

        #initialize the dictionary for the probability of a token given the n with a set of data

        #iterate through the methods in the data
            #iterate through the tokens in the data

                #check if n is 1

                #check if the number of tokens is greater than n

                    #check if the sequence of tokens exists
                        #increment the number of occurrences

                        #check if the sequence of tokens n exists **ending should be its own occurence as well
                            #increment the number of occurrences
                        #initialize the occurence of the sequence of tokens n exists

                    #initialize the occurences of the sequence of tokens n exists

    #function for evaluating the model perplexity
        #have the evaluation have a pass in

        #initialize the dictionary for test data

        #iterate through the dictionary
            #iterate through the iternal dictionary
                #product each probability
                #sum the number of probabilities

        #inverse the product
        #exponent of the product by the sum

        #return the perplexity
    
    #create function for predicting the next word in a sequence
        
        #look for sequence in data
            #determine most likely occurence based on n gram

        #if sequence hasn't been seen
            #no sequence known

    #function for predicting sequence based on a sequence

        #tokenize the prompt
        #determine the last n tokens

        #do while loop for predicting the next word until the sequence ends
            #determine the next word
            #determine the tokens of the next occurrence

#function for if this file specificially is run

    #pull out the tokenized data

    #seperate the data into two sections: training and testing

    #iterate through different values of n to find the best

        #initialize the model for that n value

        #evaluate the model for that n value

        #pick the current best n value or this n value based on the evaluation metric
            #lower perplexity