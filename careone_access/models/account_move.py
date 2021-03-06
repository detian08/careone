# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    current_group_account = fields.Boolean(compute="_compute_current_group_account")

    def _compute_current_group_account(self):
        flag = self.pool.get('res.users').has_group(self.env.user, 'careone_access.careone_accountant')
        if flag:
            self.current_group_account = True
        else:
            self.current_group_account = False
