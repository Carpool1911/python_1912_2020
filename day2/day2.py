print("-------------Question 1------------------")
text1 = "hello, and welcome to my world"
text2 = "by to the world"
print(text1)
text = text1 + text2

#find position of word
print(text.find("welcome"))

#Convert first character of word into uppercase
print(text.title())

#count repeted word
print(text.count("to"))

#Split a string into a list, using comma, followed by a space (, ) as the separator:
print(text.rsplit())

#Convert string in to all uppercase
print(text.upper())

print("-------------Question 2------------------")

lst2 = [2,6,7,3,100,45,34,79,43,78,215, 'abc', 34, True, 40, "male"]
#sort list
print(sorted(lst2))

#find index of given value
print(lst2.index("male"))

#remove specific value
lst2.remove(34)
print(lst2)

#remove second element
lst2.pop(2)
print(lst2)

#remove all element from list
lst2.append("helloe")
print(lst2)


print("----------------Question 3-----------------")
Dit = {"key1":"3", "key2": "yes", "key3": "no", "key4": "true"}
#Access value of key2
print(Dit["key2"])

#Change value of key 3
Dit.update({"key3": "false"})
print(Dit)

#remove the item with speicified keyname
Dit.pop("key4")
print(Dit)

#Add item
Dit["color"] = "red"
print(Dit)

#list key contains
print(Dit.keys())
