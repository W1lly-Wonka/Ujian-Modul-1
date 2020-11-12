'''
create phone no
Jika dalam string terdapat alphabet, maka yang di-return adalah "Invalid input. No alphabet.".
Jika dalam string terdapat symbol, maka yang di-return adalah "Invalid input. No symbols.".
Jika panjang dari string kurang dari 10 digit atau lebih dari 10 digit, maka yang di-return adalah "Digits must be in length of 10, not more or less"
Jika dalam string terdapat digit di bawah 0 (negative value), maka yang di-return adalah, "Input only positive number"
'''

# def create_phone_number(number) :
#     angka = 0
#     x = 0
#     for a in number :
#         if type(a) == int :
#             angka += 1
#         if type(a) == str :
#             return 'Invalid input. No alphabet'
#         if a > 9 or a < 0  :
#             x += 1

#     if angka != len(number) :
#         return 'Just input the number'
#     elif x != 0 or x < 0 :
#         return 'Input only positive number'
#     elif len(number) == 10 :
#         no = '('
#         for a in range(0,3) :
#             no += str(number[a])
#         no += ') '
#         for a in range(3,6) :
#             no += str(number[a])
#         no += '-'
#         for a in range(6,len(number)) :
#             no += str(number[a])        
#         return no
#     else :
#         return 'Digits must be in length of 10, not more or less'

# print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

'''
Buatlah sebuah function bernama move_zeros. Function ini akan Memindahkan semua angka 0 ke sisi sebelah kanan list.
'''
# def moveZeros(array):
#     ListBaru=[]
#     ListIsiNol = []
#     for i in array:
#         if not isinstance(i, bool):
#             if i == 0:
#                 ListIsiNol.append(i)
#                 continue
#         ListBaru.append(i)
#     return ListBaru + ListIsiNol

# print(moveZeros([False,1,0,1,2,0,1,3,"a"]))
# print(moveZeros([0,0,0,"test",0,3,"a",True,False]))
# print(moveZeros([0,True,True,False,"a","b",1,1,1]))

'''
class statistic, 4 method
mean() : Untuk mencari rata-rata.
median() : Untuk mencari nilai tengah.
mode() : Untuk mencari nilai yang paling sering muncul (most frequent value). 
Jika terdapat satu value yang frekuensi (jumlah) kemunculannya sama dengan value yang lain,
maka mode akan me-return tidak ada modus.
std() : Untuk mencari nilai standard deviation atau simpangan baku. 
Rumus standard deviation yang digunakan adalah:

'''
# class statistic:

# x = [ 1,2,3,4,5,"a" ]
# x = [ 12,10,10,10,10 ]
# x = [ 4,5,2,1,6,7 ]

# # def getMean(list) :
#     sum = 0

#     for item in list :
#         sum += item

#     mean = sum / len(list)
#     return mean

# print(getMean(x))

# def getMedian(list) :
#     list.sort()
#     median = 0
#     if (len(list) % 2 != 0) :
#         median = list[(len(list) // 2)]
#     else :
#         mid1 = list[(int(len(list) / 2)) - 1]
#         mid2 = list[int(len(list) / 2)]
#         median = (mid1 + mid2) / 2
#     return median

# print(getMedian(x))

# def getMode(list) :
#     countList = []
#     # create countList
#     for num in list :
#         check = False
#         for list1 in countList :
#             if(list1[0] == num) :
#                 list1[1] += 1
#                 check = True
#         if(check == False) :
#             countList.append([num, 0])

# # create list of mode/s
#     maxFrequency = 0
#     modes = []
#     for list1 in countList :
#         if (list1[1] > maxFrequency) :
#             modes = [list1[0]]
#             maxFrequency = list1[1]
#         elif (list1[1] == maxFrequency) :
#             modes.append(list1[0])

# # if every value appears same amount of times
#     if (len(modes) == len(countList)) :
#         modes = []
#     return modes

# print(getMode(x))

# s = [ 1,2,3,4,5,"a" ]
# s = [ 12,10,10,10,10 ]
# s = [ 4,5,2,1,6,7 ]

# def standard_deviation(List):
#     avg = sum(List) * 1.0 / len(List)
#     variance = list( map( lambda x: (x - avg)**2, List) )
#     return ( sum(variance) * 1.0 / len(variance) ) ** 0.5
 
# print (standard_deviation(s))

