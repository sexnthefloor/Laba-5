# [130]
# Перепишите элементы данного массива в новый массив,
# помещая в него сначала все отрицательные, затем нулевые и, нако¬нец, положительные элементы.
first_list = [5, -2, 3, 0, 2, 0, -9, -11, 4, 9, 1, -5, 0]
second_list = [i for i in first_list if i<0] + [i for i in first_list if i==0] + [i for i in first_list if i>0]
print (second_list)