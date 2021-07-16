import tkinter.scrolledtext as scrolledtext
import tkinter as tk
from tkinter import Scrollbar

window = tk.Tk()            #instantiating Tkinter, opens window
window.title("Budget Note") #what the window will be named

#reset the scroll region to encompass the inner fram
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

window.resizable(0,1)       #window resize,0=False 1=True(x,y)

window.columnconfigure(0,minsize=25)
window.rowconfigure([0,1],minsize=10)

#################
#CREATING CANVAS#
#################
frm_main=tk.Frame(window)
frm_main.grid(column=0,row=0)

frm_main.columnconfigure([0,1],weight=1)
frm_main.rowconfigure([0,1,2,3,4,5,6],minsize=10,weight=1)



#create label for topleft part of gui
lbl_top_left = tk.Label(
        frm_main,
        text="Categories",
        borderwidth = 3,
        relief = "sunken",
        width=30,
        height=10
        )
lbl_top_left.grid(
        row=0,
        column=0,
        pady=(3,0),
        sticky='nw'
        )

#left side panel
#lbl_left = tk.Label(
#        frm_main,
##        borderwidth=3,
#        relief = 'raised',
#        )
#lbl_left.grid(row=1,
#        column=0,
#        sticky='nsew',
#        padx=(2,0)
#        )

frm_selection = tk.Frame(
        frm_main,
        relief='groove')
frm_selection.grid(
        row=1,
        column=0,
        padx=(2,0),
        rowspan=6
        )

frm_selection.columnconfigure(0,weight=1)

lbl_selection=tk.Label(
        frm_selection,
        borderwidth=3,
        relief='groove'
        )
lbl_selection.grid(
        row=0,
        column=0,
        rowspan=6,
        sticky='nsew'
        )


#TODO:
# - figure out how to size frame to stay same size
# - need to research to find out if I need to make the entire program nested into a canvas

cnv_1 = tk.Canvas(frm_main)
cnv_1.grid(column=1,row=0,sticky='nsew',rowspan=6)

#adding scrollbar to frame_workspace
frame_workspace=tk.Frame(cnv_1)
frame_workspace.grid(column=0,row=0)
frame_workspace_scrollbar=Scrollbar(cnv_1)
frame_workspace_scrollbar.config(command=cnv_1.yview)
frame_workspace_scrollbar.grid(column=1,row=0,sticky='nse',rowspan=5)

text_boxes = [0]


#test text windows
txt_1=scrolledtext.ScrolledText(frame_workspace,undo=True)
txt_1['font']=('consolas','12')
txt_1['height']=(5)
txt_1.grid(
        column=0,
        row=0,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_2=scrolledtext.ScrolledText(frame_workspace,undo=True)
txt_2['font']=('consolas','12')
txt_2['height']=(5)
txt_2.grid(
        column=0,
        row=1,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_3=scrolledtext.ScrolledText(frame_workspace,undo=True)
txt_3['font']=('consolas','12')
txt_3['height']=(5)
txt_3.grid(
        column=0,
        row=2,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_4=scrolledtext.ScrolledText(frame_workspace,undo=True)
txt_4['font']=('consolas','12')
txt_4['height']=(5)
txt_4.grid(
        column=0,
        row=3,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_5=scrolledtext.ScrolledText(frame_workspace,undo=True)
txt_5['font']=('consolas','12')
txt_5['height']=(5)
txt_5.grid(
        column=0,
        row=4,
        pady=5,
        padx=5,
        sticky='n'
        )

cnv_1.bind("<configure>", lambda e:cnv_1.configure(scrollregion = my_canvas.bbox("all")))

#Program run until user exits
window.mainloop()
