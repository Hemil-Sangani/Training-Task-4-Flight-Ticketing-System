import frappe
import random

def execute():
    flights = frappe.get_all("Airplane Ticket",fields=["name","seat"])
    for flight in flights:
        if not flight['seat']:
            seat_name = f"{random.randint(1,100)}{random.choice(['A','B','C','D','E'])}"
            frappe.db.set_value("Airplane Ticket", flight['name'], "seat", seat_name)