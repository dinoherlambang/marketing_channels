#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class channels_type(models.Model):

    _name = "marketing_channels.channels_type"
    _description = "marketing_channels.channels_type"
    name = fields.Char( required=True, string="Marketing Channels",  help="")
    description = fields.Text( string="Description",  help="")


