# Declaring Variables
from pyscript import display

restaurant_name = 'CHICHA San Chen' # String
popular_item_price = 195 # Integer
year_established = 1998 # Integer
has_delivery = True # Boolean
product_names = ['Bubble Milk Tea','Dong Ding Oolong Latte','Milk with Brown Sugar Bubble','Cassia Black Tea with Mousse','Lemon Wonderland'] # List
business_hours = '10:00 AM - 10:00 PM' # String
menu_prices = {'Bubble Milk Tea': 195,
               'Dong Ding Oolong Latte': 170,
               'Milk with Brown Sugar Bubble': 220,
               'Cassia Black Tea with Mousse': 170,
               'Lemon Wonderland': 230} # Dictionary

# Displaying Variables
display(f'Try our best-seller for P{popular_item_price}!', target='popular')

display(product_names[0], target='row1col1' )
display(f'P{menu_prices['Bubble Milk Tea']}', target='row1col2')
display(product_names[1], target='row2col1' )
display(f'P{menu_prices["Dong Ding Oolong Latte"]}', target='row2col2')
display(product_names[2], target='row3col1' )
display(f'P{menu_prices['Milk with Brown Sugar Bubble']}', target='row3col2')
display(product_names[3], target='row4col1' )
display(f'P{menu_prices['Cassia Black Tea with Mousse']}', target='row4col2')
display(product_names[4], target='row5col1' )
display(f'P{menu_prices['Lemon Wonderland']}', target='row5col2')

display(f'Since {year_established}', target='since')
display(f'{business_hours}', target='hours')
if has_delivery:
   display(f"Delivery through the CHICHA San Chen app!", target='delivery')