import matplotlib.pyplot as plt

#collect the data
print("Enter Pokeman Data:")
print("Day 1: ", end= "")
day1 = int(input())
print("Day 2: ", end= "")
day2 = int(input())
print("Day 3: ", end= "")
day3 = int(input())


#put the data in a list
data = [day1, day2, day3]

# New version - Loop and get each day at a time
data = [] #empty list
num_days = int(input("How many days? "))
for day in range(num_days):
  print("Day ", day, ":", end="")
  today = int(input())
  data.append(today) # add it to the end of the list

# put the data in a list (DONE)
# print min and max
print("Best day:", max(data))
print("Worst day:", min(data))

# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()
