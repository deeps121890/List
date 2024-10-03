'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
'''
# Function to calculate the sum of elements in the array
def sum_of_array_elements():
    # Input the number of elements in the array
    n = int(input())  # First integer corresponds to n
    elements = []  # Initialize an empty list to hold the elements

    # Input the array elements
    for _ in range(n):
        element = int(input())  # Read each element
        elements.append(element)  # Add the element to the list

    # Calculate the sum of the elements
    total_sum = sum(elements)  # Use the built-in sum function

    # Output the sum
    print(total_sum)

# Call the function
sum_of_array_elements()
