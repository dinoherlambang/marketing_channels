#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class marketing_channels(models.Model):

    _name = "crm.lead"
    _description = "crm.lead"

    _inherit = "crm.lead"
    marketing_channels = fields.Char( string="Marketing channels",  help="")
    description = fields.Text( string="Description",  help="")


    chanels_type_id = fields.Many2one(comodel_name="marketing_channels.channels_type",  string="Marketing Channels",  help="")
