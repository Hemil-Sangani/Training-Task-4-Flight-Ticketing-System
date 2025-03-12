import frappe

def get_context(context):
    context.shops = frappe.get_all("Shop", fields=["name", "shop_number", "status"])
    return context