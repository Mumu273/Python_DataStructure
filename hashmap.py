print("Hashmap\n")

city_map = {}
# city_map['usa'] = ['New York']
user_input_for_city_map = input("Enter country name and the city name of the country you want to store. Separate the cities from country name using colon. "
                                "After finishing a list of cities of a country use a semicolon to separate from other country city list.\n").lower()


city_map_keys = user_input_for_city_map.split(";")
separate_key_value = [key.strip() for key in city_map_keys]


for key in separate_key_value:
    city_map[key.split(":")[0].strip()] = key.split(":")[1].strip()

print(city_map)

options = {
    1: "Find City",
    2: "Find Country"
}

print("Chose from the options bellow.\n")
print(options)

chosen_option = int(input("If you want to find the city using country name choose option 1, otherwise choose option 2\n"))

if options.get(chosen_option):

    if chosen_option == 1:
        country_names = input("Enter country names(Separate country names using comma if you want to find the cities of multiple country):\n").lower()
        country_names = country_names.split(",")
        country_names = [name.strip() for name in country_names]
        for country in country_names:
            print(country + ":" + city_map.get(country))

    if chosen_option == 2:
        city_names = input("Enter city names(Separate city names using comma if you want to find the countries of multiple cities):\n").lower()
        city_names = city_names.split(",")
        city_names = [name.strip() for name in city_names]
        print(city_names)
        values_from_city_map = list(city_map.values())

        print(values_from_city_map)
        if city_names in values_from_city_map:
            print([key for key, val in city_map.items() if val==city_names])
            print("I want to see here")
            # print(country + ":" + city_map.get(country))
            print(city_names)
else:
    print("Please choose a valid option.\n")



# usa: new york, los angels; canada: toronto