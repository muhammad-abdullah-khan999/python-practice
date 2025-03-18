#memoryview
#memview:memoryview = memoryview(b"Operation Badar")
#print(type(memview), "memory view : ", memview)
#print(bytes(memview[0:5]))
#print(memview[4:12])



#id() in Python
# x = [1,2,3]
# y = x

# print((id(x)))
# print(id(y))

# y.append(4)
# print(x)
# print(y)




# a = 1000
# b = 1000
# print(a == b)  # True (Same value)
# print(a is b)  # False (Different memory locations)
# print(id(a), id(b))  # Different IDs (not cached)




# string_methods : str = dir(str)
# filtered_methods : str = [method for method in string_methods if not method.startswith("__")]
# print(filtered_methods)




# word = "Python"
# for letter in word:
#     print(letter)




# numbers = [1,2,3,4,6]
# for num in numbers:
#     if num == 2:
#         print("Breaking the loop!")
#         break
# else:
#     print("Loop successfully completed")




# for i in range(2,12,2):
#     print(i)




# for _ in range(10):
#     print(f"number counting : { _ }" )




# number: int = 1
# while number < 8:
#     print(f" number is : {number}")
#     number += 1




# for outerLoop in range(1,6):
#     print(f"Multiplication Table for {outerLoop}")
#     for innnerLoop in range(1,4):
#         print(f"{innnerLoop} X {outerLoop} = {innnerLoop * outerLoop}")
#     print()




# total = 0
# for i in range(1 , 101):
#     total += i
# print(f"The sum of all numbers from 1 to 100 is : {total}")




# num = 24
# factors = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         factors.append(i)
# print(f"Factors of {num}: {factors}")




# words = ['apple', 'banana', 'kiwi']
# words.sort(key= lambda word: len(word))
# print(words)