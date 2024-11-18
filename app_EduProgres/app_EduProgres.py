import reflex as rx
from .componentes.login_page import login_page
def index()->rx.components:
    return rx.box(
        login_page()
    )

app = rx.App()
app.add_page(index, title="Iniciar Sesión")

