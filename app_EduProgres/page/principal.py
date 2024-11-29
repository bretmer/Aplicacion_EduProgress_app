import reflex as rx
from .encabezado import encabezado
from .seccion import seccion
from .barra import barra
def principal():
    return rx.box(
        encabezado(),
        barra(),
        seccion(),
        align_items="flex-start",
        spacing=0,
    )