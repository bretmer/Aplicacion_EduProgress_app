import reflex as rx
def encabezado():
    return rx.hstack(
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(rx.icon("menu"), variant="soft",color="black"),
                ),
                rx.menu.content(
                    rx.menu.item(rx.link("Teacher",href="/principal")),
                    rx.menu.item(rx.link("Estudent", href="/main")),
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
                            "Tarea creadas",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Tareas recientes"),
                    rx.menu.item("Tareas pasadas"),
                    rx.menu.item("Todas las tareas"),
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Examenes creados",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Examenes recientes"),
                    rx.menu.item("Examenes pasados"),
                    rx.menu.item("Todos los examenes"),
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Evaluaciones creadas",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Recientes"),
                    rx.menu.item("Pendientes"),
                    rx.menu.item("Pasadas")
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Gestion de Informes",
                            size="4",
                            weight="medium",
                            color="white"
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                        color="white"
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Pendientes"),
                    rx.menu.item("Nuevos"),
                    rx.menu.item("Recientes"),
                    rx.menu.item("Descargas "),
                ),
            ),
            spacing="7",
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
