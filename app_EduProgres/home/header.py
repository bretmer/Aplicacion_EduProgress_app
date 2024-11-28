import reflex as rx
def header():
    return rx.hstack(
        rx.hstack(
            rx.heading("Menú Principal"),
        ),

        rx.hstack(
            rx.link("Mis Calificaciones", href="#calificaciones_page" , color="white", mb=2, justify="center",spacing="1"),
            rx.link("Progreso", href="#progreso_page", color="white", mb=2, justify="center",spacing="1"),
            rx.link("Tareas", href="#tareas_page", color="white", mb=2, justify="center"),
            rx.link("Exámenes", href="#examenes_page", color="white", mb=2, justify="center"),
            rx.link("Notificaciones", href="#notificaciones_page", color="white", mb=2, justify="center"),
        ),
        justify="between",
        background="blue",
        padding="1em",
        spacing="2",
        position="fixed",
        width="100%",
        top="0",
    )
    # rx.box(
    #     rx.container(
    #         rx.hstack(
    #             rx.link("eduproges",align="left"),
    #         ),
    #         rx.hstack(
    #         #rx.heading("EduProgress", size="lg", color="re", mb=5),
    #         rx.link("Mis Calificaciones", href="#" , color="white", mb=2),
    #         # background_color="#2c3e50",
    #         # width="250px",
    #         # height="100vh",
    #         # padding="20px",
    #         # position="fixed",
    #         # color="white",
    #         ),
    #         background="blue"
    #     ),

    # ),

    



# def main_content():
#     """Crea el contenido principal."""
#     return rx.box(
#         rx.box(
#             rx.heading("Mis Calificaciones", size="md", mb=3),
#             rx.link("Materia: Matemáticas"),
#             rx.unordered_list(
#                 rx.list_item("Examen 1: 85%"),
#                 rx.list_item("Tarea 1: 90%"),
#             ),
#             id="calificaciones",
#         ),
#         rx.box(
#             rx.heading("Progreso Académico", size="md", mb=3),
#             rx.link("Aquí se mostrarán gráficos de progreso (placeholder)."),
#             rx.link("Promedio Actual: 9.2"),
#             id="grafica",
#         ),
#         rx.box(
#             rx.heading("Enviar Tareas", size="md", mb=3),
#             rx.form(
#                 rx.textarea(placeholder="Descripción", mb=3),
#                 rx.file_input(mb=3),
#                 rx.button(
#                     "Enviar Tarea",
#                     on_click=lambda: print("Tarea enviada con éxito"),
#                     background_color="#3498db",
#                     color="white",
#                 ),
#             ),
#             rx.link("Su tarea ha sido enviada con éxito.", color="green", mt=3),
#             id="tareas",
#         ),
#         rx.box(
#             rx.heading("Cargar Exámenes", size="md", mb=3),
#             rx.form(
#                 rx.file_input(mb=3),
#                 rx.button(
#                     "Enviar Examen",
#                     on_click=lambda: print("Examen enviado con éxito"),
#                     background_color="#3498db",
#                     color="white",
#                 ),
#             ),
#             rx.link("Su examen ha sido enviado con éxito.", color="green", mt=3),
#             id="examenes",
#         ),
#         rx.box(
#             rx.heading("Notificaciones", size="md", mb=3),
#             rx.link("Trabajo: Proyecto final de Historia"),
#             rx.link("Fecha límite: 30/11/2024"),
#             id="notificaciones",
#         ),
#         margin_left="270px",
#         padding="20px",
#         width="calc(100% - 270px)",
#         background_color="#ecf0f1",
#     )
