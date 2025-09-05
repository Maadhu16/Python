# Variables - containers for storing data values.
# Variable names are case-sensitive.

#Example:

x = 5                    # x => variable name, 5 => value
y = "Maadhu"             # y => variable name, Maadhu => value
print(x)
print(y)

Output => 5
          Maadhu

## Global variables - Variables that are created outside of a function.

# Example:

x = "awesome"                

def myfunc():
  print("Python is " + x)

myfunc()
