from prettytable import PrettyTable
class  example6:
    def readTableF(arr, td):#td это просто таблица ниже шапки, то есть список элементов попорядку, который я буду формировать в fiweWays
        #sheet = book["Sheet1"]
        #i = 1

    #    print(arr)
        th = arr
    #    td = []
    #    print(len(td))

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(table)