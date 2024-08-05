import reflex as rx
from .nav import navbar

def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    """This is my base page layout all of my pages will use this page and the content is replaced by child and logo and color remain same"""
    if hide_navbar:
        return rx.container(
        child,
        # rx.logo(),
        rx.color_mode.button(position="bottom-right")
    )

    return rx.fragment(   #return nothing
        navbar(),
        rx.box(
            child,
            id="my-child-box-layout",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-right"),
        padding = "30em"
    )