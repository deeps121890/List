'''
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
[1, 2, 3, 4]
'''
# Function to create and display a list
def create_and_display_list():
    # Input the size of the list
    n = int(input())  # First integer corresponds to the size of the list
    elements = []  # Initialize an empty list to hold the elements

    # Input the list elements
    for _ in range(n):
        element = int(input())  # Read each element
        elements.append(element)  # Add the element to the list

    # Display the list
    print(elements)  # Print the list

# Call the function
create_and_display_list()
