# i = 0

# while i <= 10:
#     if i % 2 == 1: break 
#     print(i)
#     i+=1

#k  bezkanechno popitka
# while int(input('Enter number: ')) > 0:
#     pass

#k ogranichenie popitki (5)
#  for i in range(5):
#     if int(input('Enter number: ')) > 0:
#         break 



# print('Now you will be asked to enter 2 numbers that will be divided and the answer will be printed')
# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: Note that you cannot use 0 '))

# if b == 0:
#     i = 0
#     while True:
#         if i > 3:
#             print('O Stupid asshole. Do not you know math?')
#         else: print('Pleas enter non-zero value')
#         b =int(input('Enter 2nd number: Note that you cannot use 0'))
#         if b != 0:
#             print(a / b)
#             break 
#         i+=1 

# a = int(input('Enter 1st number: '))
# # b = int(input('Enter 2nd number: Note THAT YOU CANNOT USE 0:  '))
# i = 1
# while True:
#     b = int(input('Enter 2nd number: Note THAT YOU CANNOT USE 0:  '))
#     try:
#         print(a / b)
#         break 
#     except:
#         if i > 3: print('Blya ti chto tupoy?')
#         else: print('Please enter non-zero value')
# i+=1  


while True:
    try:
        a= int(input('Enter positive number: '))
        if a < 0: raise ValueError('You were asked to enter positive number: ')
        else: break
    except ValueError as ve:
        print(ve)
