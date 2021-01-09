def stringify(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
    	try:
	    result = str(result)
    	except:
	    pass
    	return result
    return wrapper
 
        
@stringify
def add(a, b):
    return a + b
 

print(add([2, 3], [2,5]))
