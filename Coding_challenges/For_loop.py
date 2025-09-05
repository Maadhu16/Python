# For Loop

# Problems: 

for i in "apple":        # using i variable for iterate values
    print(i)

Output - a
         p
         p
         l
         e

# loop with list 

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:      # using fruit variable for iterate fruits variable 
    print(fruit)

Output - apple
         banana
         cherry

# loop with dictionary

student = {"name": "Roshan", "age": 22}

for i, j in student.items():    # i for iterate key , j for value , .items() returns all key-value pairs in dictionary 
    print(i, ":", j)

Output - name : Roshan
         age : 22

# range method - range(start, stop, step) 

for i in range(5):      # range(5) starts from 0 to 4  
    print(i)

Output -  0
          1
          2
          3
          4

# Nested for loop 

for i in range(1,6):             # i (Outer loop) range starts from 1 to 5
    for j in range(1,3):         # j (inner loop) range starts from 1 to 2 
        print(i,j,"mango")

Output -  1 1 mango
          1 2 mango
          2 1 mango
          2 2 mango
          3 1 mango
          3 2 mango
          4 1 mango
          4 2 mango
          5 1 mango
          5 2 mango
 
# weeks and days 

for i in range(1,3):
    print("week",i)
    for j in range(1,8):
        print("day",j)

Output -  week 1
          day 1
          day 2
          day 3
          day 4
          day 5
          day 6
          day 7
          week 2
          day 1
          day 2
          day 3
          day 4
          day 5
          day 6
          day 7

# star pattern 

for i in range(5):
    print()
    for j in range(1,i+1):          # i+1 → take the value of i and add 1 to it 
        print("*",end="")           # end="" → prints on the same line.


Output - 
          *
          **
          ***
          ****
                    
for i in range(5):
    print()
    for j in range(1,i-1):          # i-1 → take the value of i and subtratct 1 to it 
        print(j,end=" ")            # end=" " → adds a space instead of a newline.

Output -                               


          1 
          1 2 
