import requests

def recipe_search(ingredient, dietary_requirement_num):
    app_id = '5824a27e'
    app_key = '2d03552e6ce6231fab99aa6382a4e6a9'
    result = requests.get(f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}')
    dietary_require = ['vegan', 'vegetarian', 'dairy-free', 'gluten-free', 'peanut-free']
    for num in dietary_requirement_num:
        if num in ['1', '2', '3', '4', '5']:
            url = f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&health={dietary_require[int(num)-1]}"
            result = requests.get(url)
            dietary_data = result.json()
            return dietary_data["hits"]
        data = result.json()
        return data['hits']

def recipe_calories(ingredient, dietary_requirement_num, another):
    app_id = '5824a27e'
    app_key = '2d03552e6ce6231fab99aa6382a4e6a9'
    result = requests.get(f'https://api.edamam.com/search?q={ingredient} + {another}&app_id={app_id}&app_key={app_key}')
    dietary_require = ['vegan', 'vegetarian', 'dairy-free', 'gluten-free', 'peanut-free']
    for num in dietary_requirement_num:
        if num in ['1', '2', '3', '4', '5']:
            url = f"https://api.edamam.com/search?q={ingredient} + {another}&app_id={app_id}&app_key={app_key}&health={dietary_require[int(num)-1]}"
            result = requests.get(url)
            dietary_data = result.json()
            return dietary_data["hits"]
    result = result
    data = result.json()
    return data['hits']

def run(ingredient, dietary_requirement_num):
    results = recipe_search(ingredient, dietary_requirement_num)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print(recipe['calories'])
        print()
        file.write(recipe['label'] + '\n' + recipe['url'] + '\n\n')

def calories_run(ingredient, dietary_requirement_num):
    dietary_requirement_num = dietary_requirement_num
    results = recipe_search(ingredient, dietary_requirement_num)
    for result in results:
        recipe = result['recipe']
        if recipe['calories'] < max_calories:
            print(recipe['label'])
            print(recipe['url'])
            print(recipe['calories'])
            print()
            file.write(recipe['label'] + '\n' + recipe['url'] + '\n\n')

def further_calories_run(ingredient, dietary_requirement_num, another):
    dietary_requirement_num = dietary_requirement_num
    results = recipe_calories(ingredient,dietary_requirement_num, another)
    for result in results:
        recipe = result['recipe']
        if recipe['calories'] < max_calories:
            print(recipe['label'])
            print(recipe['url'])
            print(recipe['calories'])
            print()
            file.write(recipe['label'] + '\n' + recipe['url'] + '\n\n')

def run_search(ingredient, dietary_requirement_num, another):
    global recipe
    results = recipe_calories(ingredient, dietary_requirement_num, another)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print(recipe['calories'])
        print()
        file.write(recipe['label'] + '\n' + recipe['url'] + '\n\n')

dietary_requirement_num = input("Do you have any of these dietary requirements? No = 0 Vegan = 1, vegetarian = 2, lactose = 3, gluten = 4, peanut allergy = 5: ")
file = open('output.txt', 'w')

calories = input("Would you like to filter by calories (y/n): ")
if calories == "y":
    ingredient = input('Enter an ingredient: ')
    max_calories = float(input("Enter max calories: "))
    calories_run(ingredient, dietary_requirement_num)
else:
    max_calories = 0
    ingredient = input('Enter an ingredient: ')
    run(ingredient, dietary_requirement_num)

search_again = input("Do you want to narrow it down further? y/n ")
if search_again == "y":
    dietary_requirement_num = dietary_requirement_num
    another = input("What additional ingredient would you like to search for? ")
    if calories:
        further_calories_run(ingredient, dietary_requirement_num, another)
    run_search(ingredient, dietary_requirement_num, another)
else:
    print()
    print("Okay, see your searches above")

file.close()