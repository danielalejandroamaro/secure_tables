# -*- coding: utf-8 -*-
from openerp import http

# class AuditV2(http.Controller):
#     @http.route('/audit_v2/audit_v2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/audit_v2/audit_v2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('audit_v2.listing', {
#             'root': '/audit_v2/audit_v2',
#             'objects': http.request.env['audit_v2.audit_v2'].search([]),
#         })

#     @http.route('/audit_v2/audit_v2/objects/<model("audit_v2.audit_v2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('audit_v2.object', {
#             'object': obj
#         })