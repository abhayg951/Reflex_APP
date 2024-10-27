import reflex as rx

from ..Reflex_APP import base_page
from .. import navigate

class ContactFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
    
    print(form_data)

@rx.page(route=navigate.routes.CONTACT_PAGE_URL)
def contact_page() -> rx.Component:
    my_form = (
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                    placeholder="First Name",
                    name="first_name",
                    required=True,
                    width = "100%"
                    ),
                    rx.input(
                    placeholder="Last Name",
                    name="last_name",
                    required=True,
                    width = "100%"
                    ),
                    width = "100%"
                ),
                
                rx.input(
                    type="email",
                    placeholder="Email",
                    required=True,
                    width = "100%"
                ),
                rx.text_area(
                    name="message",
                    placeholder="Your message here",
                    required=True,
                    width = "100%"
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactFormState.handle_submit,
            reset_on_submit=True,
        ),
    )
    return base_page(
        rx.vstack(
            rx.heading("Contact us", size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width = "50vw"
                )
            ),
            rx.mobile_and_tablet(
                rx.box(
                    my_form,
                    width = "50vw"
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        ),
        hide_navbar=False
    )