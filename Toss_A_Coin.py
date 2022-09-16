import random as rd


#For display/visualisation effect only
SEPARATION = "*" * 30

#Tosses coin n- times, shows outcome comparison between the 
#Head and the Tail and return the difference between their counts   
def Toss_Coin(n):

    #Stores the two sides of a coin (Head and Tail) 
    COIN_SIDES = ["Head", "Tail"]
    
    #Accumalatively stores the result of each single toss
    results = []
    
    #Repeatedly tosses coin n- times 
    for i in range(n):
        #coin Toss 
        rd.shuffle(COIN_SIDES)
        coin_Side_Pick = COIN_SIDES[rd.randint(0,1)]
    
 	#Takes the outcome of coin Toss to results
        results.append(coin_Side_Pick)
    
    #counts and print the number of Head 
    no_Head = results.count("Head")
    print("Count:Number of Heads = ", no_Head )
    
    #counts and prints the number of Tail
    no_Tail = results.count("Tail")
    print("Count:Number of Tails = ", no_Tail )
    
    #Difference in number of counts
    difference = abs( no_Head - no_Tail )
    print("\nDifference in number of Counts = ", difference)
    
    #Percentage of Head in n- tosses
    Head_probability = (no_Head) / (n)
    Head_percentage = round(Head_probability * 100, 2)
    print( f"Head_probability = {Head_probability}")
    print( f"Head_percentage = {Head_percentage}%")
    
    #Percentage of Tail in n- tosses
    Tail_probability = (no_Tail) / (n)
    Tail_percentage = round(Tail_probability * 100, 2)
    print( f"Tail_probability = {Tail_probability}")
    print( f"Tail_percentage = {Tail_percentage}%")
    
    return difference


#Total number of times to toss coin 
n = 10000

"""
To conpare multiple values of Toss_Coin(),
set the value of i to desired value
"""
KEY = True
while KEY:
        #Number of times to call Toss_Coin()
	i = 5

	#Stores difference for each round of n- tosses               
	store_Diff = []

	#Repeated calls Toss_Coin() i-times
	for j in range(i):
	    print(SEPARATION)
	    
	    #Takes the return value of Toss_Coin() to store_Diff
	    store_Diff.append(Toss_Coin(n))
	    
	if i > 1:
	    print(SEPARATION)
	    print(f"No of {n} tosses = ", i)
	    print("Maximum Difference Between Counts= ", max(store_Diff))
	    print("Minimum Difference Between Counts= ", min(store_Diff))
	    
	KEY = False
    
