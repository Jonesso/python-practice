import re


table1 = [
    ["Тимур А. Викли","2001.12.06", "+75707894170"],
    ["Ильдар О. Рокко","2001.08.10", "+72138254191"],
    ["Ильдар О. Рокко","2001.08.10", "+72138254191"],
    ["Рамиль В. Мукян","2001.12.18", "+76726199582"],
    ["Ильдар О. Рокко","2001.08.10", "+72138254191"],
    ["Константин Р. Чатов","2002.10.11", "+72134797435"]
    ]

table2 = [
    ["Вадим Ш. Вечицберг","2001.12.14", "+78930427521"],
    ["Адель К. Газумман","1999.04.07", "+70778997896"],
    ["Влад Н. Гадебянц","2001.05.17", "+70600640742"],
    ["Влад Н. Гадебянц","2001.05.17", "+70600640742"],
    ["Влад Н. Гадебянц","2001.05.17", "+70600640742"],
    ["Вячеслав Д. Цисалян","2001.07.23", "+73581848995"]
]


# функция для задания
def f23(table):
    
    sort(table)
    table = deleteDuplicates(table)
    renameElements(table)
    # for line in table:
    #     print(line)
    return(table)

# функция удаления повторяющихся строк
def deleteDuplicates(table):
    new_table = []
    for line in table:
        if line not in new_table:
            new_table.append(line)
    return new_table



# функция для организации сортировки таблицы по 3-ему элементу строки
def keyFunc(line):
   return line[2]

# функция сортировки
def sort(table):
    table.sort(key=keyFunc)

# функция приведения элементов к нужному формату
def renameElements(table):
    for line in table:
        for cell in  range(len(line)):
            # регулярное выражение для даты
            match = re.fullmatch(r'\d{4}\.\d{2}\.\d{2}',line[cell])
            if match:
                line[cell] = match[0][-2:]+"/"+match[0][-5:-3]+"/"+match[0][:4]
            # регулярное выражение для номера телефона
            match = re.fullmatch(r'\+\d+',line[cell])
            if match:
                line[cell] = match[0][:2]+" ("+match[0][2:5]+") "+match[0][5:8]+"-"+match[0][8:10]+"-"+match[0][10:]
            # регулярное выражение для имени
            match = re.fullmatch(r'\w+\s\w\.\s+\w+',line[cell])
            if match:
                line[cell] = match[0][:match[0].find(' ')]+match[0][match[0].find(' ')+3:]
    
            

# if __name__ =='__main__':
#     f23(table1)
    # f23(table2)