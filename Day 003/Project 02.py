city=["CSS","Chowk Azam","Lahore"]


city.append("Riazabad")
city.append("Karachi")


print(city)


city.extend(["Multan","Murree"])


print(city)

print(city[0])

for item in ["CSS","Multan"]:
    if item in city:
        city.remove(item)


print(city)
