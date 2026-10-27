# store many items
# ages = [21, 72, 43, 76, 23, 78,88, 90, 15]
#
# names = ["Jane", "Jack", "Moha","Rick"]
#
# # functions
# ages.append(31)
# # ages.clear()
# ages.sort()
# ages.reverse()
# print(ages)
#
# names.sort(reverse=True)
# print(names)
#
# print(len(names))
# print(len(ages))
#
# print(sum(ages)/len(ages))
#
# # retrieve an element
# print(ages[0])
# print(ages[-1])
# print(ages[-2])
# print(ages[:2])
# print(ages[-3:])
# print(ages[::-1])
# print(ages[3:4])

#set
scores = {88, 78, 88, 65, 77 }
print(scores)
scores.add(90)
scores.remove(65)
print(scores)

# tuple immutable
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays[0])

# dictionary
person = {"name": "Jason", "age": 22, "weight":53, "height":1.88}

print(person["name"])
print(person["age"])

people = [
          {"name":"Aria","age": 29},
          {"name":"Morris","age":20},
          {"name":"Hellen","age":23}
           ]
print(people[0]["age"])

