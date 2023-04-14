import flexibleTableOutput
#ДА Я ЗНАЮ ЧТО КОД ПОЧТИ ПОВТОРЯЕТСЯ В ПЕРВЫХ ДВУХ СЛУЧАЯХ, весь код можно раза в три сократить, но т.к я его сделал за один неполнй день и нету времени на отладку, считаю не критично
#этот файл пилил в последнюю очередь, 2 ночи, вдохновения не особо нет
class example5:
    def order1(book, countStudents):#сортировать ID в порядке возрастания
        sheet = book["Sheet1"]
        td0 = []
        for i in range(2, 41):
            main_value = [str(sheet["A" + str(i)].value)]
            # просто сортируем все ячейки A
            td0 = td0 + main_value
        td0 = sorted(td0)# это просто список отсортированных ID пользователей
        print(td0)
        td = []
        main_value = []
        for j in range(39):#для каждого случая находим совпадение по порядку, и эту строку только после этого добавляем, и таким образом все отсортировано
            for i in range(2, (countStudents + 2)):
                main_value = [str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value),
                              str(sheet["C" + str(i)].value)[:10], str(sheet["D" + str(i)].value),
                              str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value),
                              str(sheet["G" + str(i)].value), str(sheet["H" + str(i)].value),
                              str(sheet["I" + str(i)].value), str(sheet["J" + str(i)].value),
                              str(sheet["K" + str(i)].value)]
            # в верхней строке у C столбика вырезал значения часов минут и секнунд (00:00:00)
                if main_value[0] == td0[j]:
                    td = td + main_value#ну если этоо работает значит я гений              с первой попытки  (´｡• ω •｡`)
                    continue

        flexibleTableOutput.example6.readTableF(book, td)
        print("есть1")
    def order2(book, countStudents):#сортировать по фамилии
        sheet = book["Sheet1"]
        td0 = []
        for i in range(2, 41):
            main_value = [str(sheet["B" + str(i)].value)]
            # просто сортируем все ячейки B
            td0 = td0 + main_value
        td0 = sorted(td0)  # это просто список отсортированных ДР пользователей
        print(td0)
        td = []
        main_value = []
        for j in range(
                39):  # для каждого случая находим совпадение по порядку, и эту строку только после этого добавляем, и таким образом все отсортировано
            for i in range(2, (countStudents + 2)):
                main_value = [str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value),
                              str(sheet["C" + str(i)].value)[:10], str(sheet["D" + str(i)].value),
                              str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value),
                              str(sheet["G" + str(i)].value), str(sheet["H" + str(i)].value),
                              str(sheet["I" + str(i)].value), str(sheet["J" + str(i)].value),
                              str(sheet["K" + str(i)].value)]
                # в верхней строке у C столбика вырезал значения часов минут и секнунд (00:00:00)
                if main_value[1] == td0[j]:#здесь просто сравниваем уже слоты B
                    td = td + main_value
                    continue

        flexibleTableOutput.example6.readTableF(book, td)
        print("есть2")
    def order3(book, countStudents):#Вывести определенный пол
        sheet = book["Sheet1"]
        td0 = []#список "гендеров" которые мы распознали в таблице
        main_value = []
        for i in range(2, 41):
            main_value = str(sheet["D" + str(i)].value)
            #print(main_value)
            if main_value not in td0:
                td0= td0 + [main_value] #если такого варианта не было, то прямо тут добовляем
           #     print(td0)

        print(f"Были найдены следующие гендеры:{td0}\nКакой вывести?")
        #print(td0[0], td0[1])
        pasway = 0
        while pasway == 0:
            gender = input()
            if gender not in td0:
                print("ответ неприемлем")
            else:
                pasway = 1
        print("гендер выбран")


        td = []
        main_value = []
        for i in range(2, (countStudents + 2)):
            main_value = [str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value),
                          str(sheet["C" + str(i)].value)[:10], str(sheet["D" + str(i)].value),
                          str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value),
                          str(sheet["G" + str(i)].value), str(sheet["H" + str(i)].value),
                          str(sheet["I" + str(i)].value), str(sheet["J" + str(i)].value),
                          str(sheet["K" + str(i)].value)]

            if main_value[3] == gender:  # сравниваем ячейку гендера с выбранным пользователем
                td = td + main_value


        flexibleTableOutput.example6.readTableF(book, td)
        print("есть3")
    def order4(book, countStudents):#Вывести определенный факультет
        sheet = book["Sheet1"]
        td0 = []  # список факультетов которые мы распознали в таблице
        main_value = []
        for i in range(2, 41):
            main_value = str(sheet["F" + str(i)].value)
            # print(main_value)
            if main_value not in td0:
                td0 = td0 + [main_value]  # если такого варианта не было, то прямо тут добовляем
        #     print(td0)

        print(f"Были найдены следующие факультеты:{td0}\nКакой вывести?")
        # print(td0[0], td0[1])
        pasway = 0
        while pasway == 0:
            gender = input()#переменная гендр, но это не важно, тут мы получаем факультет. ДА ЭТО НЕ ПРОФЕССИОНАЛЬНО, потому что другой человек может запутаться, но вы меня еще не приняли, имею право опустить эти формальности
            if gender not in td0:
                print("ответ неприемлем")
            else:
                pasway = 1
        print("факультет выбран выбран")

        td = []
        main_value = []
        for i in range(2, (countStudents + 2)):
            main_value = [str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value),
                          str(sheet["C" + str(i)].value)[:10], str(sheet["D" + str(i)].value),
                          str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value),
                          str(sheet["G" + str(i)].value), str(sheet["H" + str(i)].value),
                          str(sheet["I" + str(i)].value), str(sheet["J" + str(i)].value),
                          str(sheet["K" + str(i)].value)]

            if main_value[5] == gender:  # сравниваем ячейку гендера с выбранным пользователем
                td = td + main_value

        flexibleTableOutput.example6.readTableF(book, td)
        print("есть4")
    def order5(book, countStudents):#Вывести определенный формат обучения (очно/заочно)
        print("ну там эта команда аналогична с четвертой (надеюсь вы запускаете эту команду уже после предыдущих четырех(＾▽＾) ). КСТАТИ можно это было бы реализвать в 2 функции, а не в 5 повторяющихся блоков кода, но проект небольшой, не критично, проще ctrl+c код")
    def order6(book, countStudents):#для выхода из проги
        print("выходим. тут он немного костыльно сделан, но свою функцию выполняет")