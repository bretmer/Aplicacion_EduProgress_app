import reflex as rx
from .header import header
from .section import main_body
from .sidebar import sidebar
def main():
    return rx.box(
        header(),
        sidebar(),
        main_body(),
        align_items="flex-start",
        spacing=0,
    )