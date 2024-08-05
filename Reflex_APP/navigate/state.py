import reflex as rx

from . import routes

class NavState(rx.State):
    
    def to_home(self):
        return rx.redirect(routes.HOME_PAGE_URL)
    
    def to_about(self):
        return rx.redirect(routes.ABOUT_PAGE_URL)
    
    def to_price(self):
        return rx.redirect(routes.PRICE_PAGE_URL)
    
    def to_contact(self):
        return rx.redirect(routes.CONTACT_PAGE_URL)