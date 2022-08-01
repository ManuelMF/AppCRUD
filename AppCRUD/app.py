from tkinter import *
import sqlite3
from tkinter import messagebox

# CONTROLADOR
#---------------------------------------------------------------- 

def salir():
	respuesta=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
	if respuesta==True:
		quit()

def borrar():
	EntryId.delete(0, "end")
	EntryNombre.delete(0, "end")
	EntryPassword.delete(0, "end")
	EntryApellido.delete(0, "end")
	EntryDireccion.delete(0, "end")
	TextComentario.delete("1.0", "end")

def crearUsuario():
	if nombre.get()!="" and contra.get()!="":
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		#miCursor.execute("INSERT INTO datosUsuarios VALUES(NULL,'"+nombre.get()+"','"+contra.get()+"','"+apellido.get()+"','"+direccion.get()+"','"+TextComentario.get("1.0", "end")+"')")
		#Forma menos engorrosa de hacerlo y mas segura
		datos=nombre.get(),contra.get(),apellido.get(),direccion.get(),TextComentario.get("1.0", "end")
		miCursor.execute("INSERT INTO datosUsuarios VALUES(NULL,?,?,?,?,?)",datos)

		miConexion.commit()
		messagebox.showinfo("Base de datos", "Registro insertado con exito")
		borrar()
		miConexion.close()

def cargarUsuario():
	if miId.get()!="":
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()
		try:
			miCursor.execute("SELECT * FROM datosUsuarios WHERE dat_coddad = '"+miId.get()+"'")
			usuario=miCursor.fetchall()
			nombre.set(usuario[0][1])
			contra.set(usuario[0][2])
			apellido.set(usuario[0][3])
			direccion.set(usuario[0][4])
			TextComentario.delete("1.0", "end")
			TextComentario.insert(1.0, usuario[0][5])
		except IndexError:
			messagebox.showwarning("Cargar usuario", "No hay ningun usuario con ese id")

def updateUsuario():
	if miId.get()!="":
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		#miCursor.execute("update datosUsuarios set dat_nombre='"+nombre.get()+"',dat_password='"+contra.get()+"', dat_apellido='"+apellido.get()+"', dat_direccion='"+direccion.get()+"', dat_comentarios='"+TextComentario.get("1.0", "end")+"' where dat_coddad = '"+miId.get()+"'")
	 	#Forma menos engorrosa de hacerlo y mas segura
		datos=nombre.get(),contra.get(),apellido.get(),direccion.get(),TextComentario.get("1.0", "end"),miId.get()
		miCursor.execute("update datosUsuarios set dat_nombre=?,dat_password=?, dat_apellido=?, dat_direccion=?, dat_comentarios=? where dat_coddad =?",(datos))

		miConexion.commit()
		messagebox.showinfo("Base de datos", "Registro actualizado con exito")
		borrar()
		miConexion.close()

def deleteUsuario():
	if miId.get()!="":
		miConexion=sqlite3.connect("Usuarios")
		miCursor=miConexion.cursor()

		miCursor.execute("delete from datosUsuarios where dat_coddad='"+miId.get()+"'")

		messagebox.showinfo("Base de datos", "Registro borrado con exito")
		borrar()
		miConexion.commit()
		miConexion.close()

#----------------------------------------------------------------

# MODELO
#----------------------------------------------------------------

