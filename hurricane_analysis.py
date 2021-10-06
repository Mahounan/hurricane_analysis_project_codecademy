#Overview

#This project is slightly different than others you have encountered thus far on
#Codecademy. Instead of a step-by-step tutorial, this project contains a series
#of open-ended requirements which describe the project you’ll be building.
#There are many possible ways to correctly fulfill all of these requirements,
#and you should expect to use the internet, Codecademy, and other resources when
#you encounter a problem that you cannot easily solve.

#Project Goals

#You will work to write several functions that organize and manipulate data about
#Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed.
#Each one of these functions will use a number of parameters, conditionals,
#lists, dictionaries, string manipulation, and return statements.

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


##1-In order to complete this project, you should have completed the Loops and Dictionaries sections of the Learn Python 3 Course. This content is also covered in the Data Scientist Career Path.

#2-
##Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity,
##the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist,
##you want to look at data about the most powerful hurricanes that have occurred.
##
##Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category
##5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. For some of the hurricanes, damage data was not
##recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (1000000000) and
##M stands for millions (1000000).
##
##Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data
##is retained as "Damages not recorded".
##
##Test your function with the data stored in damages.



#create an empty new damage list
new_damages=[]

#define my function that take a list as input
def update_damages1(data):
    new_damages1=[]
    for damage in data:
        if damage != "Damages not recorded":
            if "B" in damage:
                damage_new = float(damage.strip("B"))*1000
                new_damages1.append(damage_new)
            if "M" in damage:
                damage_new = float(damage.strip("M"))
                new_damages1.append(damage_new)
        else:
            new_damages1.append("Damages not recorded")
    return new_damages1

new_damages1=update_damages1(damages)
print(new_damages1)



#3-

##Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data includes:
##
##names: names of the hurricanes
##months: months in which the hurricanes occurred
##years: years in which the hurricanes occurred
##max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
##areas_affected: list of different areas affected by each of the hurricanes
##deaths: total number of deaths caused by each of the hurricanes
##The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane.
##
##For example, names[0] yields the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).
##
##Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries
##themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
##
##Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}.
##
##Test your function on the lists of data provided.

def construct_dict(names, months, years, max_sustained_winds, areas_affected, new_damages1, deaths):
    hurricane = {}
    for i in range(len(names)):
        hurricane.update({names[i]:{"Name":names[i],"Month":months[i],"Year":years[i], "Max Sustained Wind":max_sustained_winds[i], "Areas Affected":areas_affected[i], "Damage":new_damages1[i], "Deaths":deaths[i]}})
    #print(hurricane)
    return hurricane

hurricanes=construct_dict(names, months, years, max_sustained_winds, areas_affected, new_damages1, deaths)
#construct_dict(names=names, months=months, years=years, max_sustained_winds=max_sustained_winds, areas_affected=areas_affected, damages=damages, deaths=deaths)

print(hurricanes)



#4-
##In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
##
##Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists
##containing a dictionary for each hurricane that occurred in that year.
##
##For example, the key 1932 would yield the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'],
##'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected':
##                                                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}].
##
##Test your function on your hurricane dictionary.
year_hurricane = {}


def year_dict(hurricanes):
    for hurri in hurricanes.keys():
        current_year = hurricanes[hurri]["Year"]
        current_cane = hurricanes[hurri]        
        if hurricanes[hurri]["Year"] not in year_hurricane.keys():
            year_hurricane[hurricanes[hurri]["Year"]]=[current_cane]
            continue
        year_hurricane[current_year].append(current_cane)
    print(year_hurricane)
    
year_dict(hurricanes)



#5-
##You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is 
##important for making preparations for future hurricanes.
##
##Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return 
##the results in a dictionary where the keys are the affected areas and the values are counts of how many times 
##the areas were affected.
##

##a-Test your function on your hurricane dictionary.
def affected_area_count1(dictionary):
    count_of_areas1={}
    for hurri in dictionary.keys():
        for area in dictionary[hurri]["Areas Affected"]:
            if area not in count_of_areas1.keys():
                count_of_areas1[area] = dictionary[hurri]["Areas Affected"].count(area)
                continue
            count_of_areas1[area] += dictionary[hurri]["Areas Affected"].count(area)
    return count_of_areas1

count_of_areas1=affected_area_count1(hurricanes) 
print(count_of_areas1)


##b-Test your function on your Areas Affected list.
def affected_area_count(listofareas):
    count_of_areas={}
    for areas in listofareas:
        for area in areas:
            if area not in count_of_areas.keys():
                count_of_areas[area]= areas.count(area)
                continue #Once if is satisfied, the remainder of the code is ignored!Executed only when if not satisfied
            count_of_areas[area] += areas.count(area)
    return count_of_areas
    #print(count_of_areas)
    
    
count_of_areas=affected_area_count(areas_affected) 
print(count_of_areas)

#6-
##Write a function that finds the area affected by the most hurricanes, and how often it was hit.
##
##Test your function on your affected area dictionary.

def most_affected(count_of_areas):
    max_area = 'Central America'
    max_area_count = 0    
    for area in count_of_areas.keys():
        if count_of_areas[area] > max_area_count:
            max_area_count = count_of_areas[area]
            max_area = area
    print("The most affected area is " + max_area + ". It was hit " + str(max_area_count) + " times.")

most_affected(count_of_areas)


#7-
##Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
##
##Test your function on your hurricane dictionary.

