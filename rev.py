'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''
# Function to print the list in reverse order
def print_reverse_list():
    # Input the list elements in a single line
    elements = list(map(int, input().split()))  # Read the input and convert to a list of integers

    # Print the elements in reverse order
    print(" ".join(map(str, elements[::-1])))  # Reverse the list and join for output

# Call the function
print_reverse_list()
