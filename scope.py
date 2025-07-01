# username = "Parth"

# def func():
#     username = "Rakholiya"
#     print(username)

# print(username)
# func()

# x = 99

# def func(y):
#     z = x+y
#     return z

# result = func(1)
# print(result)

def func1(num):
    def func2(i):
        return num*i

    print(func2(5))
print(func1(2))        


