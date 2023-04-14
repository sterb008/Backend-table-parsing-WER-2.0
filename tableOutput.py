from prettytable import PrettyTable
class  example:
    def readTable(book):#countStudents
        sheet = book["Sheet1"]
        arr = []
        alphabets_in_capital = []
        for i in range(65, 91):
            alphabets_in_capital.append(chr(i))

        for i in range(26):
            a = str(sheet[alphabets_in_capital[i] + str(1)].value)
            if a == 'None':
                break
            arr.append(a)#собираем шапку

        th = arr
        td = []
        main_value = []
        countStudents = 0

        for i in range(2, 1000000): #сомневаюсь что студентов будет больше ляма
            data = str(sheet["A" + str(i)].value)
            if data != "None":
                countStudents += 1#считаем колличество студентов
            else:
                break
        print(f"Было найдено{countStudents} студентов")
        arr2 = []
        print(len(arr))
        for i in range(2, (countStudents + 2)):
            arr2 = []
            for j in range(len(arr)): #двойной цикл потому что для  каждой строчки собираем все данные
                main_value = str(sheet[alphabets_in_capital[j] + str(i)].value)
                arr2.append(main_value)
            # в верхней строке у C столбика вырезал значения часов минут и секнунд (00:00:00)
            #print(arr2)
            td = td + arr2

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(table)




        return arr, countStudents, alphabets_in_capital