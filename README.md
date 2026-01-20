# Take-Home Assignment for an English Motorsport Firm for a Junior Software Developer position

## Overview

This assessment is a **required part of the application** and must be **submitted within 24 hours**.

You are asked to design and explain an algorithm that assigns students to exams and seats them in an exam hall while respecting a set of constraints.

---

## Problem Description

There is an exam hall containing **25 students** and **5 different tests** (T1 through T5).

### Students
- Create **25 students**, named **A01 to A25**
- Students must be **sorted alphabetically**

### Special Students
- Randomly flag **exactly 2 students** as **Special**
- **Special students must take Test T5**

### Test Assignment
- Each student takes **one test** (T1–T5)
- Non-special students are assigned a test **based on their alphabetical position**
- Special students override this rule and **must take T5**

### Seating Arrangement
- Seat all students in a **5 × 5 grid** (25 seats total)
- Every seat must be filled by exactly one student

### Neighbour Constraint
- A student **must not** be seated next to another student taking the **same test**
- A *neighbour* is any **adjacent cell**, including:
  - Up
  - Down
  - Left
  - Right
  - Diagonals

---

## Required Output

Your solution must:
- Describe an **algorithm** that satisfies all constraints
- Output:
  - Each student
  - Their assigned test
  - Their position in the grid

---

## Implementation Requirements

- The solution must be implemented in **one of the following languages**:
  - **C#**
  - **TypeScript**
  - **Python**
- The solution **must be runnable**
- Include **unit tests** demonstrating correctness
- Upload your solution as a **ZIP file**
- Solutions will be **automatically checked for AI involvement**

---

## Example Grid Visualization

Below is a representation of the 5×5 grid layout.  
Each cell represents a desk occupied by a student.

```
+-----+-----+-----+-----+-----+
| A?/T?| A?/T?| A?/T?| A?/T?| A?/T?|
+-----+-----+-----+-----+-----+
| A?/T?| A?/T?| A?/T?| A?/T?| A?/T?|
+-----+-----+-----+-----+-----+
| A?/T?| A?/T?| A?/T?| A?/T?| A?/T?|
+-----+-----+-----+-----+-----+
| A?/T?| A?/T?| A?/T?| A?/T?| A?/T?|
+-----+-----+-----+-----+-----+
| A?/T?| A?/T?| A?/T?| A?/T?| A?/T?|
+-----+-----+-----+-----+-----+
```

- Each cell contains a **student (Axx)** and their **test (Tx)**
- Neighbours include all surrounding cells (including diagonals)
- No two neighbouring cells may contain the **same test**

---

# Example Resulting Grid Output

seating arrangement:

A01(T1)   | A02(T2)   | A03(T3)   | A04(T5)   | A06(T1)  
A05(T5)   | A09(T4)   | A11(T1)   | A07(T2)   | A08(T3)  
A12(T2)   | A13(T3)   | A10(T5)   | A19(T4)   | A14(T5)  
A15(T5)   | A16(T1)   | A17(T2)   | A18(T3)   | A21(T1)  
A22(T2)   | A23(T3)   | A20(T5)   | A24(T4)   | A25(T5) 

--- 
