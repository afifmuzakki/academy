# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()


class Aftersales(models.Model):
    _name = 'academy.after_sales'

    aftersales = fields.Html()


class Home(models.Model):
    _name = 'academy.home_page'

    home = fields.Html()


# class academy(models.Model):
#     _name = 'academy.academy'
#     _description = 'academy.academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
