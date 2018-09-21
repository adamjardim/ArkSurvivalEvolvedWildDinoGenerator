import GUI as GUI
import command as command
import tkinter as tk

root = tk.Tk()
app = GUI.gui("Ark Server Code Generator", 640, 480, master=root)

testCommand = command.Command("Foo", 1, "[testCommand]")

app.addCommand(testCommand)
app.mainloop()
