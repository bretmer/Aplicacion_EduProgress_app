import reflex as rx

def barra():
    return rx.container(
        rx.vstack(
            rx.heading("Opciones", size="lg", color="black", mb=5, weight="bold"),
            rx.hstack(
                rx.icon("home"),
                rx.link(
                    "Inicio", 
                    href="/#", 
                    color="white", 
                    mb=2
                ),
            ),
            rx.hstack(
                rx.icon("circle-user"),
                rx.link("Perfil", href="/#",color="white",mb=2,),
            ),
            rx.hstack(
                rx.icon("palette"),
                rx.link("Tema" , href="/#", color="white", mb=2),
            ),
            rx.hstack(
                rx.icon("settings"),
                rx.link(
                    "Configuracion",
                    href="/#",
                    color="white",
                    mb=2,
                ),
            ),
            rx.hstack(
                rx.icon("log-out"),
                rx.link("Cerrar sesion", href="/#",color="white",mb=2,),
            ),
            spacing="4",
            alingn_items="start",
        ),
        background_color="gray",
        width="250px",
        height="100vh",
        padding="20px",
        position="fixed",
        top="61px",
        left="0",
    )
