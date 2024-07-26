# Pascal's Triangle in Python

## Resources
To complete this project, you should familiarize yourself with the following resources:
- [What is Pascal’s Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=XMriWTvPXHI)
- [What are Python Algorithms](https://www.geeksforgeeks.org/python-programming-language/)

## Additional Resources
- [Mock Technical Interview](https://www.pramp.com/)
- [Must Know](https://realpython.com/)

## Project Overview
This project involves implementing Pascal's Triangle in Python. Pascal's Triangle is a triangular array of the binomial coefficients. Each row represents the coefficients in the expansion of a binomial raised to successive powers.

## Learning Objectives
To successfully complete this project, you should revise the following Python concepts:

### Lists and List Comprehensions
- Understand how to create, access, modify, and iterate over lists.
- Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.

### Functions
- Know how to define and call functions.
- Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.

### Loops
- Use for and while loops to iterate through sequences.
- Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.

### Conditional Statements
- Apply if, elif, and else conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).

### Recursion (Optional)
- While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
- Recognize base cases and recursive cases for a function that generates the triangle’s rows.

### Arithmetic Operations
- Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.

### Indexing and Slicing
- Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.

### Memory Management
- Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.

### Error and Exception Handling (Optional)
- Use try-except blocks as needed to handle potential errors, such as invalid input types or values.

### Efficiency and Optimization
- Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
- Evaluate and apply optimizations to improve the performance of the solution.

## Implementation Details
1. **Function Definition**:
   - Define a function `generate_pascals_triangle(n)` where `n` is the number of rows to generate.
   
2. **List Initialization**:
   - Initialize a list to hold the rows of Pascal’s Triangle.
   
3. **Iterative Approach**:
   - Use a loop to generate each row based on the values of the previous row.
   - Utilize list comprehensions to make the code more concise.

4. **Edge Cases**:
   - Ensure the function handles edge cases, such as when `n` is 0 or 1.

5. **Output**:
   - The function should return a list of lists, where each inner list represents a row of Pascal’s Triangle.

## Example Usage
```python
def generate_pascals_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

# Example
n = 5
print(generate_pascals_triangle(n))
# Output:
# [
#   [1],
#   [1, 1],
#   [1, 2, 1],
#   [1, 3, 3, 1],
#   [1, 4, 6, 4, 1]
# ]

