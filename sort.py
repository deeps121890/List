'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
# Function to sort and print the list
def sort_and_print_list():
    # Input the list elements in a single line
    elements = list(map(int, input().split()))  # Read the input and convert to a list of integers

    # Sort the list
    elements.sort()  # Sort the list in ascending order

    # Print the sorted list
    print(" ".join(map(str, elements)))  # Join the sorted list into a string for output

# Call the function
sort_and_print_list()
