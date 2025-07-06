spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = [foods["name"] for foods in spicy_foods]
    return new_list

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"]>5]
    return spiciest_foods

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

print_spicy_foods(spicy_foods)



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods["cuisine"] == cuisine:
            return foods

get_spicy_food_by_cuisine(spicy_foods,"American")


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"]>5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")



def get_average_heat_level(spicy_foods):
    total = 0
    for foods in spicy_foods:
        total+= foods["heat_level"]
    average = total/len(spicy_foods)
    return average

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods,{
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }))
