# Copyright (c) 2023, Om Rathod and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):
	pass

################SERVER SIDE SCRIPTING EVENTS##################

	# def validate(self):
	# 	frappe.msgprint("This Is Server Side Scripting...")

	# def before_save(self):
	# 	frappe.throw("This Is Server Side Scripting...")

	# def before_insert(self):
	# 	frappe.throw("This Is Server Side Scripting...")

	# def on_update(self):
	# 	frappe.throw("This Is Server Side Scripting...")

	# def before_submit(self):
	# 	frappe.msgprint("This Is Server Side Scripting...")

	# def on_submit(self):
	# 	frappe.msgprint("This Is Server Side Scripting...")
	
	# def on_cancle(self):
	# 	frappe.msgprint("This Is Server Side Scripting...")
	
	# def on_trash(self):
	# 	frappe.msgprint("This Is Server Side Scripting...")

	# def after_delete(self):
	# 	frappe.msgprint("This Is Server Side Scripting...")



########################VALUE FATCHING########################

	# def validate(self):
	# 	frappe.msgprint(_("my name is '{0}' ").format(
	# 		self.first_name+" "+ self.middle_name+" "+ self.last_name))

	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}.the family member name is '{1}' and Realation is '{2}'").format(
	# 			row.idx,row.name1,row.realation))

	############################# get_doc###########################

	# frappe.get_doc(doctype,name)

	# def validate(self):
	# 	self.get_document()
		
	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	frappe.msgprint(_("The First Name is {0} and Age is {1}").format(doc.first_name,doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_("{0}.The family members name is '{1}' and realation is '{2}' ").format(
	# 			row.idx,row.name1,row.realation))


#######################new_doc() & delete_doc()#############################

#This Is For Insert.......
	# def validate(self):
	# 	self.new_document()


	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name ='Ram'
	# 	doc.middle_name ='Siya'
	# 	doc.last_name = 'Ram'
	# 	doc.age =100

	# 	doc.append("family_members",{"name1":"jain",
	# 								"realation":"sister",
	# 								"age":22
	# 								})

	# 	doc.insert()

#this is for delete..........
	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','CLIENT-006')

#some escape hatches that can be used to skip certain checks#

	# doc.insert(
	# 	ignore_permissions =True #ignore write permission during insert
	# 	ignore_links=True #ignore link validation in th document
	# 	ignore_if_duplicate=True #dont insert if duplicaterntry error is thrown
	# 	ignore_mandatory=True #insert if even if mandatory fields are not set
 	# 	)
# doc.save() #
	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name ='Ram'
	# 	doc.middle_name ='Siya'
	# 	doc.last_name = 'Ram'
	# 	doc.age =100
	# 	doc.save()

	# 	doc.save(
	# 	ignore_permissions=True #ignore write permission during insert
	# 	ignore_version=True #do not create a version record
	# 	)

# doc.delete() #
# 	def validate(self):
# 		self.delete_document()

# 	def delete_document(self):
# 		doc = frappe.get_doc('Client Side Scripting','CLIENT-002')
# 		doc.delete()

# doc.db_set() #
# 	def validate(self):
# 		self.db_set_document()

# 	def db_set_document(self):
# 		doc = frappe.get_doc('Client Side Scripting','CLIENT-003')
# 		doc.db_set('age',45)

# # frappe.db.get_list(doctype,filters,or_filters,fields,order_by,group_by,start,page_length) #
# 	def validate(self):
# 		self.get_list()

# 	def get_list(self):
# 		doc = frappe.db.get_list('Client Side Scripting',
# 				filters={
# 					'enable': 1
# 				},
# 				fields=['first_name','age']
# 				)
# 		for d in doc:
# 			frappe.msgprint(_("the parent first name is {0} and age is {1}").format(d.first_name,d.age))


# frappe.db.get_value(doctype,name,fieldname) or frappe.db.get_value(doctype,filters,fieldname) #
	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'CLIENT-003',['first_name','age'])
	# 	frappe.msgprint(_("the parent firstname is {0} and age is {1}").format(first_name,age))

# frappe.db.set_value(doctype, name ,fieldname, value) #
	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting', 'CLIENT-003','age',43)

	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'CLIENT-003',['first_name','age'])
	# 	frappe.msgprint(_("the parent firstname is {0} and age is {1}").format(first_name,age))

# frappe.db.exists(doctype, name) #
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting', 'CLIENT-050'): #true
	# 		frappe.msgprint(_("the document is exists in database"))
	# 	else:
	# 		frappe.msgprint(_("the document does not exists in database"))
		
# frappe.db.count(doctype, filters) #
	# def validate(self):
	# 	doc_count = frappe.db.count('Client Side Scripting', {'enable':1}) #true
	# 	frappe.msgprint(_("the enable document is {0}").format(doc_count))

# frappe.db.sql(query, filters, as_dict) #
	# def validate(self):
	# 	self.sql()

	# def sql(self):

	# 	data = frappe.db.sql("""
	# 							SELECT
	# 								first_name,
	# 								age
	# 							FROM
	# 								`tabClient Side Scripting`
	# 							WHERE
	# 								enable = 1

	# 							""", as_dict=1)


	# 	for d in data:
	# 		frappe.msgprint(_("the parent first name is {0} and age is {1}").format(d.first_name,d.age))


# server side call #
# call a server side msg using client side scripting #
	# enable: function(frm) {
	# 	frm.call({
	# 		doc: frm.doc,
	# 		method: 'frm_call',
	# 		args: {
	# 			msg: "hello"
	# 		},
	# 		freeze: true,
	# 		freeze_message:__("Calling frm_call Method"),
	# 		callback: function(r) {
	# 			frappe.msgprint(r.message)

	# 			#  frappe.msgprint("server side calling complete")

	# 			#  frm.refresh_field('medication_orders'):
	# 		}
	# 	});
	# }


##########py
	