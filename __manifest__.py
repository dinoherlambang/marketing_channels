#-*- coding: utf-8 -*-

{
	"name": "Marketing Channels",
	"version": "1.0", 
	"depends": [
		'base','crm','web',
	],
	"author": "Dino Herlambang",
	"category": "Utility",
	"website": "dino.herlambang@gmail.com",
	"images": ["static/description/images/main_screenshot.jpg"],
	"price": "10",
	"license": "LGPL-3",
	"currency": "USD",
	"summary": "This is the Marketing Channels module",
	"description": """

Information
======================================================================

* created menus
* created objects
* created views
* logics

""",
	"data": [
		"security/groups.xml",
        "data/channels_type_data.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/marketing_channels.xml", #inherited
		"view/channels_type.xml",
		"report/channels_type.xml",
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}