import frappe

def get_context(context):
    shop_name = frappe.form_dict.get("shop_id")
    context.shop = frappe.get_doc("Shop",shop_name)
    if context.shop.rent_amount == 0:
        context.shop.rent_amount = frappe.get_single("Airport Shop Settings").default_rent_amount
    return context