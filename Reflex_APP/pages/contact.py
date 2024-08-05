import reflex as rx

from ..Reflex_APP import base_page
from .. import navigate

@rx.page(route=navigate.routes.CONTACT_PAGE_URL)
def contact_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact us", size="9"),
            rx.text(
                "This is the contact us page"
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh"
        ),
        hide_navbar=False
    )