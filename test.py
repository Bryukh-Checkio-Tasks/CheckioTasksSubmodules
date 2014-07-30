#Your optional code here
#You can import some modules or create additional functions
 
 
def checkio(data):
    a=[]
    k=data.count
    count=0
    for i in range(0,k):
        for j in range (0,k):
            if(data[i]==data[j]):
                count=count+1
        if(count>1):
            a.append(data[i])
            count=0
 
 
    data=a
 
    return data
 
 
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
