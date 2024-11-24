import reflex as rx

def register_page():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Crear Cuenta", size="8", color="blue"),
                rx.input(placeholder="Nombres", size="2", width="75%"),
                rx.input(placeholder="Apellidos", size="2", width="75%"),
                rx.input(placeholder="Celular", size="2", width="75%"),
                rx.input(placeholder="Correo electrónico", size="2", width="75%", autocomplete="email"),
                rx.input(placeholder="Contraseña", type_="password", size="2", width="75%"),
                rx.input(placeholder="Confirmar contraseña", type_="password", size="2", width="75%"),
                rx.button("Registrarme", color_scheme="blue", size="3",width="75%"),
                spacing="3",
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            width="460px",
            height="470px",
            padding="20px",
            #background="white",
            #border_radius="40px",
            box_shadow="0px 4px 10px rgba(0, 0, 0, 0.25)",
        ),
        background="gray.100",
        height="100vh",
        #bg="linear-gradient(to bottom, #4facfe, #00f2f3)",
    )
