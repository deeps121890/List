'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
# Function to find the largest number in a list
def find_largest_number():
    # Input the size of the list
    size = int(input())  # First input corresponds to the size of the list
    elements = []  # Initialize an empty list to hold the elements

    # Input the list elements
    for _ in range(size):
        element = int(input())  # Read each element
        elements.append(element)  # Add the element to the list

    # Find the largest element in the list
    largest_number = max(elements)  # Use the built-in max function

    # Output the largest number
    print(largest_number)

# Call the function
find_largest_number()
