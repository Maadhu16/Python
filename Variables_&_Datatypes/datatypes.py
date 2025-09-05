# Datatypes - defines the kind of value stored in a variable.

# Example:

a = 10              # 10 => int ( Represents whole numbers )
print(type(a))

Output => Integer

b = "Maadhu"        # maadhu => String ( for text )
print(type(b))

Output =>  String

c = 10.5             # 10.5 => float ( for decimal numbers )
print(type(c))

Output => Float

d = True
e = False

print(type(d))
print(type(e))

Output => bool          # Boolean - is widely used in conditions, comparisons, and control flow.
          bool

# List - store multiple items in a single variable.
# Ordered, mutable, allows duplicates, Can store mixed data types.

f = ["apple", "banana", "cherry"]   
print(type(f))

Output => List 

# Tuple - collection of store multiple values.
# Ordered, immutable, allows duplicates, Can store mixed data types.

g = ("apple", "banana", "cherry", "apple")
print(type(g))

Output => Tuple

# Set - is collection of multiple values
# Unordered, unchangeable, not allow duplicates, can stored mixed data types.

h = {1, "hello", 3.14, True}
print(type(h))

Output => Set

# Dictionary - is a collection of key–value pairs.
# each key is unique and also used to access values, Unordered, mutable, can stored mixed data types.

i = {"name": "Maddy", "age": 21}       # name => key ; Maddy => value
print(type(i)

Output => Dictionary
