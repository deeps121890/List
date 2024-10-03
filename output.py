'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
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
