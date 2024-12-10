import reflex as rx
def header():
    return rx.hstack(
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(rx.icon("menu"), variant="soft",color="black"),
                ),
                rx.menu.content(
                    rx.menu.item(rx.link("Teacher",href="/principal")),
                    rx.menu.item(rx.link("Estudent", href="/main")),
                    rx.menu.item(rx.link("Padre", href="/mainPrincipal")),
                    rx.menu.separator(),
                    rx.menu.item("Archive"),
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
                    rx.menu.item("Edit", shortcut=""),
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
                            "Mis calificaciones",
                            size="4",
                            weight="medium",
                            color="white",
                
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
                    rx.menu.item("Por Materia"),
                    rx.menu.item("Por Tareas"),
                    rx.menu.item("Por Examenes"),
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Progreso academico",
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
                    rx.menu.item("Graficas"),
                    rx.menu.item("Barras"),
                    rx.menu.item("Informe de progreso")
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Tareas",
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
                    rx.menu.item("Pendientes"),
                    rx.menu.item("Nuevas"),
                    rx.menu.item("Terminadas")
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Examenes",
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
                    rx.menu.item("Pendientes"),
                    rx.menu.item("Nuevos"),
                    rx.menu.item("Terminados"),
                ),
            ),
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
                    rx.menu.item("De tareas"),
                    rx.menu.item("De examenes"),
                    rx.menu.item("Avances academicos")
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
