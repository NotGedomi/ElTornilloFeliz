#IMPORTAR LIBRERIA TKINTER
import tkinter
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter import ttk
from pymongo import *
from tkinter import messagebox
lista = []

#CREACION DE VENTANA PRINCIPAL
ventana = Tk()
ventana.title("Recepción De Pedidos")
ventana.config(bg="#191919")
ventana.iconbitmap("img/ETF1.ico")
ventana.resizable(0,0)



#LOGO
logo = PhotoImage(file="img/ETF1.gif")
Label(ventana, image=logo, bg="#191919" ,bd=0).grid(column=0,row=0,columnspan=2,sticky=EW, pady=5, padx=10)

lista_de_activados = []

#####################################################################################################

#FUNCIONES
def buscar():
    if get.get() == Sierra[0]:
        tree.insert(parent='', index=0, iid=0, text='', values=(Sierra[0],Sierra[1],Sierra[2],Sierra[3],Sierra[4],Sierra[5]))
        get.set("")
        product1.focus()
        lista_de_activados.append("Sierra")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")
    elif get.get() == Alicate[0]:
        tree.insert(parent='', index=1, iid=1, text='', values=(Alicate[0],Alicate[1],Alicate[2],Alicate[3],Alicate[4],Alicate[5]))
        get.set("")
        product1.focus()
        lista_de_activados.append("Alicate")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")
    elif get.get() == Tornillo[0]:
        tree.insert(parent='', index=2, iid=2, text='', values=(Tornillo[0],Tornillo[1],Tornillo[2],Tornillo[3],Tornillo[4],Tornillo[5]))
        get.set("")
        product1.focus()
        lista_de_activados.append("Tornillo")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")
    elif get.get() == Destornillador[0]:
        tree.insert(parent='', index=3, iid=3, text='', values=(Destornillador[0],Destornillador[1],Destornillador[2],Destornillador[3],Destornillador[4],Destornillador[5]))
        get.set("")
        product1.focus()
        lista_de_activados.append("Destornillador")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")            
    else:
        #MENSAJE ID NO ENCONTRADO
        messagebox.showinfo("Aviso","Producto no encontrado, verifique la lista de ID")
        get.set("")
        product1.focus()
    print(lista_de_activados)

#FUNCIONES DE IMPRESION DE ARCHIVO
 
def iniciarArchivo():
    archivo = open("file.txt","a")
    archivo.close()
    
def imprimir():
    namep = getname.get()
    lastnamep = getlastname.get()
    addressp = getaddress.get()
    dnip = getdni.get()
    phonep = getphone.get()
    lista.append("-----------------------------NUEVO CLIENTE-------------------------------------------")
    lista.append("Nombre:"+namep+" / "+"Apellidos:"+lastnamep+" / "+"DNI:"+dnip+" / "+"Direccion:"+addressp+" / "+"Telefono:"+phonep)
    lista.append("------------------------INFORMACION DEL PRODUCTO-------------------------------------")
    contador = 0
    if "Sierra" in lista_de_activados:
        lista.append(f"Herramienta : {Sierra[1]}\nCantidad : {Sierra[3]} \nPrecio : S/.{Sierra[5]}\n")
        contador+=Sierra[5]
        #Sierra = ["01","Sierra","1","1",50,50]
    if "Alicate" in lista_de_activados:
        lista.append(f"Herramienta : {Alicate[1]}\nCantidad : {Alicate[3]} \nPrecio : S/.{Alicate[5]}\n")
        contador+=Alicate[5]
    if "Tornillo" in lista_de_activados:
        lista.append(f"Herramienta : {Tornillo[1]}\nCantidad : {Tornillo[3]} \nPrecio : S/.{Tornillo[5]}\n")
        contador+=Tornillo[5]
    if "Destornillador" in lista_de_activados:
        lista.append(f"Herramienta : {Destornillador[1]}\nCantidad : {Destornillador[3]} \nPrecio : S/.{Destornillador[5]}\n")
        contador+=Destornillador[5]
    lista.append(f"Total a pagar : S/.{contador}")
    
    escribirBoleta()
    messagebox.showinfo("información","El boleta de venta ha sido guardada")
    getname.set("")
    getlastname.set("")
    getaddress.set("")
    getdni.set("")
    getphone.set("")

#ARCHIVO TXT    
def escribirBoleta():
    archivo = open("Boleta.txt","w")
    # lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()
    
###########################################################################################    


#CONTENEDOR PRINCIPAL
contenedor1= Frame(ventana)
contenedor1.config(bg="#191919")
contenedor1.grid(column=0,row=1,sticky=NSEW,padx=(20,20),pady=(10,10))
contenedor1.columnconfigure(0,weight=1)
contenedor1.columnconfigure(0,weight=1)

def is_valid_text(text):
    return text in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ  "
validatecommand = contenedor1.register(is_valid_text)


#DESCRIPCIÓN
dcn=Label(contenedor1, text="FERRETERÍA EL TORNILLO FELIZ")
dcn.config(bg="#191919", font=("Impact",18), fg="white")
dcn.grid(column=1,row=1, columnspan=5,sticky=NSEW, pady=10)

#DNI
dni=Label(contenedor1, text="DNI")
dni.config(bg="#191919", font=("Arial Black",8), fg="#ebc121")
dni.grid(column=1,row=2,sticky=NSEW,pady=10,padx=10)


#ENTRY DNI SOLO 8 DIGITOS
def is_valid_date(action, char, text):
    # Solo chequear cuando se añade un carácter.
    if action != "1":
        return True
    return char in "0123456789" and len(text) < 8

validatecommand = contenedor1.register(is_valid_date)

