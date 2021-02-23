#If / For / While Nesting
x = "Cisco"

if "i" in x:
    if len(x) > 3: #if nesting
        print(x, len(x))

#Cisco 5 #result of the above block

list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2: #for nesting
        print(i*j)

#40 80 120 50 100 150 60 120 180 #result of the above block

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:  #while nesting
        print(z)
        z += 1

#5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10	#result of the above block

for number in range(10):
    if 5 <= number <= 9: #mixed nesting
        print(number)

#5 6 7 8 9 #result of the above block
