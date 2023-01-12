from collections import deque
miligrams_coffein = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

dayli_coffeins = 0
drink = 300

while miligrams_coffein and energy_drinks:

    coffein_in_drink = miligrams_coffein[-1] * energy_drinks[0]

    if coffein_in_drink <= drink:
        miligrams_coffein.pop()
        energy_drinks.popleft()
        drink -= coffein_in_drink
        dayli_coffeins += coffein_in_drink

    elif coffein_in_drink > drink:
        miligrams_coffein.pop()
        energy_drinks.append(energy_drinks.popleft())
        if dayli_coffeins == 0:
            dayli_coffeins = 0
        else:
            dayli_coffeins -= 30
            drink += 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {dayli_coffeins} mg caffeine.")