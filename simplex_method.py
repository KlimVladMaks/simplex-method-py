# Для реализации симплекс-метода использовался алгоритм с сайта:
# https://programforyou.ru/calculators/simplex-method

import re


class SimplexMethod:
    """
    Класс для реализации симплекс-метода для решения задачи линейного программирования (ЗЛП).
    """
    def __init__(self):
        """
        Метод для инициализации класса.
        """
        # Список коэффициентов целевой функции
        self.objective_coefficients: list[int]

        # Направление оптимизации ('max' или 'min')
        self.objective_sense: str

        # Матрица с коэффициентами ограничений
        self.constraint_matrix: list[list[int]]

        # Список с типами ограничений ('>=', '<=', '=')
        self.constraint_senses: list[str]

        # Список с правыми частями ограничений
        self.constraint_rhs = list[int]

        # Таблица с ЗЛП в каноническом виде (в ограничениях используются только равенства)
        # Пример:
        # [20, 20, 10, 0, 0, 0, "max"]
        # [-4, -3, -2, 1, 0, 0, -33],
        # [-3, -2, -1, 0, 1, 0, -23],
        # [-1, -1, -2, 0, 0, 1, -12]
        self.canonical_problem_table: list[list]
    

    def load_problem(self, file_path: str) -> None:
        """
        Метод для загрузки ЗЛП. На вход принимает путь до txt-файла с ЗЛП.
        Пример ожидаемого формата в txt-файле:

        ```
        2x1 +3x2 +x3 +4x4 -> max
        x1 +x2 +x3 +x4 <= 10
        2x1 +x2 -x3 +x4 = 8
        x2 +2x3 +x4 >= 5
        ```
        """

        # === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===

        # Паттерн для извлечения коэффициента и индекса X из строки
        pattern = re.compile(r'^([+-]?)(\d*)x(\d+)$')

        def parse_coefficient_index(s: str) -> tuple[int,int]:
            """
            Функция для извлечения коэффициента и индекса X из строки.
            Примеры работы:
            ```
            "2x1" -> (2, 1)
            "+3x2" -> (3, 2)
            "+x3" -> (1, 3)
            "-x3" -> (-1, 3)
            "-5x4" -> (-5, 4)
            "x6" -> (1, 6)
            ```
            """
            m = pattern.match(s)
            sign, coefficient, index = m.groups()
            coefficient = int(coefficient) if coefficient else 1
            if sign == '-':
                coefficient = -coefficient
            
            # В Python индексы начинаются с нуля, так что возвращаем (index - 1)
            return coefficient, int(index) - 1

        # ===============================
        
        # Считываем все непустые строки из txt-файла, убирая '\n' и лишние пробелы по краям
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() != '']
        
        # Строка с целевой функцией
        objective_function = lines[0]
        
        # Разбиваем строку с целевой функцией на отдельные элементы
        objective_function = objective_function.split()
        
        # Удаляем элемент '->' (он не нужен для дальнейших расчётов)
        objective_function.pop(-2)

        # Направление оптимизации ('max' или 'min')
        objective_sense = objective_function.pop(-1)

        # Преобразуем элементы-строки в картежи вида (коэффициент, индекс)
        # Пример преобразования элемента: "-5x4" -> (-5, 4)
        for i in range(len(objective_function)):
            objective_function[i] = parse_coefficient_index(objective_function[i])

        # Получаем число значимых переменных
        number_of_variables = max(i for _, i in objective_function) + 1

        # Создаём список для коэффициентов целевой функции
        # (изначально заполняем его нулями)
        objective_coefficients = [0 for _ in range(number_of_variables)]

        # Заполняем список коэффициентами целевой функции
        # ci - (coefficient, index)
        for ci in objective_function:
            objective_coefficients[ci[1]] = ci[0]
        
        # Список со строками с ограничениями
        constraints = lines[1:]

        # Разбиваем строки с ограничениями на отдельные элементы
        for i in range(len(constraints)):
            constraints[i] = constraints[i].split()
        
        # Список с типами ограничений ('>=', '<=', '=')
        constraint_senses = []

        # Список с правыми частями ограничений
        constraint_rhs = []

        # Заполняем списки с типами и правыми частями ограничений
        for c in constraints:
            constraint_senses.append(c.pop(-2))
            constraint_rhs.append(int(c.pop(-1)))
        
        # Преобразуем оставшиеся элементы в формат (коэффициент, индекс)
        for c in constraints:
            for i in range(len(c)):
                c[i] = parse_coefficient_index(c[i])
        
        # Создаём матрицу с коэффициентами ограничений
        # (изначально заполняем её нулями)
        constraint_matrix = []
        for _ in range(len(constraints)):
            constraint_matrix.append([0 for _ in range(number_of_variables)])
        
        # Заполняем матрицу с коэффициентами ограничений соответствующими значениями
        for row_i in range(len(constraints)):
            for ci in constraints[row_i]:
                constraint_matrix[row_i][ci[1]] = ci[0]
        
        # Загружаем полученные параметры ЗЛП в глобальные переменные класса
        self.objective_coefficients = objective_coefficients
        self.objective_sense = objective_sense
        self.constraint_matrix = constraint_matrix
        self.constraint_senses = constraint_senses
        self.constraint_rhs = constraint_rhs

        # Преобразуем параметры ЗЛП к каноническому виду
        self._convert_problem_to_canonical_form()

        
    def _convert_problem_to_canonical_form(self):
        """
        Преобразует ЗЛП к каноническому виду и записывает в единую таблицу для дальнейшей работы.
        """
        pass
