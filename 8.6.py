distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100km: '))
total_fuel_consumption = distance * (fuel_consumption/100)
total_cost = total_fuel_consumption * fuel_price
print(f'cena:{total_cost}')
