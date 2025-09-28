weather = input("What's the weather like today? (sunny/rainy/cold): ")
weather = weather.lower()
if weather == "sunny":
    print("Wear a t-shirt and a sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a rain coat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this kind of weather.")