import unittest
from solution import Student, Solution

class Tester(unittest.TestCase):

    def setUp(self):
        self.tester = Solution()

    def test_rule_student_generation(self):
        self.assertEqual(len(self.tester.students), 25, "25 students are created")  # tests that there are 25 students

    def test_rule_special_student_flagging(self):
        special_students = [s for s in self.tester.students if s.is_special]  # number of special students
        self.assertEqual(len(special_students), 2, "2 students are special")

    def test_neighbour_checker_logic(self):
        # 2 examples students
        student_t1 = Student('S1', test='T1')
        student_t2 = Student('S2', test='T2')
        
        self.assertTrue(self.tester.neighbour_checker(2, 2, student_t1))  # checking neighbours and insertion in empty grid

        self.tester.grid[2][1] = student_t1  # neighbour on the left
        self.assertFalse(self.tester.neighbour_checker(2, 2, student_t1), "left neighbor has same test")

        self.tester.grid = [[None]*5 for _ in range(5)] # grid reset
 
        self.tester.grid[1][1] = student_t1 # student in 1,1
        self.assertFalse(self.tester.neighbour_checker(2, 2, student_t1), "top right diagonal neighbour has same test")
        
        self.tester.grid = [[None]*5 for _ in range(5)] # grid reset

        self.tester.grid[3][3] = student_t2 # student in 3,3
        self.assertTrue(self.tester.neighbour_checker(2, 2, student_t1), "bottom right has a different test")


if __name__ == '__main__':
    unittest.main()