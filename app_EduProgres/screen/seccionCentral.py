import reflex as rx

def seccionCentral():
    return rx.vstack(
            rx.box(
                rx.card(
                    rx.box(
                        rx.heading("Notificaciones", size="md"),
                        # rx.hstack(
                        #     rx.button("Marcar como leidas", width="30%"),
                        #     rx.button("Filtrar por asignatura", width="30%"),
                        #     rx.button("Filtrar por categoria", width="30%"),
                        #     spacing="8",
                        #     margin_top="1em"
                        # ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Curso"),
                                    rx.table.column_header_cell("Notificacion"),
                                    rx.table.column_header_cell("Calificacion obtenida"),
                                    rx.table.column_header_cell("Estado"),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell("Matematicas"),
                                    rx.table.cell("Examen parcial calificado"),
                                    rx.table.cell("85"),
                                    rx.table.cell(
                                        rx.button("Marcar como leido")
                                    ),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell("Historia"),
                                    rx.table.cell("Proyecto entregado"),
                                    rx.table.cell("92"),
                                    rx.table.cell(
                                        rx.button("leido")
                                    ),
                                ),
                            ),
                            margin_bottom="20px",
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
                        rx.heading("Rendimiento Academico", size="md"),
                        rx.hstack(
                            rx.button(
                                "Ver Graficos",
                                color="White",
                                width="46%",
                                margin_top="1em",
                            ),
                            rx.button(
                                "Ver informes visuales",
                                color="White",
                                width="48%",
                                margin_top="1em",
                            ),
                            spacing="9",
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
                        rx.heading("Informes", size="lg"),
                        rx.text("Haz clik en un informe para revisarlo directamente:"),
                        rx.hstack(
                            rx.button("Informe Semanal",width="48%"),
                            rx.button("Informe Mensual", width="48%"),
                            margin_top="0.5em",
                            spacing="7"
                            
                        ),
                        rx.hstack(
                            rx.button("Descargar informe", width="100%"),
                            margin_top="0.5em"
                        )
                    ),
                    margin_left="70px",
                    width="90%",
                    margin_bottom="20px",
                ),
                rx.card(    
                    rx.box(
                        rx.heading("Recordatorios ", size="lg"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Fecha"),
                                    rx.table.column_header_cell("Actividad"),
                                    rx.table.column_header_cell("Curso"),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell("2024-12-10"),
                                    rx.table.cell("Entrega de proyecto"),
                                    rx.table.cell("Historia"),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell("2024-12-15"),
                                    rx.table.cell("Examen final"),
                                    rx.table.cell("Matematicas"),
                                ),
                            ),
                            margin_bottom="20px",
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