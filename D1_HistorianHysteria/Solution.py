# Create 2 lists
list1 = []
list2 = [] 
distanceList = []


# Open input and Read Input
# Store Column 1 in List1
# Store Column 2 in List2
with open('input.txt','r') as file:
    print(input)
    for line in file:
        words = line.split()
        list1.append(int(words[0]))
        list2.append(int(words[1]))

# Close File
file.close()

# Order List1 and List2
list1.sort()
list2.sort()

# List1.item = abs(List1.item -List2.item)
for index, LocationIDs in enumerate(list1):
    distanceList.append(abs(list1[index] - list2[index]))

# distance = sum of items in List1
distance = 0
for LocationID in distanceList:
    distance += LocationID

print(distance)

 #########################################################################
 #Part2

similarityScoreList = []

for item1 in list1:
    
    repetetion = 0
    for item2 in list2:
        if item1 == item2:
            repetetion += 1
    similarityScoreList.append(item1*repetetion)

print(similarityScoreList)

similarityScore = 0
for item in similarityScoreList:
    similarityScore += item

print(similarityScore)
    