#mylist = [34, 3, 1, 51, 6, 33, 23, 2, 29, 5, 33, 1, 7, 65, 4, 12, 5, 7, 46, 3, 41, 15, 3, 23, 2, 1, 3, 21, 35, 4, 6, 2, 13, 5, 14, 10, 3, 25, 7, 13, 14, 7, 5, 33, 21]

#def multiplyList(myList) :
     
    # Multiply elements one by one
 #   result = 1
 #   for x in myList:
#         result = result * x
#    return result
     
#print(multiplyList(mylist))


my_list = [34, 3, 1, 51, 6, 33, 23, 2, 29, 5, 33, 1, 7, 65, 4, 12, 5, 7, 46, 3, 41, 15, 3, 23, 2, 1, 3, 21, 35, 4, 6, 2, 13, 5, 14, 10, 3, 25, 7, 13, 14, 7, 5, 33, 21]
odd_product = 1
even_product = 1

#5
for i in my_list:
    if(i % 2 == 0):
        even_product *= i
    else:
        odd_product *= i

#6
print("Product of all odd numbers: ", odd_product)