getdni = StringVar()
dni1=Entry(contenedor1,textvariable=getdni, fg="#191919", bg="#ebc121",validate="key",validatecommand=(validatecommand, "%d", "%S", "%s"))
dni1.grid(column=2,row=2,sticky=NSEW,pady=10,padx=10)

#NOMBRE
name=Label(contenedor1, text="NOMBRES")
name.config(bg="#191919", font=("Arial Black",8), fg="#ebc121")
name.grid(column=1,row=3,sticky=NSEW,pady=10,padx=10)


def is_valid_text(text):
    return text in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ  "
validatecommand = contenedor1.register(is_valid_text)

#ENTRY NOMBRE SOLO TEXTO
getname = StringVar()
name1=Entry(contenedor1,textvariable=getname,fg="#191919", bg="#ebc121",validate="key", validatecommand=(validatecommand, "%S"))
name1.grid(column=2,row=3,sticky=NSEW,pady=10,padx=10)

#APELLIDOS
lastname=Label(contenedor1, text="APELLIDOS")
lastname.config(bg="#191919", font=("Arial Black",8), fg="#ebc121")
lastname.grid(column=4,row=3,sticky=NSEW,pady=10,padx=10)

#APELLIDOS ENTRY
getlastname = StringVar()
lastname1=Entry(contenedor1,textvariable=getlastname,fg="#191919", bg="#ebc121",validate="key", validatecommand=(validatecommand, "%S"))
lastname1.grid(column=5,row=3,sticky=NSEW,pady=10,padx=10)

#DIRECCION
address=Label(contenedor1, text="DIRECCIÓN DE DOMICILIO")
address.config(bg="#191919", font=("Arial Black",8), fg="#ebc121")
address.grid(column=1,row=4,sticky=NSEW,pady=10,padx=10)

#DIRECCION ENTRY
getaddress = StringVar()
address1=Entry(contenedor1,textvariable=getaddress,fg="#191919", bg="#ebc121")
address1.grid(column=2,row=4,columnspan=4,sticky=NSEW,pady=10,padx=10)

#TELEFONO
phone=Label(contenedor1,text="TELÉFONO FIJO / CELULAR")
phone.config(bg="#191919", font=("Arial Black",8), fg="#ebc121")
phone.grid(column=1,row=5,sticky=NSEW,pady=10,padx=10)

#ENTRY TELEFONO CHECK SOLO NUMERO

def is_valid_char(char):
    return char in "0123456789" 
 
validatecommand = contenedor1.register(is_valid_char)
getphone = StringVar()
phone1=Entry(contenedor1,textvariable=getphone,fg="#191919", bg="#ebc121",validate="key", validatecommand=(validatecommand, "%S"))
phone1.grid(column=2,row=5,columnspan=2,sticky=NSEW,pady=10,padx=10)

#ID PRODUCTO
product=Label(contenedor1, text="ID DEL PRODUCTO")
product.config(bg="#191919", font=("Arial Black",8), fg="#ebc121")
product.grid(column=1,row=6,sticky=NSEW,pady=10,padx=10)

#ENTRY ID PRODUCTO
get=StringVar()
product1=Entry(contenedor1,textvariable=get,fg="#191919", bg="#ebc121")
product1.grid(column=2,row=6,sticky=NSEW,pady=10,padx=10)

#BOTON BUSCAR PRODUCTO POR ID
button=Button(contenedor1,font=("Arial Black",8),bg="#191919", fg="white",activebackground="#ebc121",activeforeground="#191919", text="AÑADIR",command=buscar).grid(column=3,row=6,sticky=NSEW,padx=10, pady=10)



#VIEWTREE
style = ttk.Style()
style.configure("Treeview",
                background="#ebc121",
                foreground="#191919",
                rowheight=25,
                fieldbackground="#191919")
style.map('Treeview', background=[('selected', '#ffd01c')])

tree = ttk.Treeview(ventana)
tree['columns']=('cod_pro', 'Description', 'Unidad','Cantidad','Precio','SubTotal')
tree.column('#0', width=0, stretch=NO)
tree.column('cod_pro', anchor=CENTER)
tree.column('Description', anchor=CENTER)
tree.column('Unidad', anchor=CENTER)
tree.column('Cantidad', anchor=CENTER)
tree.column('Precio', anchor=CENTER)
tree.column('SubTotal', anchor=CENTER)


#CREACIÓN DE HEADING
tree.heading('#0', text='', anchor=CENTER)
tree.heading('cod_pro', text='Cod_Pro', anchor=CENTER)
tree.heading('Description', text='Description', anchor=CENTER)
tree.heading('Unidad', text='Unidad', anchor=CENTER)
tree.heading('Cantidad', text='Cantidad', anchor=CENTER)
tree.heading('Precio', text='Precio', anchor=CENTER)
tree.heading('SubTotal', text='SubTotal', anchor=CENTER)
tree.grid(column=0,row=7,columnspan=2,sticky=EW, pady=5, padx=10)


          
#PRODUCTOS
Sierra = ["ETF01","Sierra","1","1",55,55]
Alicate = ["ETF02","Alicate","1","1",23,23]
Tornillo = ["ETF03","Tornillo","1","1",1,1]
Destornillador = ["ETF04","Destornillador","1","1",7,7]
 
 #BOTON IMPRIMIR
printbutton=Button(ventana, text="BOLETA",font=("Arial Black",8),bg="#ebc121", fg="#191919",activebackground="#191919",activeforeground="white",command=imprimir).grid(column=0,row=8,columnspan=2,sticky=NSEW, padx=10,pady=10)

ventana.mainloop()

