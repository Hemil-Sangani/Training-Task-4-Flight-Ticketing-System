# Copyright (c) 2025, Hemil and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def before_submit(self):
		self.status = "Completed"

	def on_change(self):
		if self.has_value_changed("gate_number"):
			frappe.enqueue(update_ticket_gate_number,queue='short',flight=self.name,new_gate_number=self.gate_number)

def update_ticket_gate_number(flight,new_gate_number):
	tickets = frappe.get_all("Airplane Ticket",filters={"flight":flight},fields=["name"])
	for ticket in tickets:
		frappe.db.set_value("Airplane Ticket",ticket["name"],"gate_number",new_gate_number,update_modified=True)
	frappe.db.commit()