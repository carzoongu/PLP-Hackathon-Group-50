def main():
    
    #Ask for the number of fat in grams
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    fat_calories(fat_grams)
    
    #Ask for the number of Carbohydrates in grams
    carb_grams = float(input("Enter the number of carbohydrates grams consumed: "))
    carb_calories(carb_grams)
    
def fat_calories(fat_grams):
    #Calculate the calories from fat
    calories_from_fat = fat_grams * 9
    print("The Calories from fat are " ,calories_from_fat, "Calories")
    
def carb_calories(carb_grams):
    #Calculate The calories from Carbohydrates
    calories_from_carbs = carb_grams * 4
    print("The Calories from carbohydrates are ", calories_from_carbs, "calories")
    
#Call the main function

main()
