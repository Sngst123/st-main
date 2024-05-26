import multiprocessing

def multiply_row_col(row, col):
    # Умножение строки на столбец и возвращение результата
    return sum(row[i] * col[i] for i in range(len(row)))

def multiply_element(args):
    # Распаковка аргументов
    row, col = args
    return multiply_row_col(row, col)

def multiply_matrices(matrix1, matrix2):
    # Проверка совместимости матриц
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Несовместимые матрицы для умножения")

    # Транспонирование второй матрицы для более эффективного доступа к столбцам
    transposed_matrix2 = list(zip(*matrix2))

    # Создание пула процессов
    pool = multiprocessing.Pool()

    # Подготовка аргументов для умножения
    args = [(row, col) for row in matrix1 for col in transposed_matrix2]

    # Выполнение умножения матриц с использованием пула процессов
    result = pool.map(multiply_element, args)

    # Преобразование результата в матрицу
    result_matrix = [result[i:i+len(matrix2)] for i in range(0, len(result), len(matrix2))]

    # Завершение работы пула процессов
    pool.close()
    pool.join()

    return result_matrix

if __name__ == "__main__":
    # Пример матриц для умножения
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Умножение матриц
    result = multiply_matrices(matrix1, matrix2)
    print("Результат умножения матриц:")
    for row in result:
        print(row)
