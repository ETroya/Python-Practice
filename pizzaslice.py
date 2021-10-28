# Your code below:
toppings= ["peppronni","pineapple","cheese", "sausage", "olives", "anchovies","mushrooms"]

prices = ["2","6","1","3", "2", "7", "2"]

num_two_dollar_slices =prices.count("2")

num_pizzas=len(toppings)

pizza_and_prices = list(zip(prices, toppings))
pizza_and_prices.sort()
cheapest_pizzas= pizza_and_prices[1]
priciest_pizza = pizza_and_prices[-1]
three_cheapest = pizza_and_prices[:3]
pizza_and_prices.pop()
print("We sell "+ str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices.insert(3, [2.5, "peppers"])
print(pizza_and_prices)
print(three_cheapest)