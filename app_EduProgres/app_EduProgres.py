import reflex as rx
from .components.login_page import login_page
from .components.register_page import register_page
from .home.main import main
from .page.principal import principal
from .screen.mainPrincipal import mainPrincipal

def index ()->rx.components:
    return rx.center(
        rx.box(
            rx.text(
                "¡Bienvenido a EduProgress!",
                size="8",
                weight="bold",
                color="black",
                margin_top="-1em",
                margin_bottom="em",
            ),
            rx.text("Como estudiante mira tus rendimientos academicos",weight="bold",size="3",align="center",margin_top="1em"),
            rx.text("en un solo lugar",align="center",size="3",weight="bold"),
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
                margin_top="4em"
            ),
        ),
        height="100vh",
        background_image="url('https://st.depositphotos.com/1001564/2470/i/450/depositphotos_24704059-stock-photo-background.jpg')",
        background_size="cover",
        background_position="center",
        #bg="linear-gradient(to bottom, #4facfe, #00f2f3)",
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(login_page, route="/login_page")
app.add_page(register_page, route="/register_page")
app.add_page(main, route="/main")
app.add_page(principal, route="/principal")
app.add_page(mainPrincipal, route="/mainPrincipal")


