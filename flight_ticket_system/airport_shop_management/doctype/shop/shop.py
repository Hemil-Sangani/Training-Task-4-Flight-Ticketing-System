# Copyright (c) 2025, Hemil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Shop(Document):
	def on_change(self):
		all_shops = frappe.get_all("Shop",filters={"airport":self.airport}, fields=["name","status"])
		available_shops = sum(1 for shop in all_shops if shop.status=="Available")
		occupied_shops = sum(1 for shop in all_shops if shop.status=="Occupied")
		frappe.db.set_value("Airport", self.airport, "available_shops", available_shops, update_modified=True)
		frappe.db.set_value("Airport", self.airport, "lease_shops", occupied_shops, update_modified=True)
		frappe.db.set_value("Airport", self.airport, "total_shops", occupied_shops+available_shops, update_modified=True)
	
	def after_insert(self):
		default_settings = frappe.get_single("Airport Shop Settings")
		if default_settings and default_settings.default_rent_amount:
			self.rent_amount = default_settings.default_rent_amount
			self.save()

