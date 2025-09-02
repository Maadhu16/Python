## While loop ##

While loop : 
            used when you want to repeat a block of code as long as a condition is True.

## Examples ##

i=5
while(i==5):
    print(i)
    i=1


##print 10,20,30..200 ##

i=10
while(i<=200):
    print(i,end=",")
    i=i+10


##reverse order number

i=10
while(i>0):
    print(i)
    i=i-1

## find the factorial ##

i=20
fact=1
while(i>0):
    fact*=i
    i-=1
print(fact)

## Break - to stop ##

i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

## continue - to skip ##

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

## Right angled triangle pattern ##

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()   # new line
    i += 1
