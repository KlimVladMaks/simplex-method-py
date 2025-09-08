# Для реализации симплекс-метода использовался алгоритм с сайта:
# https://programforyou.ru/calculators/simplex-method

import copy


"""
Заметки:
- Если какое-либо из значений столбца b отрицательно, то решения задачи не существует.
"""


class SimplexMethod:

    def solve(self, task_table: list[list]):
        """
        Решает задачу линейного программирование, используя симплекс-метод.

        Пример:

        Для системы вида:

        F = 20*x_1 + 20*x_2 + 10*x_3 -> max
        -4*x_1 - 3*x_2 - 2*x_3 + x_4 = -33
        -3*x_1 - 2*x_2 - 1*x_3 + x_5 = -23
        -1*x_1 - 1*x_2 - 2*x_3 + x_6 = -12

        (Доступны две цели задачи: "max" и "min")

        Нужно передать следующую таблицу:

        task_table = [
            [20, 20, 10, 0, 0, 0, "max"]
            [-4, -3, -2, 1, 0, 0, -33],
            [-3, -2, -1, 0, 1, 0, -23],
            [-1, -1, -2, 0, 0, 1, -12]
        ]

        Примечание:

        В таблице должен быть
        """
        # Коэффициенты целевой функции (coefficients)
        self.c = task_table[0].copy()
        self.c.pop()

        # Цель задачи (найти максимум или минимум) (objective)
        self.obj = task_table[0][-1]

        # Симплекс-таблица (simplex table)
        self.st = copy.deepcopy(task_table[1:])

        # Размер базиса (число условий)
        self.basis_size = len(self.st)

        # Избавляемся от отрицательных свободных коэффициентов
        for row in self.st:
            if row[-1] < 0:
                self._get_rid_of_negative_free_coefficients()
                break
        
        # Дельты симплекс-таблицы для оптимизации решения
        self.deltas = [None for _ in range(len(self.st[0]) - 1)]

        # Цикл оптимизации с помощью дельт
        while True:
            # Рассчитываем дельты
            self._calculate_deltas()

            # Проверяем решение на оптимальность
            if self._checking_all_deltas(self.obj):
                break
            
            # Ищем разрешающий столбец
            resolution_column_j = None

            # При заданном условии "max" - ищем столбец с минимальной дельтой
            if self.obj == "max":
                resolution_column_j = self.deltas.index(min(self.deltas))

            # При заданном условии "min" - ищем столбец с максимальной дельтой
            elif self.obj == "min":
                resolution_column_j = self.deltas.index(max(self.deltas))
            
            # Рассчитываем симплекс-отношения Q
            q = self._calculate_simplex_relations_of_q(resolution_column_j)

            # Ищем строку с минимальным Q (разрешающая строка)
            # (Элемент на пересечении разрешающих столбца и строки также называется разрешающим)
            row_with_min_q_i = None
            q_min = float("inf")
            for i in range(len(q)):
                if (not (q[i] is None)) and (q[i] < q_min):
                    row_with_min_q_i = i
                    q_min = q[i]
            
            # Приводим разрешающий элемент к единице, а все остальные элементы в разрешающем столбце к нулю
            self._dividing_row_in_simplex_table(row_with_min_q_i, self.st[row_with_min_q_i][resolution_column_j])
            self._zero_out_other_items_in_the_column(row_with_min_q_i, resolution_column_j)
    
        # Формируем ответ в виде: [[<Значения x_1, x_2, x_3, ...>], <Значение целевой функции F>]
        answer = [[0 for _ in range(len(self.c))], None]

        # Находим значения переменных x_1, x_2, x_3, ...
        basis_indexes = self._get_basis_indexes()
        i = 0
        for bi in basis_indexes:
            answer[0][bi] = self.st[i][-1]
            i += 1
        
        # Находим значение целевой функции F
        f = 0
        for i in range(len(self.c)):
            f += self.c[i] * answer[0][i]
        answer[1] = f

        return answer

    def _get_rid_of_negative_free_coefficients(self):
        """
        Избавляется от отрицательных свободных коэффициентов b.
        """
        while True:
            # Найдём строку с минимальной отрицательной b
            i_min = self._find_row_with_smallest_negative_b()
            # Если такой строки нет, значит все свободные коэффициенты положительны
            if i_min is None:
                return

            # Найдём в строке i_min минимальный отрицательный элемент
            j_min = self._find_minimum_negative_item_in_row(i_min)
            if j_min is None:
                raise Exception("В строке нет отрицательных значений!")
            
            # Делим строку на найденный элемент
            self._dividing_row_in_simplex_table(i_min, self.st[i_min][j_min])

            # Обнуляем все другие элементы в этом столбце
            self._zero_out_other_items_in_the_column(i_min, j_min)

    def _find_row_with_smallest_negative_b(self):
        """
        Находит строку с минимальным отрицательным b.
        """
        b_min = 0
        i_min = None
        for i in range(len(self.st)):
            if self.st[i][-1] < b_min:
                b_min = self.st[i][-1]
                i_min = i
        return i_min

    def _find_minimum_negative_item_in_row(self, i):
        """
        Находит минимальный отрицательный элемент в строке.
        """
        row = self.st[i][:-1]
        min_element = 0
        j_min = None
        for j in range(len(row)):
            if row[j] < min_element:
                min_element = row[j]
                j_min = j
        return j_min
    
    def _dividing_row_in_simplex_table(self, row_i, divisor):
        """
        Делит строку в таблице на заданное значение.
        """
        row = self.st[row_i]
        for j in range(len(row)):
            row[j] = row[j] / divisor

    def _zero_out_other_items_in_the_column(self, i, j):
        """
        Приводит к нулю все элементы столбца кроме заданного.
        """
        for row_i in range(len(self.st)):
            if row_i == i:
                continue
            row = self.st[row_i]
            subtraction_coeff = row[j]
            for k in range(len(row)):
                row[k] = row[k] - (self.st[i][k] * subtraction_coeff)

    def _calculate_deltas(self):
        """
        Рассчитывает дельты для симплекс-таблицы.
        """
        coeffs_indexes = self._get_basis_indexes()
        coeffs = []
        for ci in coeffs_indexes:
            coeffs.append(self.c[ci])
        for j in range(len(self.st[0]) - 1):
            delta_j = 0
            for i in range(len(self.st)):
                delta_j += self.st[i][j] * coeffs[i]
            delta_j -= self.c[j]
            self.deltas[j] = delta_j

    def _get_basis_indexes(self):
        """
        Возвращает базис симплекс-таблицы.
        """
        coeffs_indexes = [None for _ in range(len(self.st))]
        for j in range(len(self.st[0])):
            one_i = None
            one_count = 0
            is_only_one_and_zeros = True
            for i in range(len(self.st)):
                if self.st[i][j] == 1:
                    one_i = i
                    one_count += 1
                    if one_count > 1:
                        is_only_one_and_zeros = False
                        break
                elif self.st[i][j] != 0:
                    is_only_one_and_zeros = False
                    break
            if is_only_one_and_zeros and one_count == 1:
                coeffs_indexes[one_i] = j
                if None not in coeffs_indexes:
                    return coeffs_indexes

    def _checking_all_deltas(self, obj):
        """
        Проверяет оптимальность решения с помощью дельт.
        """
        for delta in self.deltas:
            if ((delta > 0) and (obj == "min")) or ((delta < 0) and (obj == "max")):
                return False
        return True
            
    def _calculate_simplex_relations_of_q(self, j):
        """
        Рассчитывает симплекс-отношения Q.
        """
        q = []
        for i in range(len(self.st)):
            if self.st[i][j] <= 0:
                q.append(None)
                continue
            q.append(self.st[i][-1] / self.st[i][j])
        return q
