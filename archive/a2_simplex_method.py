# Для реализации симплекс-метода использовался алгоритм с сайта:
# https://programforyou.ru/calculators/simplex-method

import re


class SimplexMethod:
    def __init__(self):
        pass

    def load_task(self, file_path):
        """
        Загружает задачу линейного программирования из файла.
        """
        pattern = re.compile(r'^\s*([+-]?\d*)x(\d+)\s*$')

        def parse_term(s: str) -> tuple[int,int]:
            """
            "+3x2" -> (3, 2)
            """
            m = pattern.match(s)
            if not m:
                raise ValueError(f"Неверный формат: {s!r}")
            coef_str, idx_str = m.groups()
            coef = int(coef_str) if coef_str not in ('', '+', '-') else (1 if coef_str in ('', '+') else -1)
            return coef, int(idx_str)

        def max_second(tuple_list):
            if not tuple_list:
                raise ValueError("Список пуст")
            return max(t for _, t in tuple_list)

        # Коэффициенты целевой функции
        objective_coeffs = []

        # Направление оптимизации
        objective_sense = ""

        # Матрица коэффициентов ограничений
        constraint_matrix = []

        # Список знаков ограничений
        constraint_senses = []

        # Правая часть ограничений
        constraint_rhs = []

        # Считываем строки из указанного файла
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() != '']

        # Строка с целевой функцией
        objective_function_str = lines[0]

        # Список строк с ограничениями
        constraints_str = lines[1:]

        # Список с компонентами целевой функции
        objective_function_list = objective_function_str.split()

        # Удаляем строку "->" (в алгоритме она не нужна)
        objective_function_list.pop(-2)

        # Извлекаем направление оптимизации
        objective_sense = objective_function_list.pop(-1)

        # Преобразование вида "+3x2" -> (3, 2)
        for i in range(len(objective_function_list)):
            objective_function_list[i] = parse_term(objective_function_list[i])

        # Находим число значимых x
        number_var_x = max_second(objective_function_list)

        # Заполняем список с коэффициентами целевой функции
        objective_coeffs = [0 for _ in range(number_var_x)]

        for _ in range(len(constraints_str)):
            constraint_matrix.append([0 for _ in range(number_var_x)])
