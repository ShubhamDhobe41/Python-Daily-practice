list1=[1,3,4,5,6,7,6]

# square_list =[]
# for item in list1:
#     square_list.append(item*item)
# print(square_list)



# better way use list comprension
squred_list = [i*i for i in list1]
print(squred_list)