#4.3
# for a in range(1,21,2):
#     print(a)

# list1=list(range(1,1000000))
# # for a in list1:
# #     print(a)
# print(min(list1),max(list1))
# print(sum(list1))

# list2=[a for a in range(3,31) if a%3==0 ]
# print(list2)
# list2=[]
# for a in range(3,31):
#      if a%3==0:
#           list2.append(a)
# print(list2)
    
# list3=[a**3 for a in range(1,11)]
# print(list3)

# def city_country(city,country):
#      print(f"{city},{country}")
# city_country('shanghai','china')

def food(*args):
     
     print('food contains',args)
food(1,2,3,4)