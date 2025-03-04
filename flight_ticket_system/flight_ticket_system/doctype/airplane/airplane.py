# Copyright (c) 2025, Hemil and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class Airplane(Document):
	def autoname(self):
		airline_count = frappe.db.count("Airplane",{"airline":self.airline}) + 1
		self.name = f"{self.airline}-{airline_count}"

