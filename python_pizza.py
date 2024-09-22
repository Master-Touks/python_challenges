pizza_size = {
    "s": 15,
    "m": 20,
    "l": 25
}

pepperoni_add_ons = {
    "y": 2,
    "pepperoni_big": 3,
    "n": 0
}

cheese_add_ons = {
    "y": 1,
    "n": 0
}

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

if size in ("m", "l") and pepperoni == "y":
    pepperoni = "pepperoni_big"


bill = (pizza_size[size]
        + pepperoni_add_ons[pepperoni]
        + cheese_add_ons[extra_cheese])

print(f"Your final bill is: ${bill}.")
