import requests
query = input("search here: ")
try:
    url = f"https://api.freeapi.app/api/v1/public/meals?page=1&limit=10&query={query}"
    data = requests.get(url)
    print(data)
    response= data.json()
except :
    print("something went wrong")
def main():
    if response["success"] and response["data"] != []:
        apidata = (response["data"])
        apidata2 = apidata["data"]
        meal_dta = apidata2[0]
        meal_name = meal_dta["strMeal"]
        strCategory = meal_dta["strCategory"]
        strInstructions = meal_dta["strInstructions"]
        strIngredient1 = meal_dta["strIngredient1"]
        strIngredient2 = meal_dta["strIngredient2"]
        strIngredient3 = meal_dta["strIngredient3"]
        strIngredient4 = meal_dta["strIngredient4"]
        strIngredient5 = meal_dta["strIngredient5"]
        strIngredient6 = meal_dta["strIngredient6"]
        strIngredient7 = meal_dta["strIngredient7"]
        strIngredient8 = meal_dta["strIngredient8"]
        strIngredient9 = meal_dta["strIngredient9"]
        strIngredient10 = meal_dta["strIngredient10"]
        strIngredient11 = meal_dta["strIngredient11"]
        strIngredient12 = meal_dta["strIngredient12"]
        strIngredient13 = meal_dta["strIngredient13"]
        strIngredient14 = meal_dta["strIngredient14"]
        strIngredient15 = meal_dta["strIngredient15"]
        strIngredient16 = meal_dta["strIngredient16"]
        strIngredient17 = meal_dta["strIngredient17"]
        strIngredient18 = meal_dta["strIngredient18"]
        strIngredient19 = meal_dta["strIngredient19"]
        strIngredient20 = meal_dta["strIngredient20"]
        strMeasure1 = meal_dta["strMeasure1"]
        strMeasure2 = meal_dta["strMeasure2"]
        strMeasure3 = meal_dta["strMeasure3"]
        strMeasure4 = meal_dta["strMeasure4"]
        strMeasure5 = meal_dta["strMeasure5"]
        strMeasure6 = meal_dta["strMeasure6"]
        strMeasure7 = meal_dta["strMeasure7"]
        strMeasure8 = meal_dta["strMeasure8"]
        strMeasure9 = meal_dta["strMeasure9"]
        strMeasure10 = meal_dta["strMeasure10"]
        strMeasure11 = meal_dta["strMeasure11"]
        strMeasure12 = meal_dta["strMeasure12"]
        strMeasure13 = meal_dta["strMeasure13"]
        strMeasure14 = meal_dta["strMeasure14"]
        strMeasure15 = meal_dta["strMeasure15"]
        strMeasure16 = meal_dta["strMeasure16"]
        strMeasure17 = meal_dta["strMeasure17"]
        strMeasure18 = meal_dta["strMeasure18"]
        strMeasure19 = meal_dta["strMeasure19"]
        strMeasure20 = meal_dta["strMeasure20"]
        
        print(f"meal name is {meal_name}and the ingreadiants are {strIngredient1} is {strMeasure1} , \n {strIngredient2} is {strMeasure2},  \n{strIngredient3} is {strMeasure3},\n{strIngredient4} is {strMeasure4},\n{strIngredient5} is {strMeasure5},\n{strIngredient5} is {strMeasure5},\n {strIngredient6} is {strMeasure6},\n {strIngredient7} is {strMeasure7},\n {strIngredient8} is {strMeasure8},\n{strIngredient9} is {strMeasure9}, \n{strIngredient10} is {strMeasure10},\n{strIngredient11} is {strMeasure11},\n {strIngredient12} is {strMeasure12},\n {strIngredient13} is {strMeasure13},\n{strIngredient14} is {strMeasure14},\n {strIngredient15} is {strMeasure15},\n {strIngredient16} is {strMeasure16},\n {strIngredient17} is {strMeasure17}, \n{strIngredient18} is {strMeasure18},\n {strIngredient19} is {strMeasure19},\n {strIngredient20} is {strMeasure20}\n  ")
        print(f"the category is {strCategory} and the instructions are {strInstructions}")
    else:
        print("somwthing went wrong from api")


if __name__ == "__main__":
    main()

