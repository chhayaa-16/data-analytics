def total(data):
    return sum(data)



def average(data):
    
    return sum(data)/ len(data)
    


def highest(data):
    return max(data)

def lowest(data):
    return min(data)


def logic(data):
    
    if 1000 not in data:
        data.append(1000)
        return (data)
    else:
        print("value exixt")



def assending(data):  
    data.sort()
    return(data) 
   
#or--- def ass(data):
#           return sorted(data)

def descending(data):
    data.reverse()
    return (data)


#def des(data)
     #   return sorted(data, reverse = True)



