



from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk,messagebox
import gui18, gui20,metodos

# limpia el frame para poder actualizar la ventana
def titulo(frame5):
    # Limpia el frame
    for item in frame5.winfo_children():
        item.destroy()

#creacion de todos los elementos de la ventana y acceso a ruta completa     
def cliente_ver_estado(frame5):
    global button_image_1, button_image_2, button_image_3, button_image_4,button_image_5,entry_image_1,entry_image_2,image_image_1
    
    # Limpia el frame
    titulo(frame5)
    
    #verifica directorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame19"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    #lectura de frame
    canvas = Canvas(
        frame5,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    #imagen
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        93.0,
        300.0,
        image=image_image_1
    )

    #texto
    canvas.create_text(
        400.0,
        24.0,
        anchor="nw",
        text="Ver estado del pedido",
        fill="#000000",
        font=("MicrosoftSansSerif", 32 * -1)
    )

    #texto
    canvas.create_text(
        250.0,
        111.0,
        anchor="nw",
        text="Ingrese el ID del cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #! funcion que verifica los pedidos del cliente y los enlista
    def pedidos():
        identificador = entry_1.get()
        if identificador in metodos.sistema.clientes:
            cliente=metodos.sistema.clientes[identificador]
            if cliente.envios:
                cli=[]
                for envio in cliente.envios:
                    cli.append(metodos.sistema.obtener_info_job(envio.id_job))
            else:
                messagebox.showinfo(title=None, message="no tiene pedidos registrados")
        else:
            messagebox.showwarning(title=None, message="cliente no encontrado")
        global combo
        combo = ttk.Combobox(frame5,state="readonly", values=cli)
        combo.place(x=556.0, y=175.0)
    
    
    #?boton que busca los pedidos del cliente
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        frame5,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: pedidos(),
        relief="flat"
    )#Boton para buscar el envio con el ID especificado
    button_5.place(
        x=729.0,
        y=101.0,
        width=50.0,
        height=45.0
    )
    
    
    #texto
    canvas.create_text(
        250.0,
        171.0,
        anchor="nw",
        text="Ingrese el ID del envío a ver:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        631.0,
        125.5,
        image=entry_image_1
    )#Cuadro donde se ingresa ID del envio a ver
    entry_1 = Entry(
        frame5,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=564.0,
        y=108.0,
        width=134.0,
        height=33.0
    )

    #!buscar estado envio
    def bus_estado_pedido():
        id_job = combo.get()
        if id_job in metodos.sistema.envios:
            canvas.itemconfig(estado, text=metodos.sistema.obtener_estado_job(id_job))
        else:
            messagebox.showwarning(title=None, message=f'No se ha encontrado ningún envío con el {id_job}')
            
            
    
    #?boton que busca estado del envio
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame5,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: bus_estado_pedido(),
        relief="flat"
    )#Boton para buscar el envio con el ID especificado
    button_1.place(
        x=729.0,
        y=163.0,
        width=50.0,
        height=45.0
    )

    canvas.create_text(
        250.0,
        231.0,
        anchor="nw",
        text="estado del envio:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        631.0,
        241.5,
        image=entry_image_1
    )
    
    estado=canvas.create_text(
        631.0,
        241.0,
        anchor="center",
        text=" ",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame5,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui18.cliente_ver_pedido(frame5),
        relief="flat"
    )#Boton funcionalidad
    button_2.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame5,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Ya estas aca"),
        relief="flat"
    )#Boton funcionalidad que se esta usando
    button_3.place(
        x=14.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame5,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui20.cliente_ver_historial(frame5),
        relief="flat"
    )#Boton funcionalidad
    button_4.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    