def decor(input_func):
    def result(*args):
        print("\n>>> Called decorated func <<<", end="\n")
        out = input_func(*args)
        print("\n\t^^^")
        return not out
    return result

input("Func will be called...")

@decor # Using the decorator (he get func inself)
def result_func(txt = "some txt"):
    print(str(txt))
    return True

print("Her result is: " + str(result_func("\tsome func")))

class Commodity:
    def sell_with_price(self, price):
        print(f"Commodity selled with price: {price}")

class Human:
    default_name = "Default huma" # атрибут класса (обращаться через имя класса)
    @staticmethod
    def say_bae():
        print("Bye babe!")

    def __init__(self, name):
        if name:
            self.__name = name # атрибут объекта (обращаться через экземпляр класса)
        else: self.__name = Human.default_name

    #>>> Getter property
    @property
    def Name(self):
        return "Negger name: " + self.__name

    def say_hello(self):
        print(f"Hello! Im heman end my name is {self.__name}")

class Negr (Human, Commodity):
    def __init__(self, name, price, age):
        self.price = price
        self.__age = age
        super().__init__(name)
    def say_hello(self):
        super().say_hello()
        print("Im a negra")

#>>> Property
    @property
    def Age(self):
        return self.__age
    
    @Age.setter
    def Age(self, value):
        try:
            if int(value) > 0 and int(value) < 110:
                self.__age = value
            else: print("Not correct age")
        except: print("Not num age")
        finally: print("Age setted")
#End of property <<<
    def __del__(self):
        self.sell_with_price(self.price)

    def get_all_data(self):
        return self.price, self.__age, self.Name 

bobba = Negr("Bobba", 102, 35)
zeli = Negr("Zelli", 18, 12)

print(f"Negrils {bobba.Name} and {zeli.Name} adds to cart. Total price = {bobba.price + zeli.price}")

bobba.Age = input("Set bobbas age: ")
print(f"{bobba.Name} age is {bobba.Age}")

bobba.say_hello()

if isinstance(zeli, Commodity):
    zeli.sell_with_price(zeli.price)
    Human.say_bae()

print(zeli.get_all_data())

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
