#print("Hello World")


counties = ("Arapahoe", "Denver", "Jefferson")

if counties[1] == 'Denver':
    print(counties[1])

counties_dict = {'Arapahoe':422829,
     'Denver':463353,
    'Jefferson':432438}



counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


for i in range(len(counties)):
    print(counties[i])

voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters": 422829})
 
voting_data.append({"county":"Denver","registered_voters": 463353})
voting_data.append({"county":"Jefferson","registered_voters": 432438})

for i in range(len(voting_data)):

      print(voting_data[i])

#skill drill 3.2.11

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county, value in counties_dict.items():
    #print(f"{county} has {value} registered voters.")
    
#skill drill 3.2.11

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for value in voting_data:
    print(f"{value['county']} has {value['registered_voters']} registered voters.")


