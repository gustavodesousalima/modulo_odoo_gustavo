from odoo import models, fields

class MeuPedidoVenda(models.Model):
    _name = 'modelo.odoo.gustavo'
    _description = 'Módulo feito por Gustavo'
    
    name = fields.Char(
        string='Nome do Pedido',
        required=True
        )

    description = fields.Text(
        string="Descrição do Pedido",
        required=True
        )

    date_order = fields.Date(
        string='Data do Pedido', 
        default=fields.Date.today()
        )

    valor_total = fields.Float(
        string="Valor total do Pedido",
        required=True,
        digits=(10, 2)
    )

    ja_entregue = fields.Boolean(
        string="Já entregue ?",
        hekp="Marque se o pedido já foi entregue",
        required=True,
        default=False
    )

    tipo_pedido = fields.Selection(
        string="Origem do Pedido",
        selection=[('nacional', 'Nacional'), ('exterior', 'Exterior')],
        required=True
    )
    
