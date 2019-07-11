import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

print(data[1])
print(data[2])
