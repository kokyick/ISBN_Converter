import math #needed to use floor function

# Python code to convert  
# given Product ID to valid ISBN.

def productIdToISBN(productId):

    #convert Product ID to array of numbers
    _productIdArray = [int(i) for i in str(productId)]

    #remove the first three digits of the array
    # as they are  prefix that can be removed.
    _noOfPrefix = 3
    _newProductIdArray = _productIdArray[_noOfPrefix:]
    
    #mod 11 is chosen as it satisfied these 3 rules:
    #1. The modulus must be greater than the number of digits in the ISBN.
    #2. The modulus must be greater than the range of digits in each position.
    #3. The modulus must be a prime integer.

    #mod will be 11 as it satisfied all three rules
    _mod = 11
    
    #get the number of digits in the product id to convert to ISBN
    _lengthOfArray = len(_newProductIdArray)
    
    #counter to loop through the array elements
    _counter = 0

    #store the weigited sum
    _weightedSum=0

    #check if the product id satisfy rule no. 1
    if (_lengthOfArray < 11):

        #loop through every digit and 
        #multiple it based on it's position in the array
        #to get the weighted sum
        for x in range(_lengthOfArray, 0, -1):
            _cal = _newProductIdArray[_counter] * (x+1)
            _weightedSum = _weightedSum + _cal
            _counter+=1

        # which is the remaining mod of the weighted sum
        _lastdigit = 0

        #if mod is not zero, need to find the last digit to get a vaild ISBN
        if ((_weightedSum % _mod)!=0): 

            #get the next nearest sum that will return mod 0
            _nextMultiplier = math.floor(_weightedSum/_mod)+1
            _balancedsum = _mod * _nextMultiplier
            
            #last digit of the ISBN would be the difference between 
            # next mod 0 sum with weighted sum
            _lastdigit = _balancedsum - _weightedSum

        #if the last digit is 10 change it to X
        if _lastdigit==10:
            _lastdigit="x"
        #append the last digit
        _newProductIdArray.append(_lastdigit)
        #join the final array to make up the final ISBN product ID
        _ISBN = ''.join(map(str, _newProductIdArray))
        return _ISBN
    else:
        return ("The number of digits in the ISBN must be smaller than the modules of 11.")



# Start Program
productID = ""
while productID != "q":
    productID = input("Enter a ProductID (Enter q to exit): ")
    
    if (productID!="q"):
        print("ISBN:",productIdToISBN(productID))

print("Thank you for your time!")