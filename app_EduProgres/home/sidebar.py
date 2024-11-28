import reflex as rx

def sidebar():
    return rx.container(
        rx.vstack(
            rx.heading("Gestión Académica", size="lg", color="white", mb=5),
            rx.link("Mis Calificaciones",color="white",mb=2,),
            rx.link("Progreso Académico",color="white",mb=2,),
            rx.link("Tareas",color="white",mb=2,),
            rx.link("Cargar Exámenes",color="white",mb=2,),
            rx.link("Notificaciones",color="white",mb=2,),
            spacing="4",
            alingn_items="start",
        ),
        background_color="#2c3e50",
        width="250px",
        height="100vh",
        padding="20px",
        position="fixed",
        top="61px",
        left="0"
    )
   