# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
# https://realpython.com/python-lambda/
# https://docs.python.org/3/tutorial/inputoutput.html
# https://www.tutorialspoint.com/pygtk/pygtk_treeview_class.htm

import gi
import threading
import sys
import subprocess
proc = subprocess.Popen([sys.argv[1]],stdout=subprocess.PIPE, stdin=subprocess.PIPE)


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def onQuit(arg):
    proc.stdin.write("QUIT 0\n".encode())
    proc.stdin.flush()
    Gtk.main_quit()

win = Gtk.Window()
win.connect("destroy", onQuit)

def onButtonClicked(arg):
    proc.stdin.write("onInput 1\n".encode())
    proc.stdin.write((textField.get_text() + "\n").encode())
    proc.stdin.flush()

def onItemSelected(widget, row, col):
    item = widget.get_model()[row][0]
    proc.stdin.write("onItemSelected 1\n".encode())
    proc.stdin.write((item + "\n").encode())
    proc.stdin.flush()

# Add the UI
layout = Gtk.Box(spacing = 7, orientation = Gtk.Orientation.VERTICAL)
win.add(layout)

inputLayout = Gtk.Box(spacing = 7)
layout.add(inputLayout)

textField = Gtk.Entry()
inputLayout.add(textField)

button = Gtk.Button(label = "+ Add")
button.connect("clicked", onButtonClicked)
button.set_can_default(True)
button.grab_default()
inputLayout.add(button)

store = Gtk.ListStore(str)

tree = Gtk.TreeView(model=store)
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
   while proc.poll() is None:
      event = proc.stdout.readline().decode().rstrip("\n")
      print(event, file=sys.stderr)
      if event == "addItem 1":
      	store.append([proc.stdout.readline().decode().rstrip("\n")])
      if event == "changeButtonText 1":
      	button.set_label(proc.stdout.readline().decode())
      if event == "changeTitle 1":
      	win.set_title(proc.stdout.readline().decode())
      if event == "QUIT 0":
      	Gtk.main_quit()
threading.Thread(target = check_input).start()

# Start the app
proc.stdin.write("START 0\n".encode())
proc.stdin.flush()

win.show_all()
Gtk.main()
