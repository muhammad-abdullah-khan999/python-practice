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




a = 1000
b = 1000
print(a == b)  # True (Same value)
print(a is b)  # False (Different memory locations)
print(id(a), id(b))  # Different IDs (not cached)
