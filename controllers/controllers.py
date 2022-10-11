# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([])
        })

    # New route
    @http.route('/academy/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/academy/<int:id>/', auth='public', website=True)
    def teacher(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })

    # @http.route('/academy/aftersales/', auth='public', website=True)
    # def index(self, **kw):
    #     return http.request.render('academy.after_sales')


class Home(http.Controller):
    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.home_page')


class Aftersales(http.Controller):
    @http.route('/aftersales/', auth='public', website=True)
    def aftersales(self, **kw):
        return http.request.render('academy.after_sales')


class Product(http.Controller):
    @http.route('/product/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.product_page')


class Promo(http.Controller):
    @http.route('/promo/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.promo_page')


class Apparel(http.Controller):
    @http.route('/aftersales/apparel/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.apparel_page')


class BookingService(http.Controller):
    @http.route('/aftersales/booking-service/', auth='public', website=True)
    def aftersales(self, **kw):
        return http.request.render('academy.booking_service')


class LiveChat(http.Controller):
    @http.route('/live-chat/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.live_chat')


class NearestDealer(http.Controller):
    @http.route('/dealer-terdekat/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.nearest_dealer')


class Pricelist(http.Controller):
    @http.route('/pricelist/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.pricelist_page')


class ProductDetail(http.Controller):
    @http.route('/product-detail/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.product_detail')


class News(http.Controller):
    @http.route('/news/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.news_page')


class EstimatedPrice(http.Controller):
    @http.route('/aftersales/estimated-price/', auth='public', website=True)
    def aftersales(self, **kw):
        return http.request.render('academy.estimated_price')


class SpareParts(http.Controller):
    @http.route('/aftersales/spare-parts/', auth='public', website=True)
    def aftersales(self, **kw):
        return http.request.render('academy.spare_parts')


class SpareParts(http.Controller):
    @http.route('/unit-order/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.unit_order')


class SpareParts(http.Controller):
    @http.route('/service-order/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.service_order')


class SpareParts(http.Controller):
    @http.route('/apparel-order/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.apparel_order')


class SpareParts(http.Controller):
    @http.route('/apparel-detail/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('academy.apparel_detail')

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })
