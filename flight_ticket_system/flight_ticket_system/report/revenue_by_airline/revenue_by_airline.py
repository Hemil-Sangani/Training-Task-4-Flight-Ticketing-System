# Copyright (c) 2025, Hemil and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	
	columns = [
		{
            "fieldname": "airline",
            "fieldtype": "Link",
            "label": "Airline",
			'options': "Airline"
        },
        {
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "label": "Revenue"
        },
	]
	tickets = frappe.get_all('Airplane Ticket',fields=['name','flight','total_amount'])
	flights = frappe.get_all('Airplane Flight',fields=['name','airplane'])
	airplanes = frappe.get_all('Airplane',fields=['name','airline'])
	flights_to_airplane = {f["name"]:f["airplane"] for f in flights}
	airplanes_to_airline = {a["name"]:a["airline"] for a in airplanes}
	airlines = frappe.get_all('Airline',fields=["name"])
	airline_revenue = {f["name"]:0 for f in airlines}
	for ticket in tickets:
		airline = airplanes_to_airline.get(flights_to_airplane.get(ticket.get("flight")))
		if airline_revenue.get(airline) != None:
			airline_revenue[airline]+= ticket["total_amount"]
	data = [{"airline":airline,"revenue":revenue} for airline,revenue in airline_revenue.items()]
	chart = get_chart(data)
	summary = get_report_summary(data)
	return columns,data, None,chart,summary

def get_chart(data):
	return {
		'data':{
			'labels':[f["airline"] for f in data],
			'datasets':[{'values':[f['revenue'] for f in data]}]
		},
		"type":"donut"

	}

def get_report_summary(data):
	total_revenue = sum([f['revenue'] for f in data])
	return [{
		"value":total_revenue,
		"label":"Total Revenue",
		"indicator":"green",
		"datatype":"Currency"
	}]


