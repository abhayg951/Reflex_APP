import reflex as rx

from ..Reflex_APP import base_page

# @rx.page(route="/about")
def about_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("About us", size="9"),
            rx.text(
                "this is the simple about us page"
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh"
        ),
        hide_navbar=False
    )