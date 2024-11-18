import reflex as rx

def login_page():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Iniciar Sesión", size="8", color="blue.600"),
                rx.input(placeholder="Correo electrónico",size="3",width="100%"),
                rx.input(placeholder="Contraseña", type_="password",size="3",width="100%"),
                rx.button("Iniciar Sesión", color_scheme="blue",size="4"),
                rx.text("¿Olvidaste tu contraseña?", color="blue", font_size="sm", cursor="pointer"),
                spacing="4",
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            width="500px",
            padding=10,
            background="white",
            border_radius="40px",
            box_shadow="0px 4px 10px rgba(0, 0, 0, 0.25)",
        ),
        background="gray.100",
        height="100vh",
    )
