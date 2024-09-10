from odoo import models, fields

class ProproHeader(models.Model):
    _name = 'propro.header'
    _description = 'Producto en Proceso'

    orden_fabricacion = fields.Char(string='Orden de Fabricacion', size=12)
    colada = fields.Char(string='Colada', size=12)
    perfil = fields.Selection([
        ('cuadrado', 'Cuadrado'),
        ('hexagono', 'Hexagono'),
        ('redondo', 'Redondo'),
        ('solera', 'Solera'),
        ('varilla', 'Varilla')
    ], string='Perfil')
    articulo_id = fields.Many2one('product.product', string='Artículos')
    articulo = fields.Char(string='Articulo', size=30)
    descripcion = fields.Char(string='Descripcion', size=50)
    fecha = fields.Date(string='Fecha de Inspección')
    cliente_id = fields.Many2one('res.partner', string='Clientes') 
    cliente = fields.Char(string='Cliente', size=9)
    nombre = fields.Char(string='Nombre', size=35)

    # Define a one2many relation to the detail model
    detail_ids = fields.One2many('propro.detail', 'header_id', string='Detalles')


class ProproDetail(models.Model):
    _name = 'propro.detail'
    _description = 'Atados del Producto en Proceso'

    header_id = fields.Many2one('propro.header', string='Header', required=True)
    atado = fields.Integer(string='Atado')
    piezas = fields.Integer(string='Piezas')
    largo = fields.Integer(string='Largo')
    medida1 = fields.Float(string='Medida 1', digits=(3, 3))
    medida2 = fields.Float(string='Medida 2', digits=(3, 3))
    rechazado = fields.Boolean(string='Rechazado')
    causas_rechazo = fields.Many2many('propro.rejection.cause', string='Causas de Rechazo')

class ProproRejectionCause(models.Model):
    _name = 'propro.rejection.cause'
    _description = 'Causas de Rechazo'

    name = fields.Char(string='Causa de Rechazo', required=True)