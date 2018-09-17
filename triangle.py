

def calcexpand(listin):
	result = []
	for x in range(0,len(listin)-1):
		result.append(listin[x]+listin[x+1])
	result.insert(0,1)
	result.append(1)
	return result



def pascal(n):
	x = 2
	pascalin = [1]
	while x <= n:
		pascalin = calcexpand(pascalin)
		x += 1
	return pascalin


print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))

print(pascal(10))




### JChoi's solution


def pascal(n):
    def pascal_int(n,i):
        if n <= 2 or i == 1 or i == n:
            return 1
        else:
            return pascal_int(n-1, i-1) + pascal_int(n-1, i)
    arr = []
    for x in range(1, n+1):
        arr.append(pascal_int(n,x))        
    return arr


print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))

print(pascal(10))