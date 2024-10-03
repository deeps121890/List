'''
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
'''
# Function to separate even and odd numbers into two lists
def separate_even_odd():
    # Input the size of the list
    size = int(input())  # First input corresponds to the size of the list
    elements = []  # Initialize an empty list to hold the elements

    # Input the list elements
    for _ in range(size):
        element = int(input())  # Read each element
        elements.append(element)  # Add the element to the list

    # Initialize lists for even and odd numbers
    even_list = []
    odd_list = []

    # Separate the elements into even and odd lists
    for num in elements:
        if num % 2 == 0:
            even_list.append(num)  # Add to even list
        else:
            odd_list.append(num)    # Add to odd list

    # Output the results
    print(f"The even list {even_list}")
    print(f"The odd list {odd_list}")

# Call the function
separate_even_odd()
