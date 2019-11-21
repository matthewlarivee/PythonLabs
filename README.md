#	PythonLabs

#	PrintOutput
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

PrintOutput was made by simply printing "OUTPUT" followed by the input string

#	LoadFile
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

LoadFile opens a text file and uses the split function with the parameter of 
a new line to create a list

#	UpdateString
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

Update string takes the input string and appends each character to an empty list.
This way it is possible to change the character using the index and is then just
joined together using the join function with nothing between the characters.

#	FindWordCount
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

FindWordCount searches goes through each object in the list and uses the count
function to see how many times the word or substring appear. It then adds all the
times it has appeared in each object and returns that sum

#	ScoreFinder
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

ScoreFinder compares existence of the player first by making sure the player in 
the list and the query are both lowercase. If the player exists, it uses the
index function to print out both the query and the score at the right index.

#	Union
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

Union works by making an empty list, then checking if each element in the first
list is in the empty list. If it isn't in the list, then it will append it,
otherwise it will do nothing in the case of the duplicate. It does this with both
lists and returns the list that everything was appended to

#	Intersection
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

Intersection works like union by appending non duplicates to an empty list,
however when it does find a duplicate that is already in the first list, it will
add that object to another empty list which holds all the duplicates. The function
then returns the duplicate list

#	NotIn
#	Matthew Larivee
#	​CSCI 102 – Section A
#	Week 12 - Part A

NotIn creates an empty list and checks if each object in the first list is not in
the second list using the key words not and in. Very simple. If they aren't in the
second list, they add it to the empty list and return that when it is done