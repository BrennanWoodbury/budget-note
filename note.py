import tkinter.scrolledtext as scrolledtext
import tkinter as tk
from tkinter import Scrollbar

window = tk.Tk()            #instantiating Tkinter, opens window
window.title("Budget Note") #what the window will be named

#window.geometry('1200x800')

window.resizable(0,1)       #window resize,0=False 1=True(x,y)

window.columnconfigure(0,minsize=25)
window.rowconfigure([0,1],minsize=10)

canvas_main=tk.Canvas(window)
canvas_main.pack()

#create label for topleft part of gui
lbl_top_left = tk.Label(
        text="Categories",
        borderwidth = 3,
        relief = "sunken",
        width=30,
        height=10
        )
lbl_top_left.grid(
        row=0,
        column=0,
        pady=(10,0)
        )

#left side panel
lbl_left = tk.Label(
#        borderwidth=3,
        relief = 'raised',
        )
lbl_left.grid(row=1,
        column=0,
        rowspan=4,
        sticky='nsew',
        padx=(2,0)
        )

#top middle to right panel
lbl_top=tk.Label(
#        borderwidth=3,
        relief = 'raised',
        width = 100,
        height = 10
        )
lbl_top.grid(column=1,row=0)

####################################################
#THIS IS THE WORkSPACE LABEL, REPLACING WITH CANVAS#
####################################################
#bulk of the program, where all the inputs will be
#lbl_workspace = tk.Label(
#        relief='flat',
#        width=100,
#        height=30,
#        )
#lbl_workspace.grid(column=1, row=1,sticky='nsew')
##adding scrollbar to workspace
#workspace_scrollbar = Scrollbar(lbl_workspace)
#workspace_scrollbar.config(command=lbl_workspace.yview)
#workspace_scrollbar.pack(side='left')
#

#############
#BEGIN CAVAS#
#############
#TODO:
# - figure out how to size frame to stay same size
# - need to research to find out if I need to make the entire program nested into a canvas
cnv_1 = tk.Canvas(window,width=100,height=30)
cnv_1.grid(column=1,row=1,sticky='nsew')

#adding scrollbar to frame_workspace
frame_workspace=tk.Frame(cnv_1)
frame_workspace_scrollbar=Scrollbar(cnv_1)
frame_workspace_scrollbar.config(command=cnv_1.yview)
frame_workspace_scrollbar.grid(column=1,row=0,sticky='nse',rowspan=5)

#test text windows
txt_1=scrolledtext.ScrolledText(cnv_1,undo=True)
txt_1['font']=('consolas','12')
txt_1['height']=(5)
txt_1.grid(
        column=0,
        row=0,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_2=scrolledtext.ScrolledText(cnv_1,undo=True)
txt_2['font']=('consolas','12')
txt_2['height']=(5)
txt_2.grid(
        column=0,
        row=1,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_3=scrolledtext.ScrolledText(cnv_1,undo=True)
txt_3['font']=('consolas','12')
txt_3['height']=(5)
txt_3.grid(
        column=0,
        row=2,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_4=scrolledtext.ScrolledText(cnv_1,undo=True)
txt_4['font']=('consolas','12')
txt_4['height']=(5)
txt_4.grid(
        column=0,
        row=3,
        pady=5,
        padx=5,
        sticky='n'
        )

txt_5=scrolledtext.ScrolledText(cnv_1,undo=True)
txt_5['font']=('consolas','12')
txt_5['height']=(5)
txt_5.grid(
        column=0,
        row=4,
        pady=5,
        padx=5,
        sticky='n'
        )

#Program run until user exits
window.mainloop()
