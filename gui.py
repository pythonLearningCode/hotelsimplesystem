from tkinter import *
import classes

# GLOBAL VARIABLES


#  CREATING THE MAIN WINDOW AND DEFINING TITLE AND GEOMETRY
main = Tk()
main.title("Sistema de Reservas")
main.geometry("800x600+200+50")


#  CREATING THE SECTION FOR RESERVATION CONTROL
reservation_control = LabelFrame(main, text='Controle de Reservas', labelanchor='n')




# CREATING THE SCROLLBAR FOR VISUALIZATION

res_scrollbar = Scrollbar(reservation_control)
res_scrollbar.pack(side='left', fill='y')

# CREATING AND USING THE CANVAS FOR THE SCROLLBAR
canvas = Canvas(reservation_control, yscrollcommand= res_scrollbar.set)
res_scrollbar.config(command = canvas.yview)


#  CREATING A FRAME THAT IS AN INTERFACE BETWEEN THE SCROLLBAR CANVAS AND THE LISTS
interface_frame = Frame(canvas)


#  CREATING THE IDS FRAME, WHILE CALLING THE CLASSES FUNCTION FOR GETTING THE INFO FROM THE DB
ids = LabelFrame(interface_frame, text='ids')
ids_list = classes.show_ids()
for index, idd in enumerate(ids_list):
    ids_list[index] = Label(ids, text=id)
    ids_list[index].pack()
ids.pack(side='left', fill='both', expand='true')

#  CREATING THE NAME FRAME, WHILE CALLING THE CLASSES FUNCTION FOR GETTING THE INFO FROM THE DB
name_frame = LabelFrame(interface_frame, text='Nome')
names_list = classes.show_names()
for index, name in enumerate(names_list):
    names_list[index] = Label(name_frame, text=name)
    names_list[index].pack()
name_frame.pack(side='left', fill='both', expand='true')


#  CREATING THE DATE FRAME, WHILE CALLING THE CLASSES FUNCTION FOR GETTING THE INFO FROM THE DB
date_frame = LabelFrame(interface_frame, text='Data')
dates_list = classes.show_resdates()
for index, date in enumerate(dates_list):
    dates_list[index] = Label(date_frame, text=date)
    dates_list[index].pack()
date_frame.pack(side='left', fill='both', expand='true')


#  CREATING THE REGISTRY FRAME, WHILE CALLING THE CLASSES FUNCTION FOR GETTING THE INFO FROM THE DB
registry_frame = LabelFrame(interface_frame, text='RG')
registrys_list = classes.show_registrys()
for index, registry in enumerate(registrys_list):
    registrys_list[index] = Label(registry_frame, text=registry)
    registrys_list[index].pack()
registry_frame.pack(side='left', fill='both', expand='true')


#  CREATING THE ROOM FRAME, WHILE CALLING THE CLASSES FUNCTION FOR GETTING THE INFO FROM THE DB
room_frame = LabelFrame(interface_frame, text='Quarto')
rooms_list = classes.show_rooms()
for index, room in enumerate(rooms_list):
    rooms_list[index] = Label(room_frame, text=room)
    rooms_list[index].pack()
room_frame.pack(side='left', fill='both', expand='true')


#  PACKING THE INTERFACE FRAME
interface_frame.pack(fill='both', expand='true', side='left')

#  PACKING THE CANVAS CONTAINER
canvas.pack(fill='both', expand='true', side='left')

#  PACKING THE RESERVATION CONTROL SECTION
reservation_control.pack(fill='both',expand='true', side='left')


#  CREATING THE NEW RESERVATION SECTION
new_reservation = LabelFrame(main, text='Nova Reserva', labelanchor='n')

# CREATING THE FUNCTION THAT INSERT A NEW RESERVATION
def save_reservation():
    label = []
    #  GETTING THE ITENS FROM THE ENTRIES
    save_name = nameentry.get()
    save_date = dateentry.get()
    save_identity = identityentry.get()
    save_room = roomentry.get()

    label.append(save_name)
    label.append(save_date)
    label.append(save_identity)
    label.append(save_room)

    #  CREATING THE OBJECT FOR THE CLIENT
    name_obj = classes.Clients(save_name, save_identity)
    name_obj.make_reservation(save_date, save_room)

    # SHOWING THE RESERVATION IMMEDIATELLY
    names_list[len(names_list)-1] = Label(name_frame, text=save_name)
    dates_list[len(dates_list) - 1] = Label(date_frame, text=save_date)
    registrys_list[len(registrys_list) - 1] = Label(registry_frame, text=save_identity)
    rooms_list[len(rooms_list) - 1] = Label(room_frame, text=save_room)

    names_list[len(names_list)-1].pack()
    dates_list[len(dates_list) - 1].pack()
    registrys_list[len(registrys_list) - 1].pack()
    rooms_list[len(rooms_list) - 1].pack()


#  CREATING THE NAME ENTRY FOR RESERVATION
nameframe = LabelFrame(new_reservation, text='Nome')
nameentry = Entry(nameframe)
nameentry.pack()
nameframe.pack( anchor='nw')


#  CREATING THE DATE ENTRY FOR RESERVATION
dateframe = LabelFrame(new_reservation, text='Data')
dateentry = Entry(dateframe)
dateentry.pack()
dateframe.pack( anchor='ne')


#  CREATING THE IDENTITY ENTRY FOR RESERVATION
identityframe = LabelFrame(new_reservation, text='Identidade')
identityentry = Entry(identityframe)
identityentry.pack()
identityframe.pack(anchor='sw')


#  CREATING THE ROOM ENTRY FOR RESERVATION
roomframe = LabelFrame(new_reservation, text='Quarto')
roomentry = Entry(roomframe)
roomentry.pack()
roomframe.pack(anchor='se')


# CREATING THE BUTTON FOR SAVING THE RESERVATION
savebutton = Button(new_reservation, text='SALVAR RESERVA', command=save_reservation)
savebutton.pack()


#  PACKING THE NEW RESERVATION SECTION
new_reservation.pack(fill='both', expand='true', anchor='nw')


#  CREATING THE DEL RESERVATION SECTION
del_reservation = LabelFrame(main, text='Apagar Reserva', labelanchor='n')

#  CREATING THE FUNCTION THAT DEL A RESERVATION
def delete_reservation():
    global names_list, dates_list, registrys_list, rooms_list


    to_del = id_del.get()
    to_del_int = int(to_del)
    classes.rm_line(to_del)

#  FORGETING THE ITENS SHOWN AT THE RESERVATION CONTROL
    names_list[to_del_int].destroy()
    dates_list[to_del_int].destroy()
    registrys_list[to_del_int].destroy()
    rooms_list[to_del_int].destroy()


#  CREATING THE ID ENTRY TO IDENTIFY THE ITEM FOR DEL RESERVATION
id_del = Entry(del_reservation)
id_del.pack()


#  CREATING THE BUTTON THAT DELS ONE RESERVATION
button_del = Button(del_reservation, text='APAGAR RESERVA', command=delete_reservation)
button_del.pack()


#  PACKING THE DEL RESERVATION SECTION
del_reservation.pack(fill='both', expand='true', anchor='sw')


#  CREATING THE MAINLOOP FOR THE APP
main.mainloop()

