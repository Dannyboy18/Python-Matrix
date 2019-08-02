import unittest

from matrix import Matrix


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class MatrixTest(unittest.TestCase):
    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    def test_can_extract_row(self):
        matrix = Matrix("1 2\n3 4")
        self.assertEqual(matrix.row(2), [3, 4])

    def test_extract_row_where_numbers_have_different_widths(self):
        matrix = Matrix("1 2\n10 20")
        self.assertEqual(matrix.row(2), [10, 20])

    def test_can_extract_row_from_non_square_matrix(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.row(3), [7, 8, 9])

    def test_extract_column_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.column(1), [1])

    def test_can_extract_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
        self.assertEqual(matrix.column(3), [3, 6, 9])

    def test_can_extract_column_from_non_square_matrix(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.column(3), [3, 6, 9, 6])

    def test_extract_column_where_numbers_have_different_widths(self):
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        self.assertEqual(matrix.column(2), [1903, 3, 4])

    def test_equal(self):
        Matrix1 = Matrix("1 2\n3 4")
        Matrix2 = Matrix("1 2\n3 4")
        self.assertEqual(Matrix1,Matrix2)

    def test_not_equal(self):
        Matrix1 = Matrix("1 2\n3 4")
        Matrix2 = Matrix("1 2\n3 5")
        self.assertNotEqual(Matrix1, Matrix2)

    def test_addition(self):
        matrix1 = Matrix("1 2\n3 4")
        matrix2 = Matrix("3 4\n5 6")
        matrix_result = Matrix("4 6\n8 10")
        self.assertEqual(matrix1.add(matrix2), matrix_result)

    def test_addition_reversed(self):
        matrix1 = Matrix("1 2\n3 4")
        matrix2 = Matrix("3 4\n5 6")
        matrix_result = Matrix("4 6\n8 10")
        self.assertEqual(matrix2.add(matrix1), matrix_result)

    def test_addition_with_different_row_length(self):
        matrix1 = Matrix("1 2\n3 4")
        matrix2 = Matrix("3 4 1\n5 6 1")
        with self.assertRaises(Exception):
            matrix1.add(matrix2)

    def test_addition_with_different_row_count(self):
        matrix1 = Matrix("1 2\n3 4")
        matrix2 = Matrix("3 4\n5 6\n7 8")
        with self.assertRaises(Exception):
            matrix1.add(matrix2)

    def test_subtraction(self):
        matrix1 = Matrix("1 2\n3 4")
        matrix2 = Matrix("3 4\n5 6")
        matrix_result = Matrix("-2 -2\n-2 -2")
        self.assertEqual(matrix1.subtract(matrix2), matrix_result)

    def test_mult(self):
        matrixA = Matrix("3 4 5\n2 1 3\n2 4 1")
        matrixB = Matrix("1 2\n2 3\n2 3")
        matrix_result = Matrix("21 33\n10 16\n12 19")
        self.assertEqual(matrixA.multiplication(matrixB), matrix_result)    

if __name__ == '__main__':
    unittest.main() 