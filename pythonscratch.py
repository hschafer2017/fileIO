f = open('data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

f = open('data.txt', 'r')
lines = f.read().split('\n')
# This dot.dot method is adding more commands onto the function. If you split a string, and give it a character to split on, it will turn it into a list. 
f.close()
print(lines)


l = ['abc', 'ghi', 'def', 'lmnop', 'qrst']
print([l])
print([1:3])
# starting from the beginning ':' goes before the number, and up to the end is ":" after the number