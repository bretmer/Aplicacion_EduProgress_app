import reflex as rx
from .componentes.login_page import login_page
from .componentes.register_page import register_page

def index ()->rx.components:
    return rx.center(
        rx.box(
            rx.text(
                "Bienvenido a EduProgress",
                size="8",
                weight="bold",
                color="blak",
                margin_top="-4em",
                margin_bottom="4em",
            ),
            rx.vstack(
                 rx.button(
                    "INICIAR SESION", 
                    size="4",
                    weight="bold",
                    bg="blue.500",
                    color="white",
                    width="100%",
                    _hover={"bg": "blue.600"},
                    on_click=lambda: rx.redirect("/login_page"),
                    border_radius="30px",
                ),
                rx.button(
                    "REGISTRARME", 
                    size="4",
                    weight="bold",
                    bg="green.500",
                    color="white",
                    _hover={"bg": "green.600"},
                    width="100%",
                    on_click=lambda: rx.redirect("/register_page"),
                    border_radius="30px",
                ),
                spacing="4",
            ),
        ),
        height="100vh",
        bg="linear-gradient(to bottom, #4facfe, #00f2f3)",
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(login_page, route="/login_page")
app.add_page(register_page, route="/register_page")

