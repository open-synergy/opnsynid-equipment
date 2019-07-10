# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class MroOperationCommon(models.Model):
    _name = "mro.operation_equipment"
    _inherit = [
        "mro.operation_common"
    ]
    _description = "MRO Operation for Equipment"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(MroOperationCommon, self)
        _super._compute_policy()

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "equipment_mro."
            "mro_operation_type_equipment").id

    mro_object_id = fields.Many2one(
        string="Equipment",
        comodel_name="equipment.equipment",
    )
    type_id = fields.Many2one(
        default=lambda self: self._default_type_id(),
    )
    maintenance_ids = fields.One2many(
        comodel_name="mro.operation_maintenance_equipment",
    )

    @api.multi
    def action_open_mro_maintenance(self):
        self.ensure_one()
        return self._get_mro_maintenance_waction(
            "equipment_mro.mro_operation_maintenance_equipment_action")
