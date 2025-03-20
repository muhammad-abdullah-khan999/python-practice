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




#Word Frequency Counter

# sentence = "apple banana apple orange banana apple"
# words:list = sentence.split()
# wordCount = {}

# for word in words:
#     if word in wordCount:
#         wordCount[word] +=1
#     else:
#         wordCount[word] = 1

# print(wordCount)




#Short code for Word Frequency Counter

# from collections import Counter
# sentence = "apple banana apple orange banana apple"
# word_count = Counter(sentence.split())
# print(word_count)



#Basic syntax for dictionary comprehension
#{key_expression: value_expression foritem in iterable if condition } # condition is optional

# original_dict = {"a":0 ,"b": 2, "c": 3 }
# print("original_dict = " , original_dict)
# doubled_dict = {k : v*2 for k,v in original_dict.items() if v > 0}
# print("doubled_dict = ", doubled_dict)




#Temperature Converter from Celsius to Fahrenhiet

celsuis = {0,10,20,30,40}
fahrenhiet_temp = {str(c) + f"{chr(176)}C" : str((c * 9/5) + 32) + f"{chr(176)}F" for c in celsuis}
print(fahrenhiet_temp)

