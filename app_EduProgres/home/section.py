import reflex as rx

def main_body():
    return rx.vstack(
            rx.box(
                rx.card(
                    rx.box(
                    rx.heading("Mis calificaciones", size="md"),
                    rx.text("Materia: Matematicas"),
                        rx.unordered_list(
                        rx.list_item("Examen 1: 85%"),
                        rx.list_item("tarea 1: 90%"),
                        ),
                    ),
                     #spacing="3",
                    #margin_top="1em",
                    #padding="10px",
                    margin_bottom="20px"
                ),
                rx.card(    
                    rx.box(
                        rx.heading("Progreso Academico ", size="md"),
                        rx.text("Promedio Actual: 15", mb=2),
                        rx.progress(
                            value=92,
                            color="green",
                            height="20px",
                        )
                    ),
                    margin_bottom="20px"
                ),
                rx.card(
                    rx.heading("Enviar Tareas", size="4"),
                    rx.form(
                        rx.text_area(placeholder="Desceipcion"),
                        rx.button(
                            "Enviar tarea",
                            color="white",
                        ),
                    ),
                    margin_bottom="20px"
                ),
                rx.card(
                    rx.heading("Cargar Exámenes", size="md", mb=3),
                    rx.form(
                        rx.button(
                            "Enviar Examen",
                            background_color="#3498db",
                            color="white",
                        ),
                    ),      
                ),
                rx.card(
                    rx.heading("Notificaciones", size="md", mb=3),
                    rx.text("Trabajo: Proyecto final de Historia"),
                    rx.text("Fecha límite: 30/11/2024"),
                ),
                margin_left="270px",
                margin_top="70px",
                padding="20px",
                #padding="20px",
                width="calc(100% - 270px)",
                height="calc(100vh - 70px)",
                background_color="#ecf0f1",
                overflow="auto",
            ),




    )