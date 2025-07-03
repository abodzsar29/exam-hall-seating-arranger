# Andrew Bodzsar
# andrewbodzsar@proton.me

# Using a backtracking algorithm
# 1. 25 students are created, A01 to A25
# 2. Pick 2 random students, flag them as special
# 3. Assign tests to all students based on their alphabetical position, 2 special students are T5
# 4. Try to place students one by one
# 5. Use backtracking to fill grid row by row, try every available student
# 6. Placement is valid if there are no collision with the neighbours
# 7. Move to next cell by recursion
# 8. Backtrack if no option is found, undo the placement and try the next student
# 9. Stop when the grid is valid or out of options 

import random

class Student:
    def __init__(self, name, test=None, is_special=False):
        self.name = name
        self.test = test
        self.is_special = is_special

    def __repr__(self):
        return f"{self.name}({self.test})"

class Solution:

    def __init__(self):
        self.grid = [[None for _ in range(5)] for _ in range(5)]  # empty 2D grid
        self.students = []  # empty list
        self.setup_student()
        
    def setup_student(self):
        self.students = [Student(f"A{i:02d}") for i in range(1, 26)] # populate list, fstrings for naming

        special_students = random.sample(self.students, 2)  # turn 2 students special
        for student in special_students:
            student.is_special = True

        tests = ['T1', 'T2', 'T3', 'T4', 'T5']  # Get one of the 5 tests, T5 is for the special
        for i, student in enumerate(self.students):
            if student.is_special:
                student.test = 'T5'
            else:
                student.test = tests[i % 5]

    def neighbour_checker(self, row, col, student):
        for row_offset in range(-1, 2):  # to check neighbours x axis
            for col_offset in range(-1, 2):  # y axis
                if row_offset == 0 and col_offset == 0:  # to avoid checking same field
                    continue

                new_row, new_col = row + row_offset, col + col_offset

                if 0 <= new_row < 5 and 0 <= new_col < 5:  # to avoid out of bounds error
                    neighbor = self.grid[new_row][new_col]
                    if neighbor is not None:
                        if neighbor.test == student.test:
                            return False
        return True

    
    def student_plotter(self, row, col):
        if row == 5:  # exit if whole grid was checked
            return True

        next_row = row + (col + 1) // 5  # allows row by row parsing of grid
        next_col = (col + 1) % 5

        for student in list(self.students):  # try to paste students
            if self.neighbour_checker(row, col, student):  # if neighbours don't collide, continue
                self.grid[row][col] = student
                self.students.remove(student)

                if self.student_plotter(next_row, next_col):  # recursive call
                    return True 

                # backtrack if false was returned
                self.students.append(student)
                self.grid[row][col] = None 

        return False
    
    def print_solution(self):              
        print("seating arrangement:")
        for row in self.grid:
            print(" | ".join(f"{str(student):<9}" for student in row))  # print as a box

def main():
    solution = Solution()

    if solution.student_plotter(0,0):
        solution.print_solution()
    else:
        print("solution is not possible")



if __name__ == "__main__":  # run through console
    main()