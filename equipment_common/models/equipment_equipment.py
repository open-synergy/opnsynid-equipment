# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class EquipmentEquipment(models.Model):
    _name = "equipment.equipment"
    _description = "Equipment"

    name = fields.Char(
        string="Equipment",
        required=True,
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    partner_id = fields.Many2one(
        string="Owner",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
        required=False,
    )
    parent_id = fields.Many2one(
        string="Parent Equipment",
        comodel_name="equipment.equipment",
    )
    note = fields.Text(
        string="Note",
    )
