import reflex as rx
from .encabezadoBarra import encabezadoBarra
from .seccionCentral import seccionCentral
from .barraLateral import barraLateral
def mainPrincipal():
    return rx.box(
        encabezadoBarra(),
        barraLateral(),
        seccionCentral(),
        align_items="flex-start",
        spacing=0,
    )