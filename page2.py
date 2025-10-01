# Declaring Variables
from pyscript import display, document

year_established = 1998 # Integer
has_delivery = True # Boolean
business_hours = '10:00 AM - 10:00 PM' # String

# Displaying Miscellaneous Variables

display(f'Since {year_established}', target='since')

display(f'{business_hours}', target='hours')
if has_delivery:
   display(f"Delivery through the CHICHA San Chen app!", target='delivery')