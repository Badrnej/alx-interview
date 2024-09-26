# 0x09. Island Perimeter

## Algorithm | Python

**Project Start Date:** September 23, 2024, 6:00 AM  
**Deadline:** September 27, 2024, 6:00 AM  
**Checker Released:** September 24, 2024, 6:00 AM  
**Auto Review:** The review will be launched automatically at the deadline.

---

### Introduction

This project focuses on solving a geometric problem within a grid context, specifically calculating the perimeter of a single island. The grid is represented by a 2D list (matrix), where each cell can either be land (`1`) or water (`0`). The goal is to apply your knowledge of 2D arrays and conditional logic to count the perimeter of the island formed by the land cells.

### Learning Objectives

- **2D Arrays (Matrices):**
  - Access and iterate over elements in a 2D array.
  - Navigate through adjacent cells (horizontally and vertically).
  
- **Conditional Logic:**
  - Apply conditions to determine if a cell contributes to the perimeter.
  
- **Counting Techniques:**
  - Develop a method to count the edges that contribute to the perimeter.
  
- **Problem-Solving:**
  - Break down the problem into smaller tasks: identifying land cells and calculating their perimeter contribution.
  
- **Python Programming:**
  - Use nested loops to iterate over grid cells.
  - Apply conditional statements to check adjacent cells' status.

---

### Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3).
- Your code should use **PEP 8** style (version 1.7).
- You are **not allowed to import any module**.
- All modules, functions, and files must be documented.
- All files should be **executable** and end with a new line.
- The first line of each file must be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.

### Approach

1. **Understand the Grid Structure:**
   - The grid is a 2D list where `1` represents land and `0` represents water.
   - You will need to check the perimeter for each land cell and ensure that no land cell is missed.

2. **Perimeter Calculation Logic:**
   - The perimeter of a cell is incremented for each side that touches water or the grid boundary.
   - For each land cell, check the four possible adjacent cells (top, bottom, left, and right):
     - If a neighboring cell is water (`0`) or outside the grid, it contributes to the perimeter.

3. **Edge Cases to Consider:**
   - A grid with no land cells.
   - Islands touching the grid boundary.
   - Small grids (1x1) or non-square grids.

---

### Example

```python
# Example grid:
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [0, 1, 0, 0]
]

# Expected output: 12 (The perimeter of the island)

