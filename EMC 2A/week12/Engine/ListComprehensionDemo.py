# with open("granny.obj") as fp:
#     line = fp.readline()
#     print(line)

line = 'v -1.240270 116.339233 17.187325'
line = line[1:]
#list comprehension
# [variable for variable in collection]
newList = []
newList = [float(value) for value in line.split()]
print(newList)

#list slicing
name = 'ruffa resentes'
nickname = name[6:9]     #name[index 0 to 2]
print(nickname)










