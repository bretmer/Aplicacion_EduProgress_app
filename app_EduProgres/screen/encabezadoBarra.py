import reflex as rx
def encabezadoBarra():
    return rx.hstack(
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(rx.icon("menu"), variant="solid",color="black"),
                ),
                rx.menu.content(
                    rx.menu.item(rx.link("Teacher",href="/principal")),
                    rx.menu.item(rx.link("Estudent", href="/main")),
                    rx.menu.item(rx.link("Padre", href="/mainPrincipal")),
                    rx.menu.separator(),
                    rx.menu.item("Archive", shortcut="⌘ N"),
                    rx.menu.sub(
                        rx.menu.sub_trigger("More"),
                        rx.menu.sub_content(
                            rx.menu.item("Move to project…"),
                            rx.menu.item("Move to folder…"),
                            rx.menu.separator(),
                            rx.menu.item("Advanced options…"),
                        ),
                    ),
                    rx.menu.separator(),
                    rx.menu.item("Share"),
                    rx.menu.item("Edit"),
                    rx.menu.separator(),
                    rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                ),
            ),
            rx.heading("Menú Principal"),
        ),
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Notificaciones",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white",
                        border="2px solid white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Recibidas"),
                    rx.menu.item("leidas"),
                    rx.menu.item("Todas"),
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Rendimiento academico",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white",
                        border="2px solid white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("En graficas"),
                    rx.menu.item("Informacion Visual"),
                ),
            ),    
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Informes",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white",
                        border="2px solid white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Informe Semanal"),
                    rx.menu.item("Informe Mensual"),
                    rx.menu.item("Informe  Academico de mi hijo")
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Recordatorios",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white",
                        border="2px solid white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("De trabajos de entrega de su hijo"),
                    rx.menu.item("Calificaciones"),
                    rx.menu.item("Proyectos finales de su hijo"),
                ),
            ),
            spacing="9",
            margin_left="150px"
        ),
        #justify="between",
        background="blue",
        padding="1em",
        spacing="2",
        position="fixed",
        width="100%",
        top="0",
    )
