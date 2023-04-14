#import functionTwo
import flexibleTableOutput
class example4:
    def choose2(row, book, countStudents, alphabets_in_capital, arr):
        sheet = book["Sheet1"]
        td0 = []
        for i in range(2, countStudents+2):
            main_value = [str(sheet[alphabets_in_capital[row] + str(i)].value)]

            td0 = td0 + main_value #полученные данные из конкретного столбика выбранного
        #print(td0)
        correct = 0
        td01 = []
        for item in td0:
            if  item not in td01:
                td01.append(item)#полученные данные из конкретного столбика выбранного, только убрали повторки
        if len(td01) < len(td0):
            print("!!!!!!!!!!!!!!!!!!!ВНИМАНИЕ!!!!!!!!!!!!!!!!!!! \n найдены совпадения в столбцах. если вы попробуете вывести сортировку алфовитом, это приведет к ошибке программы. Уже 2 ночи, сил нет исправлять.\nесли сортируем к римеру ID студентов или фамилии, и прочую индивидуальную информацию по алфавиту (КОТОРАЯ НЕ ПОВТОРЯЕТСЯ), то все работает\n!!!!!!!!!!!!!!!!!!!ВНИМАНИЕ!!!!!!!!!!!!!!!!!!!")
        while correct == 0:
            print(f"Нйденные варианты:{td01}\nБудем сортировать по алфавиту(1), или вывести конкретное значение(2)??")
            mainWay = str(input())
            if mainWay != "1" and mainWay != "2":
                print("введены некорректные значения")
                continue
            else:
                correct = 1


        if mainWay == "1":
            td01 = sorted(td01)  # это просто список отсортированных
            print(td01)
            td = []
            main_value = []
            #print(len(arr))
            for j in range(countStudents):  # для каждого случая находим совпадение по порядку, и эту строку только после этого добавляем, и таким образом все отсортировано
            #    td = []
                for i in range(2, (countStudents + 2)):
                    arr2 = []
                    for k in range(len(arr)):  # двойной цикл потому что для  каждой строчки собираем все данные
                        main_value = str(sheet[alphabets_in_capital[k] + str(i)].value)
                    #    print(alphabets_in_capital[k])
                        arr2.append(main_value)

                #    td = td + arr2

                    if arr2[row] == td01[j]:
                        td = td + arr2  # ну если этоо работает значит я гений              с первой попытки  (´｡• ω •｡`)
                        continue

            flexibleTableOutput.example6.readTableF(arr, td)
            print("есть1")
        else:
            correct = 0
            td = []
            while correct == 0:
                print(f"Какое из нижеперечисленных вывести?\n{td01}")
                way = input()  # выбор пользователя
                if way not in td01:
                    print("нет такого пункта")
                    continue
                else:
                    for i in range(len(td01)):
                        if td01[i] == way:
                            print(f"был выбран пункт {td01[i]}({i + 1})")
                            row01 = i

                    for i in range(2, (countStudents + 2)):
                        arr2 = []
                        for j in range(len(arr)):  # двойной цикл потому что для  каждой строчки собираем все данные
                            main_value = str(sheet[alphabets_in_capital[j] + str(i)].value)
                            arr2.append(main_value)
                        # в верхней строке у C столбика вырезал значения часов минут и секнунд (00:00:00)
                        # print(arr2)
                    #    td = td + arr2

                        if arr2[row] == td01[row01]:
                            td = td + arr2
                            continue
                    flexibleTableOutput.example6.readTableF(arr, td)
                    correct = 1




