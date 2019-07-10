# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class EquipmentEquipment(models.Model):
    _name = "equipment.equipment"
    _inherit = [
        "equipment.equipment",
        "mro.object_common",
    ]

    operation_ids = fields.One2many(
        comodel_name="mro.operation_equipment",
    )
    maintenance_ids = fields.One2many(
        comodel_name="mro.operation_maintenance_equipment",
    )

    @api.multi
    def action_open_mro_operation(self):
        self.ensure_one()
        return self._get_mro_operation_waction(
            "equipment_mro.mro_operation_equipment_action"
        )

    @api.multi
    def action_open_mro_maintenance(self):
        self.ensure_one()
        return self._get_mro_operation_waction(
            "equipment_mro.mro_operation_maintenance_equipment_action"
        )
