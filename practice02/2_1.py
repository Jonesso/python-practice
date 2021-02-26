#          x3
#     /   |      \
#    /    x2       x1
#   x2   / |     /  |   \
#  / |  x0 6   x0   x0  x2
# 10 9 / |    / |  / | / |
#      8 7   5  4  3 2 1 0

#          '0'
#     /   |      \
#    /   '2'       '3'
#  '1'   / |     /  |   \
#  / |  '4' 6  '5' '6'  '7'
# 10 9 / |    / |  / | / |
#      8 7   5  4  3 2 1 0


# словарь с обозначением вершины x[i] в ключ - номер вершины (см. схему сверху), значениями i и номерами
# вершин-наследников
convert_to_numbers_dict = {
    '0': [3, ['1', '2', '3']],
    '1': [2, [10, 9]],
    '2': [2, ['4', 6]],
    '3': [1, ['5', '6', '7']],
    '4': [0, [8, 7]],
    '5': [0, [5, 4]],
    '6': [0, [3, 2]],
    '7': [2, [1, 0]]}
# словарь со связями между вершинами
connection_dir = {0: ['tea', 'toml'], 1: ['raml', 'abap', 'volt'], 2: ['eagle', 'd'], 3: ['less', 'glyph', 'text']}


def f21(x):
    root = '0'
    root_x_num = 3
    # так как корень дерева - x[3], начну отталкиваться от него
    root_node = convert_to_numbers_dict[root][1][connection_dir[root_x_num].index(x[root_x_num])]
    return f21_recursive_part(x, root_node)


def f21_recursive_part(x, root_node):
    if root_node not in convert_to_numbers_dict.keys():
        return root_node
    else:
        current_index = convert_to_numbers_dict[root_node][0]
        return f21_recursive_part(x, convert_to_numbers_dict[root_node][1][
            connection_dir[current_index].index(x[current_index])])

# if __name__ == "__main__":
#     print(f21(['tea','volt','d','glyph']))
#     print(f21(['tea','volt','eagle','text']))
