import reflex as rx

def seccionCentral():
    return rx.vstack(
            rx.box(
                rx.card(
                    rx.box(
                        rx.heading("Gestion de Tareas", size="md"),
                        rx.text("Titulo de la Tarea:"),
                        rx.input(id="task-title",placeholder="Escribe el titulo de la tarea"),
                        rx.text("Enlaces a recursos:"),
                        rx.input(id="task-link", placeholder="Ingresa un enlace (opcional)", type="url"),
                        rx.text("Nivel de dificultad:"),
                        rx.select(
                            ["Basico", "Intermedio", "Avanzado"],
                            id="dificulty",
                            default_value="Basico",
                            width="100%"
                        ),
                        rx.button(
                            "Crear Nueva Tarea",
                            color="White",
                            width="100%",
                            margin_top="1em",
                        ),
                        margin_left="10px",
                    ),
                    #spacing=3,
                    #margin_top="1em",
                    #padding="10px",
                    margin_bottom="20px",
                    width="90%",
                    margin_left="70px",
                ),
                rx.card(
                    rx.box(
                        rx.heading("Gestion de Examen", size="md"),
                        rx.text("Titulo del examen:"),
                        rx.input(id="task-title",placeholder="Escribe el titulo del examen"),
                        rx.text("Enlaces a recursos:"),
                        rx.input(id="task-link", placeholder="Ingresa un enlace", type="url"),
                        rx.text("Nivel de dificultad:"),
                        rx.select(
                            ["Basico", "Intermedio", "Avanzado"],
                            id="dificulty",
                            default_value="Basico",
                            width="100%"
                        ),
                        rx.button(
                            "Crear examen",
                            color="White",
                            width="100%",
                            margin_top="1em",
                        ),
                        margin_left="10px",
                    ),
                    #spacing=3,
                    #margin_top="1em",
                    #padding="10px",
                    margin_bottom="20px",
                    width="90%",
                    margin_left="70px",
                ),
                rx.card(
                    rx.box(
                        rx.heading("Evaluaciones Personalizadas", size="lg"),
                        rx.text("Título de la Evaluacion:"),
                        rx.input(id="evaluation-title", placeholder="Escribe el titulo de la evaluacion"),
                        rx.text("Fecha de Evaluacion:"),
                        rx.input(id="evaluation-date", type="date", pr="3em"),
                        rx.text("Hora de la evaluacion:"),
                        rx.input(id="evaluation-time", type="time", pr="3em"),
                        rx.button(
                            "Crear Evaluacion",
                            color="white",
                            on_click=lambda: rx.toast("Evaluacion creado exitosamente"),
                            width="100%",
                            margin_top="1em"
                        ),
                        margin_left="10px",
                    ),
                    margin_bottom="20px",
                    margin_left="70px",
                    width="90%"
                ),
                rx.card(    
                    rx.box(
                        rx.heading("Gestion de Informes ", size="lg"),
                        rx.hstack(
                            rx.button(
                                "Generar Informe",
                                color="white",
                                on_click=lambda: rx.toast("Informe generado correctamente"),
                                width="30%"
                            ),
                            rx.button(
                                "Descargar Informe (PDF)",
                                color="white",
                                on_click=lambda: rx.download("/Informe-estudiante.pdf"),
                                width="30%"
                            ),
                            rx.button(
                                "Descargar Informe (Excel)",
                                color="white",
                                on_click=lambda: rx.download("/Informe-estudiante.cvs"),
                                width="30%"
                            ),
                            spacing="8",
                            margin_top="1em"
                        ),
                        margin_left="10px",
                    ),
                    margin_bottom="20px",
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