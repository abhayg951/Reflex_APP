"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page

from . import pages, navigate


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    # def change_heading(self):
    #     if self.label == "Welcome to Reflex!":
    #         self.label = "Hello, my name is Thomas."
    #     else:
    #         self.label = "Welcome to Reflex!"
    
    def change_label_from_input(self, val):
        self.label = val
    ...



def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link("About us", href=navigate.routes.ABOUT_PAGE_URL),
            rx.input(
                default_value=State.label,
                on_change=State.change_label_from_input
            ),
            rx.link(
                rx.button("Click me"),
                # on_click=State.change_heading
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh"
        ),
        hide_navbar=False
    )

app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route=navigate.routes.ABOUT_PAGE_URL)
app.add_page(pages.price_page, route=navigate.routes.PRICE_PAGE_URL)
