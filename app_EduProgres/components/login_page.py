import reflex as rx

def login_page():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Iniciar Sesión", size="8", color="blue"),
                rx.input(placeholder="Usuario o correo electronico",size="3",width="75%"),
                rx.input(placeholder="Contraseña", type_="password",size="3",width="75%"),
                rx.button(
                    "Iniciar sesion", 
                    color_scheme="blue",
                    size="3", 
                    width="75%",
                    on_click=lambda: rx.redirect("/main",),
                    
                ),
                rx.text("¿Olvidaste tu contraseña?",href="/#", color="blue", size="1", cursor="pointer"),
                rx.link("¿No tienes una cuenta? Regístrate aquí", href="/register_page"),
                #spacing="4",
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            width="510px",
            height="400px",
            padding="50px",
            background="white",
            #border_radius="40px",
            box_shadow="0px 4px 10px rgba(0, 0, 0, 0.25)",
        ),
        background="gray.100",
        height="100vh",
        background_image="url('https://st.depositphotos.com/1001564/2470/i/450/depositphotos_24704059-stock-photo-background.jpg')",
        background_size="cover",
        background_position="center",
    )
