d ={1:"python",2:"c++",3:"java",'name':"python programming" , 4:{1:"one",2:"two",3:"three",4:"four" }}
# print(d[4])
# print(d[4][2])
# d[5] = "Akshit"
# print(d[5])
#
# #delete any element
# del d[3]
# print(d)
#
# #copy dict
# d2 = d.copy()
# print(d2)
#
# #empty an dict
# # d.clear()
# print(d)
#
# #To print key
# print(d.keys())


#update value
# d.update({1: "c+"})
# print(d)

# d1 = {1:"python",2:"c++",3:"java",4:"python"}
# d2 = {11:"one",12:"two",13:"three", 14: "four"}
# d2.update(d1)
# print(d2)

#stack
# print("stack")

#tuple
# mytuple = ("apple", "banana", "cherry")
# print(mytuple)
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))
# print(type(thistuple))
#
# for x in thistuple:
#     print(x)


# t = (10,11,12)
# del(t)

# t1 = (1,2,3,4,5,1)
# print(min(t1))
# print(max(t1))
# print(len(t1))
# print(t1.count(1))

#set
#unorderd
#unchangeable
#unindexing
#written with curly brackets.
# set = {"a","b","c","d","e","f","g","h"}
# print(set)
# set.add("i")
# print(set)
# set2 = {1,2,3,4,5}
# set3 = set2.union(set)
# print(set3)

# set1 = set()
# set2 = set()
# for i in range (1,5):
#     set1.add(i)
# for i in range (3,9):
#     set2.add(i)
# print(set1)
# print(set2)
# set3 = set1.union(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)
# def my_function(name):
#     print("hello", name)
#
# my_function("python")


# def my_fun(*city):
#     print(city)
#     l =len(city)
#     print("last city is:",city[l-1])
#     print("first city is:",city[0])
# my_fun("SWM","Ajmer" ,"kota")

#use ** When unknown key words??

# def fun(**city):
#     print(city['s'])

#file handling
file = open("new1.txt","w")
file.write("My self Akshit")
file.write("\ni love my family including khushi")


file.close()
f = open("new1.txt","r")
for x in f:
    print(x)

with open("new1.txt","r") as f1:
    data = f1.read()
    print(data)



















