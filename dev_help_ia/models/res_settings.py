# -*- coding: utf-8 -*-
"""
Autor: Luis Fernando Hinojosa Flores
"""

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_key =  fields.Char(
        string="API Key", 
        help="Introduce tu api aqui", 
        config_parameter="dev_help_ia.api_key"
    )
