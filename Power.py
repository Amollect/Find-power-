#Find power of x raised to y from user input.

num = int(input("Enter the number:"))
p= int(input("Enter the power:"))
temp = 1
for n in range(p):
    temp = temp*num
print(temp)