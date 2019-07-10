# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class MroOperationMaintenanceCommon(models.Model):
    _name = "mro.operation_maintenance_equipment"
    _inherit = [
        "mro.operation_maintenance_common"
    ]
    _description = "MRO Operation Maintenance for Equipment"

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(MroOperationMaintenanceCommon, self)
        _super._compute_policy()

    @api.multi
    @api.depends(
        "operation_id",
    )
    def _compute_allowed_mro_object_ids(self):
        _super = super(MroOperationMaintenanceCommon, self)
        _super._compute_allowed_mro_object_ids()

    operation_id = fields.Many2one(
        comodel_name="mro.operation_equipment",
    )
    company_id = fields.Many2one(
        related="operation_id.company_id",
        store=True,
    )
    mro_object_id = fields.Many2one(
        string="Equipment",
        comodel_name="equipment.equipment",
    )
    operation_state = fields.Selection(
        related="operation_id.state",
        store=True,
    )
    kind = fields.Selection(
        related="type_id.kind",
        store=True,
    )
    allowed_mro_object_ids = fields.Many2many(
        comodel_name="equipment.equipment",
        compute="_compute_allowed_mro_object_ids",
    )
