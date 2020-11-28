from django.shortcuts import render
from dbms.models import *
# import cx_Oracle

# Global variables
test = "1"
# connection = cx_Oracle.connect('c##user1','password',"localhost:1521/orcl")
# cursor = connection.cursor()

# Index page
def index(request):
    return render(request, 'index.html', {"test":test})

# Listing all tables
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def list_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'driver.html', {'drivers': drivers })

def list_grocerystore(request):
    grocerystores = GroceryStore.objects.all()
    return render(request, 'grocerystore.html', {'groceryStores': grocerystores})

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant.html', {'restaurants': restaurants})

def list_storebranch(request):
    store_branches = StoreBranch.objects.all()
    return render(request, 'storebranch.html', {'storebranches':store_branches})

def list_restaurantbranch(request):
    restaurant_b = RestaurantBranch.objects.all()
    return render(request,'restaurantBranch.html', {'restaurantbranches':restaurant_b})

# SQL Query pages
def create_table(request):
    print("Hello world!")
    return render(request, 'create_table.html')

def drop_table(request):
    return render(request, 'drop_table.html')

def populate_table(request):
    return render(request, 'populate_table.html')

def query(request):
    return render(request, 'query.html')

# def execute_sql_script(filename):
#     f = open(f'{filename}.sql','r')
#     sql_file_context = f.read()
#     f.close()

#     sql_commands = sql_file_context.split(";")
#     for command in sql_commands:
#         try:
#             cursor.execute(command)
#         except (Exception) as msg:
#             print(f"Command skipped: {msg}")

            

