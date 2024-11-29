import reflex as rx

def main_body():
    return rx.vstack(
            rx.box(
                rx.card(
                    rx.box(
                    rx.heading("Mis calificaciones", size="md"),
                    rx.text("Filtrar calificacion:"),
                        rx.select(
                            ["Bimestre","Trimestre", "Semestre", "Materia"],
                            id="filter",
                            default_value="Materia",
                            width="100%"
                        ),
                    rx.text("Materia: Matematicas"),
                        rx.unordered_list(
                        rx.list_item("Examen 1: 85%"),
                        rx.list_item("tarea 1: 90%"),
                        ),
                        margin_left="40px"
                    ),
                    #spacing="3",
                    #margin_top="1em",
                    #padding="10px",
                    margin_bottom="20px",
                    width="90%",
                    margin_left="70px",
                ),
                rx.card(    
                    rx.box(
                        rx.heading("Progreso Academico ", size="md"),
                        rx.text("Promedio Actual: 14", mb=2),
                        rx.progress(
                            value=70,
                            color="green",
                            height="20px",
                        ),
                        margin_left="40px"
                    ),
                    margin_bottom="20px",
                    width="90%",
                    margin_left="70px",
                ),
                rx.card(
                    rx.heading("Enviar Tareas", size="md"),
                    rx.form(
                        rx.input(
                            type="file", 
                            placeholder="Subir un archivo",
                            margin_top="1em",
                            # padding="10px",
                            # border="1px solid #ddd",
                            # border_radius="5px",
                            
                        ),
                        rx.text_area(placeholder="Descripcion"),
                        rx.button(
                            "Enviar tareas",
                            color="white",
                            width="100%",
                            padding="10px",
                            margin_top="1em"
                        ),
                        #margin_left="40px",
                    ),
                    margin_bottom="20px",
                    margin_left="70px",
                    width="90%"
                ),
                rx.card(
                    rx.heading("Cargar Exámenes", size="md", mb=3),
                    rx.form(
                        rx.text_area(placeholder="Descripcion"),
                        rx.button(
                            "Enviar Examen",
                            background_color="#3498db",
                            color="white",
                            width="100%",
                            padding="10px",
                            margin_top="1em"
                        ),
                        #margin_left="40px",
                    ),
                    margin_bottom="20px",
                    width="90%",
                    margin_left="70px",     
                ),
                rx.card(
                    rx.box(
                        rx.heading("Notificaciones", size="md", mb=3),
                        rx.text("Trabajo: Proyecto final de Historia"),
                        rx.hstack(
                            rx.icon(tag="calendar"),
                            "Fecha límite: 30/11/2024", 
                        ),
                    ),
                    width="90%",
                    margin_left="70px",  
                ),
                margin_left="250px",
                margin_top="65px",
                padding="20px",
                #padding="20px",
                width="calc(100% - 260px)",
                height="calc(100vh - 70px)",
                background_color="#ecf0f1",
                overflow="auto",
            ),




    )