// Copyright (c) 2025, Hemil and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.page.add_action_item("Assign Seat",()=>{
            let d = new frappe.ui.Dialog({
                title: "Select Seat",
                fields: [
                    {
                        label: "Seat Number",
                        fieldname: 'seat',
                        fieldtype: 'Data'
                    }
                ],
                size:"small",
                primary_action_label:"Assign",
                primary_action(values){
                    frm.set_value('seat',values.seat)
                    d.hide()
                }
            })
            d.show()
        })
	},
});
