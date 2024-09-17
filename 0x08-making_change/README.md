# Coin Change Problem - "0. Change comes from within"

## Project Overview

This project tackles the classic Coin Change Problem using algorithms from the dynamic programming and greedy algorithm domains. The goal is to determine the minimum number of coins required to achieve a given total, provided a set of coin denominations. This problem not only tests algorithmic problem-solving skills but also the ability to select the appropriate method based on problem constraints.

## Learning Objectives

Through this project, you'll deepen your understanding of:

- **Greedy Algorithms**:
  - Understanding when and why greedy algorithms work for specific types of coin denominations.
  - Limitations of greedy algorithms in providing optimal solutions in certain scenarios.

- **Dynamic Programming (DP)**:
  - How dynamic programming can be used to optimize the coin change problem by solving overlapping subproblems.
  - Exploring the concept of optimal substructure.
  
- **Algorithmic Complexity**:
  - Analyzing time and space complexity for different approaches.
  - Writing efficient algorithms to meet runtime constraints.

- **Problem-Solving Strategies**:
  - Breaking down large problems into smaller sub-problems.
  - Iterative vs recursive approaches to dynamic programming.

## Key Concepts

1. **Greedy Algorithm**:
   - A greedy approach attempts to make the best possible choice at each step, selecting the largest denomination first.
   - The greedy solution may not always be optimal.

2. **Dynamic Programming**:
   - By building up solutions to smaller sub-problems and storing intermediate results, DP ensures the best solution is found efficiently.

3. **Algorithmic Complexity**:
   - The greedy approach typically operates in O(n) time, where n is the number of coins.
   - The dynamic programming solution has a time complexity of O(amount * n), where amount is the total and n is the number of denominations.

## Resources

- **Python Official Documentation**:
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) - for loops and if statements in Python.

- **GeeksforGeeks**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to Find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw)

## Problem-Solving Approach

1. **Greedy Solution**:
   - Start with the largest denomination and subtract it from the amount until the remainder is less than the denomination. Repeat with the next smaller denomination.
   - **Limitation**: Greedy algorithms do not always provide the minimum number of coins for all sets of denominations.

2. **Dynamic Programming Solution**:
   - Create a table to store results of subproblems. Initialize the table such that the value at index `i` represents the minimum number of coins needed to make `i`.
  

