# print("hello world")
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# tuple1=(19,12,15,34,54)
# print(tuple1)
# dict1={"name":"Jeet","age":18,"city":"Rajgir"}
# print(dict1)
# a=4
# b=5
# c=a+b
# print(c)
# # print("This is revision1 file")   and this is comment
# a="cgc"
# b=123
# c=a+str(b)  
# # c=a*b
# print(c)
# d=34.43
# e=34
# f=d+e
# print(f)
# set1={"2",3,4,2,32,}
# print(set1)
# input1=input("enter your name: ")
# print("hello "+input1)
# input2=input("enter your age ") 
# input3=input("enter your hometown")
# input4=input("enter your college name\n")
# input5=input("enter your branch name")



#union and update
# cities={"tokyo","newyourk","delhi","mumbai","chennai"}
# cities2={"gaya","rajgir","bihar","patna","delhi"}
# cites3=cities.union(cities2)
# print(cites3)
# cities.update(cities2)
# print(cities)
# cities.intersection_update(cities2)
# print(cities)


#insetrtion and insertion_update
# cites1={"india","china","japan","thiland"}
# cites2={"gaya","rajgir","bihar","patna","delhi","india"}
# cites3=cites1.intersection(cites2)
# print(cites3)

#disctionary

# ep1={12:283,13:9099,14:8823}
# # ep2={"19:233","91:234"}
# # ep1.update(ep2)
# # print(ep1)
# # ep1.clear()
# # print(ep1)
# ep1.pop(13)
# print(ep1)
# print(type(ep1))
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
# print(type(thisdict))



# for i in range (19):
#     print(i)
# else:
#     print("this is else block")


# try:
#     num=int(input("enter a number:"))
#     print(num)
# except:
#     print("ohh shit ")


#finally clause 
# try:
#     l= [2,3,4,5,6,7,4,4,3,3,3,2]
#     i=int(input("Enter a valid index"))
#     print(l[i])
# except:
#   print("some error bing executed ")
# finally:
#    print("i am always executed")  






def func():
    try:
        l=[2,3,4,5,63,242,3,32,4]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("something error")
        return 0
    finally:
        print("i am executed ")
x=func()  
print(x)      