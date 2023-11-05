from pandas import DataFrame, read_csv

from utils import showList
import traceback


# list

myList = [1, 2, 3, 3, 4, 5, 6, 6, 6]

print(myList)

print(myList[1])

showList(myList)

# set

mySet = {2, 99, 4, 5}

print(mySet)

showList(mySet)

mySet.add(6)
print(mySet)

mySet.add(6)
print(mySet)


mySet.remove(99)
print(mySet)


mySet = {2, 99, 4, 5}
mySet2 = {20, 99, 40, 5}

print("-"*10)
print(mySet.union(mySet2))
print(mySet.intersection(mySet2))
print(mySet.symmetric_difference(mySet2))
print("-"*10)
print(mySet.difference(mySet2))
print(mySet2.difference(mySet))



#Dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("-"*10)

print(thisdict["brand"])

showList(thisdict.values())

thisdict["New Key"] = "new value"
showList(thisdict.values())


thisdict.pop("New Key")
showList(thisdict.values())


thisdict.popitem()
showList(thisdict.values())

del thisdict["brand"]
showList(thisdict.values())


try:

    del thisdict["brawnd"]
    showList(thisdict.values())

    del thisdict
    showList(thisdict)

    thisdict.pop("new key")
    showList(thisdict.values())



except KeyError as erro1:

    print("erro na key")

except NameError:
    print(f"Erro no nome {NameError}")

print("it works")

# classes


