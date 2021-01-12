from datetime import datetime
from odoo import fields, models


class ProductWizard(models.TransientModel):
    _name = 'product.wizard'

    partner_id = fields.Many2one('res.partner', string='Vendor', required=True,
                                 change_default=True, tracking=True,
                                 domain="['|', ('company_id', '=', False),\
                                  ('company_id', '=', company_id)]",
                                 help="You can find a vendor by its Name, \
                                  TIN, Email or Internal Reference.")

    company_id = fields.Many2one('res.company', 'Company', required=True,
                                 index=True,
                                 default=lambda self: self.env.company.id)

    def create_po(self):
        selected_product = self.env['product.product'].browse(
            self._context.get('active_ids', []))
        view_id = self.env.ref('purchase.purchase_order_form').id
        pro_list = []
        for product_1 in selected_product:
            pro_list.append(
                (0, 0, {
                    'product_id': product_1.id,
                    'product_qty': 1,
                    'name': product_1.name,
                    'product_uom': product_1.uom_id.id,
                    'price_unit': product_1.list_price,
                    'date_planned': datetime.today(),
                }))
        product = self.env['purchase.order'].create(
            {
                'partner_id': self.partner_id.id,
                'order_line': pro_list
            })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase order',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'res_id': product.id,
            'views': [[view_id, 'form']],
        }
