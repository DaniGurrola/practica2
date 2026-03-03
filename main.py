import flet as ft

def main(page: ft.Page):
    page.title = "Formulario de Registro de Eventos"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        "Registro de Eventos",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.PINK
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ej: Reunion con maestros"
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

    resumen_texto = ft.Text("", weight=ft.FontWeight.BOLD)

    fecha_evento = ft.Text("")

    lista_eventos = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True
    )

    def seleccionar_fecha(e):
        if date_picker.value:
            fecha_evento.value = date_picker.value.strftime('%d/%m/%Y')
            page.update()

    date_picker = ft.DatePicker(
        on_change=seleccionar_fecha
    )

    page.overlay.append(date_picker)

    def abrir_calendario(e):
        date_picker.open = True
        page.update()

    boton_fecha = ft.Button(
        "Seleccionar fecha",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=abrir_calendario
    )

    def guardar_evento(e):
        if nombre_evento.value.strip() == "":
            resumen_texto.value = "Error: El nombre del evento no puede estar vacío!!!!."
            resumen_texto.color = ft.Colors.RED
        else:
            resumen_texto.value = ""

            nuevo_evento = ft.Container(
                content=ft.Text(
                    f"{nombre_evento.value} | "
                    f"{tipo_evento.value} | "
                    f"{modalidad.value} | "
                    f"{'Sí' if inscripcion.value else 'No'} | "
                    f"{int(duracion.value)} horas | "
                    f"{fecha_evento.value}"
                ),
                bgcolor=ft.Colors.PINK_50,
                padding=10,
                border_radius=10
            )

            lista_eventos.controls.append(nuevo_evento)

            nombre_evento.value = ""
            fecha_evento.value = ""

        page.update()

    boton_guardar = ft.Button(
        "Guardar evento",
        on_click=guardar_evento
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
            boton_fecha,
            fecha_evento,
            boton_guardar,
            ft.Divider(),
            resumen_texto,
            ft.Text("Eventos guardados:", weight=ft.FontWeight.BOLD),
            lista_eventos
        ],
        spacing=15
    )

    page.add(formulario)

ft.app(target=main)