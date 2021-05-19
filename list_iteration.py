import sys

# Set up a list for our code to work with that omits the first CLI argument, 
# which is the name of our script (list_iteration.py)
order_of_succession = sys.argv
order_of_succession.pop(0)

# Now, order_of_succession is ready for us to work with

for number, name in enumerate(order_of_succession, 1):
    print(f"{number}. {name}")
