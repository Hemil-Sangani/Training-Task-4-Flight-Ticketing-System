import frappe
import calendar
from frappe.utils import today, getdate

def generate_rent_payment_schedule():
    contracts = frappe.get_all("Contract",fields=["tenant","shop","start_date","end_date","rent_amount"])
    if contracts:
        for contract in contracts:
            month = getdate().month
            today_date = getdate(today())
            if month==1:
                month = 12
            else:
                month = month - 1
            if contract.start_date<today_date and contract.end_date >today_date :
                rent_payment = frappe.get_doc({
                    "doctype":"Rent Payment",
                    "tenant" :contract.tenant,
                    "amount":contract.rent_amount,
                    "shop":contract.shop,
                    "month":calendar.month_name[month],
                    "date":today_date,
                })
                rent_payment.insert(ignore_permissions=True)
        frappe.db.commit()
        rent_reminder = frappe.get_single("Airport Shop Settings")
        if rent_reminder.rent_reminder == "Enable":
            send_rent_reminder(contracts)

def send_rent_reminder(contracts):
    tenant_contracts = dict()
    for contract in contracts:
        if contract.tenant in tenant_contracts:
            tenant_contracts[contract.tenant].append([contract.shop,contract.rent_amount])
        else:
            tenant_contracts.update({contract.tenant:[[contract.shop,contract.rent_amount]]})
    
    for tenant,shop_details in tenant_contracts.items():
            email_id = frappe.get_doc("Tenant",tenant).email
            if email_id:
                shops = ', '.join([f"{shop_detail[0]}(Rent Amount is {shop_detail[1]})" for shop_detail in shop_details])
                subject = "Monthly Rent Reminder"
                message = f"Dear {tenant}, your shops {shops} rent is due. Please make the payment."
                frappe.sendmail(
                    recipients=email_id,
                    subject=subject,
                    message=message,
                )
        