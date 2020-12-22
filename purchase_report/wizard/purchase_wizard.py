from odoo import models


class PurchaseWizard(models.TransientModel):
    _name = "purchase.wizard"


    def action_done(self):
        data = {}
        purchase_order = self.env['purchase.order'].search([
            ('state', '=', 'purchase')])
        lst = []
        for purchase in purchase_order:
            for product in purchase.order_line:
                values = {
                    'name': purchase.name,
                    'date_order': purchase.date_order,
                    'product_id': product.product_id.name,
                    'remain_qty': product.product_qty - product.qty_received
                }
                if values['remain_qty'] > 0:
                    lst.append(values)
                    data['values'] = lst
        print('\n\n--------data--------\n\n', data)
        print('\n\n-------lst---------\n\n', lst)
        print('\n\n---order----\n\n', purchase_order)
        return self.env.ref(
            'purchase_report.purchase_line_report').report_action(
            self, data=data)
