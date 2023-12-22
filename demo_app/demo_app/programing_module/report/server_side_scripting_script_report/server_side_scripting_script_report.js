// Copyright (c) 2023, Om Rathod and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Server Side Scripting Script Report"] = {
	"filters": [
		{
			"fieldname":"name",
			"label":__("Server Side Scripting"),
			"fieldtype":"Link",
			"options":"Server Side Scripting"
		},
		{
			"fieldname":"dob",
			"label":__("DOB"),
			"fieldtype":"Date",
		},
		{
			"fieldname":"age",
			"label":__("Age"),
			"fieldtype":"Data",
		}
	]
};
