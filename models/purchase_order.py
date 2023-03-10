# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    x_comparativo = fields.Char(string="No. Comparativo")
    x_direccion_env = fields.Char(string="Dirección de Envío")
