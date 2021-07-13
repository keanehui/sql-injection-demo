from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from sqli0.models import Customer
from django.db import connection


# Create your views here.
def show_index(request):
    num_entries = None
    with connection.cursor() as cursor:
        query_str: str = "SELECT COUNT(id) FROM sqli0_customer"
        cursor.execute(query_str)
        num_entries = cursor.fetchone()[0]
    return render(request, "index.html", {
        'num_entries': num_entries
    })

def show_result(request): 
    firstName: str = ""
    try: 
        firstName = request.GET['firstName']
    except:
        pass
    password: str = ""
    try:     
        password = request.GET['password']
    except: 
        pass

    query_result = None
    with connection.cursor() as cursor:
        query_str: str = "SELECT * FROM sqli0_customer WHERE first_name='" + firstName + "' AND password='" + password + "';" 
        # SELECT * FROM sqli0_customer WHERE first_name='{firstName}' AND password='password'; 
        cursor.execute(query_str)
        customers = cursor.fetchall()

    return render(request, "result.html", {
        'query_str': query_str, 
        'col_names': ["ID", "First Name", "Last Name", "Phone", "Date of Birth", "Password"], 
        'customers': customers
    })


    # Union sqli
    # dynamic num columns