def most_deaths(hurricanes):
    max_death = 'Central America'
    max_death_count = 0    
    for hurri in hurricanes.keys():
        if hurricanes[hurri]["Deaths"] > max_death_count:
            max_death_count = hurricanes[hurri]["Deaths"]
            max_death = hurri
    print("The most deadly hurricane is " + max_death + ". It killed " + str(max_death_count) + " people.")

most_deaths(hurricanes)


#8-
##Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.
##
##Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key
##is the rating and the value is the upper bound of deaths for that rating.
##For example, a hurricane with a 1 mortality rating would have resulted in greater than 0 but less than or equal
##to 100 deaths. A hurricane with a 5 mortality rating would have resulted in greater than 10000 deaths.
##
##Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists
##containing a dictionary for each hurricane that falls into that mortality rating.
##
##Test your function on your hurricane dictionary.

def death_rating(hurricanes):
    hurricanes_rating={}
    hurricanes_rating[0]=[]
    hurricanes_rating[1]=[]
    hurricanes_rating[2]=[]
    hurricanes_rating[3]=[]
    hurricanes_rating[4]=[]
    hurricanes_rating[5]=[]
    for hurri in hurricanes.keys():
        if hurricanes[hurri]["Deaths"] == 0:
            hurricanes_rating[0].append(hurricanes[hurri])
        elif hurricanes[hurri]["Deaths"] > 0 and hurricanes[hurri]["Deaths"] <= 100:
            hurricanes_rating[1].append(hurricanes[hurri])
        elif hurricanes[hurri]["Deaths"] > 100 and hurricanes[hurri]["Deaths"] <= 500:
            hurricanes_rating[2].append(hurricanes[hurri])
        elif hurricanes[hurri]["Deaths"] > 500 and hurricanes[hurri]["Deaths"] <= 1000:
            hurricanes_rating[3].append(hurricanes[hurri])
        elif hurricanes[hurri]["Deaths"] > 1000 and hurricanes[hurri]["Deaths"] <= 10000:
            hurricanes_rating[4].append(hurricanes[hurri])
        elif hurricanes[hurri]["Deaths"] > 10000:
            hurricanes_rating[5].append(hurricanes[hurri])
    return hurricanes_rating

hurricanes_rating=death_rating(hurricanes)
print(hurricanes_rating)


#9-
##Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
##
##Test your function on your hurricane dictionary.

def most_damage(hurricanes):
    max_damage = 'Central America'
    max_damage_count = 0    
    for hurri in hurricanes.keys():
        if hurricanes[hurri]["Damage"] != "Damages not recorded":
            if hurricanes[hurri]["Damage"] > max_damage_count:
                max_damage_count = hurricanes[hurri]["Damage"]
                max_damage = hurri
    print("The hurricane with the most damage is " + max_damage + ". It cost " + str(max_damage_count) + " millions dollars.")

most_damage(hurricanes)




#10-
##Lastly, you want to rate hurricanes according to how much damage they cause.
##
##Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
##
##damage_scale = {0: 0,
##                1: 100000000,
##                2: 1000000000,
##                3: 10000000000,
##                4: 50000000000}
##For example, a hurricane with a 1 damage rating would have resulted in damages greater than 0 USD but less than or equal to 100000000 USD. A hurricane with a 5 damage rating would
##have resulted in damages greater than 50000000000 USD (talk about a lot of money).
##
##Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
##
##Test your function on your hurricane dictionary.
def damage_rating(hurricanes):
    hurricanes_rating_damage={}
    hurricanes_rating_damage["Damages not recorded"]=[]
    hurricanes_rating_damage[0]=[]
    hurricanes_rating_damage[1]=[]
    hurricanes_rating_damage[2]=[]
    hurricanes_rating_damage[3]=[]
    hurricanes_rating_damage[4]=[]
    hurricanes_rating_damage[5]=[]
    for hurri in hurricanes.keys():
        if hurricanes[hurri]["Damage"] != "Damages not recorded":
            if hurricanes[hurri]["Damage"] == 0:
                hurricanes_rating_damage[0].append(hurricanes[hurri])
            elif hurricanes[hurri]["Damage"] > float(0) and hurricanes[hurri]["Damage"] <= float(100):
                hurricanes_rating_damage[1].append(hurricanes[hurri])
            elif hurricanes[hurri]["Damage"] > float(100) and hurricanes[hurri]["Damage"] <= float(1000):
                hurricanes_rating_damage[2].append(hurricanes[hurri])
            elif hurricanes[hurri]["Damage"] > float(1000) and hurricanes[hurri]["Damage"] <= float(10000):
                hurricanes_rating_damage[3].append(hurricanes[hurri])
            elif hurricanes[hurri]["Damage"] > float(10000) and hurricanes[hurri]["Damage"] <= float(50000):
                hurricanes_rating_damage[4].append(hurricanes[hurri])
            elif hurricanes[hurri]["Damage"] > float(50000):
                hurricanes_rating_damage[5].append(hurricanes[hurri])
        if hurricanes[hurri]["Damage"] == "Damages not recorded":
            hurricanes_rating_damage["Damages not recorded"].append(hurricanes[hurri])
    return hurricanes_rating_damage

hurricanes_rating_damage=damage_rating(hurricanes)
print(hurricanes_rating_damage)      





# write your construct hurricane dictionary function here:







# write your construct hurricane by year dictionary function here:







# write your count affected areas function here:







# write your find most affected area function here:







# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:

