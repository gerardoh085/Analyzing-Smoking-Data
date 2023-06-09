'''
Author: Gerardo Hernandez Macoto
Project: Analyzing Smoking Data
'''

'''

Structure = 
{
    'Country': string, 
    'Year': integer, 
    'Data': 
        {
            'Daily cigarettes': float, 
            'Percentage': 
                {
                    'Male': float, 
                    'Female': float, 
                    'Total': float
                }, 
            'Smokers': 
                {
                    'Total': integer, 
                    'Female': integer, 
                    'Male': integer
                }
        }
}


LIMITATIONS:
    There year cut off
    There is not an accurate answer as the cut off seems to be 
    about 2012
'''


import matplotlib.pyplot as plt
import smoking
data = smoking.get_report()


# question 1:
# What is the daily average number
# of cigarettes smoked in every
# country (from 1980 - 2012)?

getDictionary = {}
getInfo = []
getCountryName = set()

for info in data:
    item = info["Country"]
    if item not in getCountryName:
        getCountryName.add(item)
        getDictionary = {"Country": item,
                         "Daily": 0, "Average": 0, "Counter": 0}
        getInfo.append(getDictionary)

for i in range(len(data)):
    for j in range(len(getInfo)):
        if data[i]["Country"] == getInfo[j]["Country"]:
            Daily = data[i]["Data"]["Daily cigarettes"]
            getInfo[j]["Daily"] += Daily
            getInfo[j]["Counter"] += 1
            getInfo[j]["Average"] = getInfo[j]["Daily"] / getInfo[j]["Counter"]


allCountries = [(i["Country"]) for i in getInfo]
avgDaily = [(i["Average"]) for i in getInfo]


plt.figure(figsize=(20, 6))
plt.bar(allCountries, avgDaily)
plt.xlabel("Country")
plt.ylabel("Average Daily Cigarettes")
plt.title("Average Daily Cigarettes per Country")
plt.xticks(allCountries, [str(i) for i in allCountries], rotation=90)
plt.tick_params(axis='x', which='major', labelsize=8)
plt.tight_layout()


# Question 2:
# what percentage of male and female smoke
# and how many for each?

tMaleList = []
tFemaleList = []

for info in data:
    tM = info["Data"]["Smokers"]["Male"]
    tF = info["Data"]["Smokers"]["Female"]

    tMaleList.append(tM)
    tFemaleList.append(tF)


# print(f"Result:\nMale: {tMaleList}, Female: {tFemaleList}")

total = sum(tMaleList) + sum(tFemaleList)
# print(sum(pMaleList))

pieChart = [round((sum(tMaleList)/total)*100, 2),
            round((sum(tFemaleList)/total)*100, 2)]

label = ["Male", "Female"]
plt.figure()
plt.pie(pieChart, labels=label, autopct='%.2f%%')


# Question 3:
# What is the total number
# of smokers per decade?

newDict = {}
newList = []
newSet = set()

for item in data:
    decade = (item["Year"]//10) * 10
    if decade not in newSet:
        newSet.add(decade)
        newDict = {"Decade": decade, "Total Smokers": 0}
        newList.append(newDict)


for i in range(len(data)):
    decade = (data[i]["Year"]//10) * 10
    for j in range(len(newList)):
        if decade == newList[j]["Decade"]:
            totalSmoker = data[i]["Data"]["Smokers"]["Total"]
            newList[j]["Total Smokers"] += totalSmoker


decadeList = [(newList[i]["Decade"]) for i in range(len(newList))]
totalSmokers = [(newList[i]["Total Smokers"]) for i in range(len(newList))]


plt.figure()
plt.bar(decadeList, totalSmokers, width=5)
plt.xlabel("Decade")
plt.xticks(decadeList)
plt.ylabel("Total Smokers (in billions)")
plt.title("Total Smokers per Decade")


plt.show()
