my_list = []

# my_list.extend([10,20,30,40])

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50,60,70])

# my_list.remove(70)
my_list.pop(7)

my_list.sort()

print(my_list)

index_of_30 = my_list.index(30)
print(index_of_30)