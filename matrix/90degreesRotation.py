# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

class Rotate:
    def rotate90Right(self, matrix):
        matrixSize = len(matrix)
        if (matrixSize == 0): return matrix

        for i in range(0, int(matrixSize / 2)):
            for j in range(i, matrixSize - 1  - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[matrixSize - j - 1][i]
                matrix[matrixSize - j - 1][i] = matrix[matrixSize - i - 1][matrixSize - j - 1]
                matrix[matrixSize - i - 1][matrixSize - j - 1] = matrix[j][matrixSize - i - 1]
                matrix[j][matrixSize - i - 1] = temp

        return matrix

print(Rotate().rotate90Right([[1,2,3], [4,5,6], [7,8,9]]))
print(Rotate().rotate90Right([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))

# 123
# 456
# 789

741
852
963