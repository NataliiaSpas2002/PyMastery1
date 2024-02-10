weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

daily_sales_volume = []

for day in weekdays:
    sales_volume = input(f'Pleas enter daily sales volume on {day}: ')
    while not sales_volume.isnumeric():
        print('Invalid input. Please enter a valid integer.')
        sales_volume = input(f'Please enter daily sales volume on {day}: ')

    daily_sales_volume.append(int(sales_volume))

total_sales = sum(daily_sales_volume)

for i in range(len(weekdays)):
    day = weekdays[i]
    sales_volume = daily_sales_volume[i]
    print(f'{day}: {sales_volume}')

print(f'Sales volume from Monday to Sunday: {daily_sales_volume}')
print(f'Weekly sales volume: {total_sales}')