# def decor(input_func):
#     def result(*args):
#         print("\n>>> Called decorated func <<<", end="\n")
#         out = input_func(*args)
#         print("\n\t^^^")
#         return not out
#     return result

# input("Func will be called...")

# @decor # Using the decorator (he get func inself)
# def result_func(txt = "some txt"):
#     print(str(txt))
#     return True

# print("Her result is: " + str(result_func("\tsome func")))

# class Commodity:
#     def __init__(self, price):
#         self.price = price

#     def display_price(self):
#         print(f"Price is: {self.price}")

# class Negr:
#     def __init__(self, name, price, age):
#         self.__name = name
#         super().__init__(price)
#         self.__age = age

# #>>> Property
#     @property
#     def Age(self):
#         return self.__age
    
#     @Age.setter
#     def Age(self, value):
#         try:
#             if int(value) > 0 and int(value) < 110:
#                 self.__age = value
#             else: print("Not correct age")
#         except: print("Not num age")
#         finally: print("Age setted")
# #End of property <<<

# #>>> Getter property
#     @property
#     def Name(self):
#         return "Negger name: " + self.__name


#     def __del__(self):
#         print(f"Slave {self.__name} selled.")

# bobba = Negr("Bobba", 102, 35)
# zeli = Negr("Zelli", 18, 12)

# print(f"Negrils {bobba.Name} and {zeli.Name} adds to cart. Total price = {bobba.price + zeli.price}")

# bobba.Age = input("Set bobbas age: ")
# print(f"{bobba.Name} age is {bobba.Age}")



# # prTxt = input("Nigga: ") # bt not a niga
# # print(prTxt)

# # if (int(prTxt) < 0): # 
# #     print("Stupid?")
# # else:
# #     f = print("ok")
# #     print("Res = " + str(f), end=" ")
# #     input("go next?")

# # def print_range(minR, maxR, /, ftName, *, lName = "NoN"):
# #     for z in range(minR, maxR):
# #         print(f"{z} repeat {ftName} and {lName}")
# #     return minR / maxR

# # res = print_range(int(input("min: ")), int(input("Max: ")), "negr", lName="Haver")
# # print("Ok, next is result: " + str(res))

# # funcMsg = lambda m = "Null", /: print(m)
# # funcMsg(input(f"call next func? ({type(funcMsg)})"))

# # def outer(n):
# #     def inter(m):
# #         nonlocal n
# #         n+=m
# #         print("m + n = " + str(n))

# #     return inter

# # closer = outer(5) # closer is closure of outer cos contain iter func cos outer returns inter

# # closer(1)
# # closer(2)
# # closer(3)
