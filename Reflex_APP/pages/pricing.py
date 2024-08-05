import reflex as rx

from ..Reflex_APP import base_page

def price_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Pricing", size="9"),
            rx.text(
                "You can see the pricing here"
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh"
        ),
        hide_navbar=False
    )