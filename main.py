import glob, os #поиск ФАЙЛА АВТОМАТИЧЕСКИ
import chooseOne
import chooseTwo
import tableOutput
mainFolder = os.getcwd()
print("ВНИМАНИЕ\n программа предазначена для работы с файлами в текущей дериктории (где лежит main или exe). ПРи попытке обращения к таблице, находящейся в другой папке, программа не сможет ее обнаружить")

nameFile, book = chooseOne.example3.choose1(mainFolder)

arr, countStudents, alphabets_in_capital = tableOutput.example.readTable(book)


#print(f"Были найдены следующие категории: {arr}\nКакой будем сортировать?")
correct = 0
while correct == 0:
    print(f"Были найдены следующие категории: {arr}\nКакой будем сортировать? (нажмите 0 для выхода)")
    way = input()  # выбор пользователя
    if way == "0":
        break
    elif way not in arr:
        print("нет такой категории")
        continue

    else:
        for i in range(len(arr)):
            if arr[i] == way:
                print(f"был выбран пункт {i+1}")
                row = i
                chooseTwo.example4.choose2(row, book, countStudents, alphabets_in_capital, arr)
                break


#def sortRow(row):
#sheet = book["Sheet1"]
