class Matrices:
    def __init__(self, matrix1, matrix2, math):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.math = math

        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        if math == 'multiply':
            result = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

        if math == 'add' or math == 'subtract' or math == 'multiply':
            for l in range(len(matrix1)):
                for i in range(len(result)):
                    for j in range(len(matrix1)):
                        if math == 'add':
                            result[i][j] = matrix1[i][j] + \
                                matrix2[i][j]
                        if math == 'subtract':
                            result[i][j] = matrix1[i][j] - \
                                matrix2[i][j]
                        if math == 'multiply':
                            result[i][j] = matrix1[i][j] * \
                                matrix2[i][j]

            for r in result:
                print(r)