def conectar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE datosUsuarios(
			dat_coddad Integer Primary Key autoincrement,
			dat_nombre varchar(50) not null,
			dat_password varchar(50) not null,
			dat_apellido varchar(50),
			dat_direccion varchar(50),
			dat_comentarios varchar(200)
			)		
		''')

		messagebox.showwarning("Base de datos","Se ha creado una nueva base de datos")
	except sqlite3.OperationalError:
		messagebox.showinfo("Base de datos","Se ha conectado correctamente a la base de datos")

	miConexion.commit()
	miConexion.close()

#----------------------------------------------------------------

# VISTA
#----------------------------------------------------------------
raiz=Tk()

# Variables de los Entry
miId = StringVar()
nombre = StringVar()
contra = StringVar()
apellido = StringVar()
direccion = StringVar()
comentarios = StringVar()

# Barra menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

MenuBBDD=Menu(barraMenu, tearoff=0)
MenuBBDD.add_command(label="Conectar", command=conectar)
MenuBBDD.add_command(label="Salir", command=salir)
barraMenu.add_cascade(label="BBDD", menu=MenuBBDD)

barraMenu.add_command(label="Borrar", command=borrar)

MenuCRUD=Menu(barraMenu, tearoff=0)
MenuCRUD.add_command(label="Create", command=crearUsuario)
MenuCRUD.add_command(label="Read", command=cargarUsuario)
MenuCRUD.add_command(label="Update", command=updateUsuario)
MenuCRUD.add_command(label="Delete", command=deleteUsuario)
barraMenu.add_cascade(label="CRUD", menu=MenuCRUD)

MenuAyuda=Menu(barraMenu, tearoff=0)
MenuAyuda.add_command(label="Licencia")
MenuAyuda.add_command(label="Acerca de...")
barraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)

# Botones
FramePrincipal=Frame(raiz)
FramePrincipal.pack()

lblId=Label(FramePrincipal,text="Id:")
lblId.grid(row=0,column=0, sticky="e", padx=10, pady=10)

EntryId=Entry(FramePrincipal, textvariable=miId)
EntryId.grid(row=0,column=1, padx=10, pady=10)
EntryId.config(justify="center")


lblNombre=Label(FramePrincipal,text="Nombre:")
lblNombre.grid(row=1,column=0, sticky="e", padx=10, pady=10)

EntryNombre=Entry(FramePrincipal, textvariable=nombre)
EntryNombre.grid(row=1,column=1, padx=10, pady=10)
EntryNombre.config(fg="red", justify="center")


lblPassword=Label(FramePrincipal,text="Password:")
lblPassword.grid(row=2,column=0, sticky="e", padx=10, pady=10)

EntryPassword=Entry(FramePrincipal, textvariable=contra)
EntryPassword.grid(row=2,column=1, padx=10, pady=10)
EntryPassword.config(justify="center",show="*")


lblApellido=Label(FramePrincipal,text="Apellido:")
lblApellido.grid(row=3,column=0, sticky="e", padx=10, pady=10)

EntryApellido=Entry(FramePrincipal, textvariable=apellido)
EntryApellido.grid(row=3,column=1, padx=10, pady=10)
EntryApellido.config(justify="center")


lblDireccion=Label(FramePrincipal,text="Dirección:")
lblDireccion.grid(row=4,column=0, sticky="e", padx=10, pady=10)

EntryDireccion=Entry(FramePrincipal, textvariable=direccion)
EntryDireccion.grid(row=4,column=1, padx=10, pady=10)
EntryDireccion.config(justify="center")


lblComentarios=Label(FramePrincipal,text="Comentarios:")
lblComentarios.grid(row=5,column=0, sticky="e", padx=10, pady=10)


TextComentario=Text(FramePrincipal, width=16, height=5)
TextComentario.grid(row=5,column=1, padx=10, pady=10)
scrollVert=Scrollbar(FramePrincipal, command=TextComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")
TextComentario.config(yscrollcommand=scrollVert.set)

FrameBotones=Frame(raiz)
FrameBotones.pack()

btnCreate = Button(FrameBotones,text="Create", command=crearUsuario)
btnCreate.grid(row=0,column=0, sticky="e", padx=10, pady=10)

btnRead = Button(FrameBotones,text="Read", command=cargarUsuario)
btnRead.grid(row=0,column=1, sticky="e", padx=10, pady=10)

btnUpdate = Button(FrameBotones,text="Update", command=updateUsuario)
btnUpdate.grid(row=0,column=2, sticky="e", padx=10, pady=10)

btnDelete = Button(FrameBotones,text="Delete", command=deleteUsuario)
btnDelete.grid(row=0,column=3, sticky="e", padx=10, pady=15)



raiz.mainloop()
#----------------------------------------------------------------