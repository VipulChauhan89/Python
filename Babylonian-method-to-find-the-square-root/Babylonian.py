# This function returns true if x and y are within maximum_allowed_difference of each other, or False otherwise.
def close_enough(x,y,maximum_allowable_difference):
    return abs(x-y)<maximum_allowable_difference

# This function returns the square root of the N using the babylonian method close upto the precision passed in the function
def babylonian_square_root(N,estimate,precision):
    # N is the number whose square root need to be calculated
    # estimate is the callers first estimate and it cannot be zero in this case
    # precision is the how close the square root can get before returning it

    # here new estimate is calculated and if estimate value is zero then this new estimate will become infinite which will cause an exception
    new_estimate=(estimate+(N/estimate))/2

    #this loop will check if the new estimate is close enough to estimate and it will run until the close_enough function will return false
    while(not close_enough(estimate,new_estimate,precision)):
        estimate=(estimate+new_estimate)/2
        print("estimate = {}".format(estimate))
        new_estimate=N/estimate
    return estimate

# running the main function
if __name__=="__main__":
    try:
        N=float(input("Enter the number to find its square root : "))
        estimate=float(input("Enter the estimate value except for 0 : "))
        precision=float(input("Enter the precision upto which you want to find the square root : "))
    except:
        print("Please enter only number.")

    # Calling the function babylonian_square_root to print the square root of the number
    print("Square root of {0} = {1}".format(N,babylonian_square_root(N,estimate,precision)))
