temp = int(input("Enter Temperature in farenheit:"))

cel = (temp - 32) * 5/9
round = (round(cel, 2))

print(f"The coversion of {temp} degrees farenheit is {round} degrees celius")