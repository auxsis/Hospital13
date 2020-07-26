# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class medical_pathology_group_member(models.Model):
    _name = 'medical.pathology.group.member'

    disease_group_id = fields.Many2one('medical.pathology.group', string="Group", required=True)
