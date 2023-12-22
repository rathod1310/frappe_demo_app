// Copyright (c) 2023, Om Rathod and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	// validate: function(frm) {
	// 	frm.set_value('full_name',frm.doc.first_name+" "+ frm.doc.middle_name+" "+ frm.doc.last_name)
	// 	let row = frm.add_child('family_members',{
	// 		name1:'johnson',
	// 		realation:'father',
	// 		age:56
	// })
	// }

	// enable:function(frm){
	// 	frm.set_df_property('first_name','reqd',1)
	// 	// frm.refresh_field('first_name');

	// 	frm.set_df_property('middle_name','read_only',1)
	// 	// frm.refresh_field('middle_name');

	// 	frm.toggle_reqd('age',true)
	// }

	refresh:function(frm){

// ################Single button###########################

	// 	frm.add_custom_button('clicked me',() =>{
	// 		frappe.msgprint(__('you clicker me....'));
	// })

// ################Dropdown button###########################
		frm.add_custom_button('om',() =>{
			frappe.msgprint(__('my name is om....'));
		},'clicked me')

		frm.add_custom_button('srushti',() =>{
			frappe.msgprint(__('my name is srushti....'));
		},'clicked me')

		frm.add_custom_button('raj',() =>{
			frappe.msgprint(__('my name is raj....'));
		},'clicked me')
}

});




// frappe.ui.form.on('Family Members', {
// 	name1: function(frm){
// 		frappe.msgprint("Child Table Name Event........")
// 	}
// });


// frappe.ui.form.on('Client Side Scripting', {
// 	// after_save: function(frm) {
// 	// 	frappe.msgprint(__("'my name is '{0}", [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name ]))
// 	// }

	
// });

