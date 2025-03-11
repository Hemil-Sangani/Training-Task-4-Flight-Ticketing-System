import frappe

def send_rent_reminder():
    tenants = frappe.get_all("Tenant",fields=["name",'email'])
    rent_reminder = frappe.get_single("Airport Shop Settings")
    if rent_reminder.rent_reminder == "Enable":
        for tenant in tenants:
            subject = "Monthly Rent Reminder"
            message = f"Dear {tenant['name']}, your shop rent is due. Please make the payment."
            print(tenant["email"])
            frappe.sendmail(
                recipients=tenant["email"],
                subject=subject,
                message=message,
            )
        