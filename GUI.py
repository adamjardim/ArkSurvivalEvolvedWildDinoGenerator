from command import Command
import tkinter as tk

def run(self):
	root = tk.Tk()
	app = gui("Ark Server Code Generator", 640, 480, master=root)
	app.mainloop()

class gui(tk.Frame):
	listOfCommands = []
	def __init__(self, title, width, height, master=None):
		self.title = title
		self.width = width
		self.height = height
		self.master = master
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def testNewCommand(self):
		if self.getNumCommands() == 0:
			print("No command to test")
		else:
			self.listOfCommands[0].generate()

	def addCommand(self, command):
		self.listOfCommands.append(command)
		print("Commands:")
		for c in self.listOfCommands:
			print("\t- " + c.name + ": " + c.code)

	def getNumCommands(self):
		return len(self.listOfCommands)

	def getCommandAtIndex(index):
		return listOfCommands[index]

	def create_widgets(self):
		self.importButton = tk.Button(self)
		self.importButton["text"] = "(click me)"
		self.importButton["command"] = self.testNewCommand()
		self.importButton.pack(side="top")
		self.importButton.pack(expand=1)

		self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.pack(side="bottom")
