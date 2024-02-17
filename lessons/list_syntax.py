"""Demonstrate Basic list Syntax"""

# Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

# Add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# creat an already populated list
grocery_list2:list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

# indexing
print("Print first element of string")
print(grocery_list[0])

# modifying by Index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After chnage:")
print(grocery_list)

# you can have duplicates
grocery_list.append("almond milk")
print("Add almond milk again: ")
print(grocery_list)

# measuring length
print("Length of list:")
print(len(grocery_list))

# removing an item
grocery_list.pop(1)
print("After removing almond milk:")
print(grocery_list)

# function name: display
# parameter: list[str]
# return nothing!
# print out the list!.
print("List functin ex1:")
def display(word: list[str]) -> None:
    """Returning a list function with nothing"""
    print(word)

x = display(["Me", "you", "we"])
print(x)

# create a list!
# name: create
# paramaters: str and str
# return value: list[str]
# put both parameters into list
print("list function ex2:")
def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

print(create("Hello", "World"))

# or
x: list[str] = create("hello, world ")