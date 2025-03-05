# Copyright (c) 2025, Hemil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
	def before_insert(self):
		alphabet = ['A','B','C','D','E']
		self.seat = f"{random.randint(1,100)}{random.choice(alphabet)}"

	def validate(self):
		add_on_type = []
		total_amount  = self.flight_price
		for add_on in self.add_ons:
			if add_on.item not in add_on_type:
				add_on_type.append(add_on.item)
				total_amount += add_on.amount
			else:
				self.add_ons.remove(add_on)
		self.total_amount = total_amount

	def on_submit(self):
		if self.status!="Boarded":
			frappe.throw("Ticket With Only Boarded Status should be submitted")
