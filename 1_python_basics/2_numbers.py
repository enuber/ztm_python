#  int and float are types of numbers.

# integer is a number 

# numbers video

print(2 + 4) # will get 6
print(2 - 4) # will get -2
print(2 * 4) # will get 8
print(2 / 4) # will get 0.5

print(type(2 + 4)) # <class 'int'>
print(type(2 / 4)) # <class 'float'> 
print(type(20+1.1)) # <class 'float'> 

print(2 ** 3) # to the power of... 8
print(2 // 4) # does division but returns the result rounded down an integer so get 0
print(5 // 4) # 1
print(5 % 4) # modulo sign, so get the remainder back in this case 1

# math functions video
# can google python3 math functions as there are alot of them but they do exist and can be used rather than having to create them yourself.

print(round(3.14)) # 3 
print(round(3.9)) # 4
print(abs(-20)) # 20 absolute value


# developer fundamentals video

# don't go and try to memorize everything, need to use the language to learn it. 


# operator precedence video

20 + 3 * 4 # 32  because multiplication happens first

# (), **, * and /, + and - 

print((5 + 4) * 10 / 2) # 45.0

print(((5 + 4) * 10) / 2) # 45.0

print((5 + 4) * (10 / 2)) # 45.0

print(5 + (4 * 10) / 2) # 25.0

print(5 + 4 * 10 // 2) # 25


# bin() video

print(bin(5)) # 0b101 the 0b is just a reference to the fact that it is a binary representation.

print(int('0b101', 2)) # will change it back to 5