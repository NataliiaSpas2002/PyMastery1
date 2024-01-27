# Homework_3
# Task 1

sales_revenue_forecast = 1000000
sales_ebitda_forecast = sales_revenue_forecast * 0.23
print(f'Sales EBITDA forecast: {sales_ebitda_forecast}')

# Task 2

land_area = 10000
land_area_in_acres = land_area / 4047
formatted_land_area_in_acres = "{:.2f}".format(land_area_in_acres)
print(f'Land area in acres: {formatted_land_area_in_acres}')

# Task 3

purchase_amount = 110
federal_tax = purchase_amount * 0.05
regional_tax = purchase_amount * 0.025
total_tax = federal_tax + regional_tax
total_sle_amount = purchase_amount + total_tax
print(f'Purchase amount: {purchase_amount} \nFederal tax: {federal_tax}'
      f'\nRegional tax: {regional_tax} \nTotal tax: {total_tax} \nTotal sales amount: {total_sle_amount}')

# Task 4
# Сделайте так, чтобы число секунд отображалось в виде <дни:часы:минуты:секунды>.

total_seconds = 200000
days = total_seconds // 86400
hours = total_seconds % 86000 // 3600
minutes = total_seconds % 86400 % 3600 // 60
seconds = total_seconds % 86400 % 3600 % 60

print(f'There is {days} days {hours} hours {minutes} minutes and {seconds} in {total_seconds}')

# Task 5
# При заданном целом числе n посчитайте n + nn + nnn.
# Попробуй подставить вместо 10 цифру 5, и у тебя должно получаться 5 + 55 + 555 = 615
# в твоем варианте должно быть 10 + 110 + 1110 = 1230
my_number = 10
print(my_number + my_number * 11 + my_number * 111)


# Task 6
speed_in_km_h = 1000
speed_in_m_sec = 1000
converted_speed = speed_in_km_h * 1000 / 3600
if converted_speed < speed_in_m_sec:
      print(f'{speed_in_km_h} kilometers per second is less then {speed_in_m_sec} meters per second')




