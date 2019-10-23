# how to make a list
favMovies = ["Dora the Explorer", "The Emoji Movie", "High School Musical"]
# print the whole list
print(favMovies)
# print individuals 
print(favMovies[2])
# to add you can append or insert 
# append adds to the end
favMovies.append("High School Musical 2")
print(favMovies)
# insert will put them wheverever you want
favMovies.insert(1, "High School Musical 3")
print(favMovies)
# how to remove items
# remove by name or index
# remove by name use "remove"
favMovies.remove("Dora the Explorer")
print(favMovies)
# pop will remove the last item unless you add an index
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remove the index
print(favMovies)

# get the length of a list
# this is a function
# the function na,e is len
print("My List has" + str(len(favMovies))+ "items")
favMovie = input("What is your favorite movie? :) ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies) - 1])

# loop through a list
count = 1

for movie in favMovies:
	print("My number "+ str(count)+"movies is"+ movie)
	count = count + 1

numList=[1,2,43,665,3465,545643]
#challenge: loop through the list and add all the numbers together, print the answer

total = 0
for number in numList:
	total = total + number


