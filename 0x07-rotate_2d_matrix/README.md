# 0. Rotate 2D Matrix

## Project Overview

This project focuses on implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The goal is to manipulate the matrix efficiently without using extra space, which requires a deep understanding of matrix manipulation and in-place operations in Python.

## Key Concepts

### Matrix Representation in Python
- **Understanding 2D Matrices**: Represented as lists of lists in Python.
- **Element Access and Modification**: Learn how to access and modify elements in a 2D matrix.

### In-place Operations
- **In-place Modifications**: Perform operations on the original matrix without creating a copy, optimizing space complexity.

### Matrix Transposition
- **Transposing a Matrix**: Swap rows and columns of a matrix. This is the first step in rotating the matrix.
- **Implementation**: Efficiently transpose a matrix in Python.

### Reversing Rows in a Matrix
- **Reversing Rows**: After transposing, reverse each row to complete the 90-degree clockwise rotation.

### Nested Loops
- **Using Nested Loops**: Employ nested loops to iterate over the matrix elements for transposition and row reversal.

## Resources

### Python Official Documentation
- **Data Structures**: Learn about list comprehensions and nested list comprehensions.
- **More on Lists**: Understand the various list operations available in Python.

### GeeksforGeeks Articles
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Basics of list manipulation in Python.

## Approach

To solve this problem:
1. **Transpose the Matrix**: Swap rows with columns.
2. **Reverse Each Row**: Reverse the order of elements in each row to achieve a 90-degree clockwise rotation.

This method efficiently performs the rotation in-place, enhancing your problem-solving skills and algorithmic thinking in Python.

## Additional Resources
- **Mock Technical Interview**: Prepare yourself with a mock interview focusing on in-place matrix manipulation problems.

## Requirements

### General
- **Allowed Editors**: `vi`, `vim`, `emacs`.
- **Environment**: All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.10).
- **File Guidelines**:
  - Every file must end with a new line.
  - The first line of each file should be: `#!/usr/bin/python3`.
  - Include a `README.md` file at the root of the project folder.
- **Coding Standards**:
  - Follow `pycodestyle` style (version 2.8.0).
  - No module imports are allowed.
  - All modules and functions should be well-documented.
  - Ensure all files are executable.

## Conclusion

By understanding these concepts and utilizing the provided resources, you will be able to rotate a 2D matrix by 90 degrees clockwise in Python efficiently and in-place. This project will test your ability to manipulate data structures and optimize algorithms, preparing you for more complex challenges.

