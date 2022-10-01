#!/usr/bin/env python3

# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
# https://realpython.com/python-lambda/
# https://docs.python.org/3/tutorial/inputoutput.html
# https://www.tutorialspoint.com/pygtk/pygtk_treeview_class.htm

import gi
import threading
import sys
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def onQuit(arg):
    sys.stdout.write("QUIT 0\n")
    sys.stdout.flush()
    Gtk.main_quit()

win = Gtk.Window()
win.set_default_size(400, 300)
win.connect("destroy", onQuit)

def onButtonClicked(arg):
    sys.stdout.write("onInput 1\n")
    sys.stdout.write(textField.get_text() + "\n")
    sys.stdout.flush()

def onItemSelected(widget, row, col):
    item = widget.get_model()[row][0]
    sys.stdout.write("onItemSelected 1\n")
    sys.stdout.write((item + "\n"))
    sys.stdout.flush()

# Add the UI
layout = Gtk.Box(spacing = 7, orientation = Gtk.Orientation.VERTICAL)
win.add(layout)

inputLayout = Gtk.Box(spacing = 7)
inputLayout.set_hexpand(True)
layout.add(inputLayout)

textField = Gtk.Entry()
textField.set_hexpand(True)
inputLayout.add(textField)

button = Gtk.Button(label = "+ Add")
button.connect("clicked", onButtonClicked)
button.set_can_default(True)
button.grab_default()
inputLayout.add(button)

store = Gtk.ListStore(str)

tree = Gtk.TreeView(model=store)
tree.set_vexpand(True)
renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("List", renderer, text=0, weight=1)
tree.append_column(column)
tree.connect("row-activated", onItemSelected)

scrolledWindow = Gtk.ScrolledWindow()
scrolledWindow.add(tree)

layout.add(scrolledWindow)

# Read input; connects the UI to the logic process
counter = 0

def check_input():
   # While process is alive ...
   while True:
      event = input()
      print(event, file=sys.stderr)
      if event == "addItem 1":
      	store.append([input()])
      if event == "changeButtonText 1":
      	button.set_label(input())
      if event == "changeTitle 1":
      	win.set_title(input())
      if event == "QUIT 0":
      	Gtk.main_quit()
      	exit()
threading.Thread(target = check_input).start()

# Start the app
sys.stdout.write("START 0\n")
sys.stdout.flush()

win.show_all()
Gtk.main()
