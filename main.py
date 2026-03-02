import flet as ft

def main(page: ft.Page):
    page.title = "Formulario de Registro de Eventos"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO 

    titulo = ft.Text(
        value="Registro de Eventos",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ej: Jornada Tecnológica 2026"
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )

    resumen_texto = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREEN
    )

    def mostrar_resumen(e):
        if nombre_evento.value.strip() == "":
            resumen_texto.value = "⚠️ Error: El nombre del evento no puede estar vacío."
            resumen_texto.color = ft.Colors.RED
        else:
            resumen_texto.color = ft.Colors.GREEN
            resumen_texto.value = f"""
Resumen del Evento:
Nombre: {nombre_evento.value}
Tipo: {tipo_evento.value}
Modalidad: {modalidad.value}
Requiere inscripción: {"Sí" if inscripcion.value else "No"}
Duración: {int(duracion.value)} horas
"""
        page.update()  

    boton = ft.ElevatedButton(
        "Mostrar resumen",
        on_click=mostrar_resumen,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    formulario = ft.Column(
        controls=[
            titulo,
            nombre_evento,
            tipo_evento,
            ft.Text("Modalidad:", weight=ft.FontWeight.BOLD),
            modalidad,
            inscripcion,
            ft.Text("Duración estimada (horas):", weight=ft.FontWeight.BOLD),
            duracion,
            boton,
            ft.Divider(thickness=2),
            resumen_texto  
        ],
        spacing=15
    )

    page.add(formulario)

ft.run(main)