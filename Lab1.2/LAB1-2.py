from openpyxl import load_workbook
from matplotlib import pyplot
from matplotlib import figure
# Создаёт таблицу ексель как целое, в качестве аргумента передаётся имя эксель файла.
# Должен лежать в том же каталоге. Этот объект - словарь.
wb = load_workbook('data_analysis_lab.xlsx')
# Загрузить лист с именем "Data" в переменную sheet
sheet = wb['Data']
# Получить содержимое колонки A в виде списка
#sheet['A'][1:]
# Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
colYears = sheet['A'][1:]
colTemp = sheet['C'][1:]
colSunActivity = sheet['D'][1:]
def getvalue(x):
    return x.value
#Вывести из колонги Годы ячейку с индексом 3. Т.е. А3 из Эксель
#print(getvalue(colYears[3]))

#Присвоим переменным значения столбцов
valueYears = list(map(getvalue, colYears))
valueSun = list(map(getvalue, colSunActivity))
valueTemp = list(map(getvalue, colTemp))
# Вывести значения столбца А списком
#print(list(valueA))

## График не выводился, когда в значениях pyplot.plot стоял
## вывод списков переменных
## pyplot.plot(list(valueYears), list(valueTemp), label="Temperature")

#Построение графиков (ось X, ось Y, лейбл)
pyplot.plot(valueYears, valueTemp, label="Temperature")
pyplot.plot(valueYears, valueSun, label="Sun Activity")
figure.canvas.set_window_title('Test')

#Добавляем подписи
pyplot.xlabel('Years')
pyplot.ylabel('Temp/Sun Activity')
pyplot.legend(loc='upper left')

# Вывод графика
pyplot.show()

#pyplot.plot(list_x, list_y, label="Метка")  # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y pyplot.show() # показать график