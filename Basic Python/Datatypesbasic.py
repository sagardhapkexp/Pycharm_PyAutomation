
# 1 - To print multiple variable in a single line
a = 10
b = 20
c = 30
print(a, b, c)  # 10,20,30

#==============================================================

# 2 - To initialise multiple variable in a single line
a, b, c = 10, 20, 30
print(a, b, c)  # 10,20,30

#==============================================================

# 3 - To have a same value in all the varaible
a = b = c = 100
print(a, b, c)  # 100,100,100

#==============================================================

# 4 - To Swap the numbers in a single line of code
x = 1
y = 2
print(x,y) #1,2
y,x = x,y
print(x,y)

#==============================================================

# 5 - To Overwrite the Values
a = 10
print(a)
a = 'Here I overwriting the value for a variable'
print(a)

#==============================================================
# 6 - To Delete the Values of Variable.
x1 = 220
x2 = 440

print(x1, x2)
del(x1)
print(x1,x2)