import reflex as rx

def sidebar():
    return rx.container(
        rx.vstack(
            rx.heading("Opciones", size="lg", color="black", mb=5, weight="bold"),
            rx.link("Historial", href="/", color="white", mb=2),
            rx.link("Descargas",href="/",color="white",mb=2,),
            rx.link("Perfil", href="/",color="white",mb=2,),
            rx.link("Cuenta", href="/",color="white",mb=2,),
            rx.link("Idioma", href="/" ,color="white",mb=2,),
            rx.link("Tema" , href="/", color="white", mb=2),
            rx.link("Configuracion",href="/#",color="white",mb=2,),
            rx.link("Ayuda", href="/", color="white", mb=2),
            rx.link("Cerrar sesion", href="/",color="white",mb=2,),
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


