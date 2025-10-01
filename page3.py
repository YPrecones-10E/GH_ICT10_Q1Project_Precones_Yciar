# Declaring Variables
from pyscript import display, document

popular_item_price = 195 # Integer
year_established = 1998 # Integer
has_delivery = True # Boolean
business_hours = '10:00 AM - 10:00 PM' # String

# Function
def order(e):
    document.getElementById('summhead').innerHTML = ""
    document.getElementById('total').innerHTML = ""
    document.getElementById('summ').innerHTML = ""

    summhead = document.getElementById('summhead')
    summhead.classList.remove("d-none")

    cont = document.getElementById('cont')
    cont.classList.remove("d-none")

    item1=document.getElementById('menu1')
    item2=document.getElementById('menu2')
    item3=document.getElementById('menu3')
    item4=document.getElementById('menu4')
    item5=document.getElementById('menu5')
    
    total = (float(item1.value) * item1.checked +
    float(item2.value) * item2.checked +
    float(item3.value) * item3.checked +
    float(item4.value) * item4.checked +
    float(item5.value) * item5.checked)

    name = document.getElementById('name').value
    address = document.getElementById('address').value
    contact = document.getElementById('contact').value

    summary = f"""
    Name: {name}
    Address: {address}
    Contact Number: {contact}
    """

    display (f'Order Summary', target='summhead')
    display (f'Total Amount: P{total}', target='total')
    display(f'{summary}', target='summ')

# Displaying Miscellaneous Variables
display(f'Try our best-seller for P{popular_item_price}!', target='popular')

display(f'Since {year_established}', target='since')

display(f'{business_hours}', target='hours')
if has_delivery:
   display(f"Delivery through the CHICHA San Chen app!", target='delivery')