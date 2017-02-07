from VideoConverter import *
from Tkinter import *
import tkFileDialog

class VcApp:
  def __init__(self, root):
    self.root = root
    root.title('VcApp')

    self.frames()
    self.components()

  def frames(self):
    self.header = LabelFrame(self.root, text="VcApp v0.1", font=("Magneto", 8), relief=SUNKEN, borderwidth=2,
                             bg="#2D8BC9")
    self.header.grid(padx=5, pady=5)
    self.input = LabelFrame(self.root, text="Select or enter input file directory.", font=("Magneto", 8), relief=SUNKEN, borderwidth=2,
                             bg="#2D8BC9")
    self.input.grid(sticky=W+E+N+S,padx=5)
    self.output = LabelFrame(self.root, text="Select or enter output file directory.", font=("Magneto", 8), relief=SUNKEN,
                            borderwidth=2,
                            bg="#2D8BC9")
    self.output.grid(sticky=W+E+N+S,padx=5)
    self.format = LabelFrame(self.root, text="Select output format.", font=("Magneto", 8),
                             relief=SUNKEN,
                             borderwidth=2,
                             bg="#2D8BC9")
    self.format.grid(sticky=W+E+N+S,padx=5)

  def components(self):
    self.file_input = Entry(self.input)
    self.file_input.grid(row=1, padx=5)
    self.file_input_button = Button(self.input, text='Select input file', command=self.selectFile, bg="#80b929")
    self.file_input_button.grid(row=1, column=2, padx=5, pady=5)

    self.file_output = Entry(self.output)
    self.file_output.grid(row=2, padx=5, pady=5)
    self.file_output_button = Button(self.output, text='File output', command=self.outputFile)
    self.file_output_button.grid(row=2, column=2, padx=5, pady=5)

    self.format_selection = StringVar(self.root)
    self.format_selection.set('iphone')
    self.file_format = OptionMenu(self.format, self.format_selection, 'iphone', 'imac', 'mackbook')
    self.file_format.grid(row=5, padx=5, pady=5)
    self.frames_label = Label(self.format, text='FPS:')
    self.frames_label.grid(row=5, column=2)
    self.frames_input = Entry(self.format, width=10)
    self.frames_input.insert(0,'30')
    self.frames_input.grid(row=5, column=3, padx=5)

    self.action_button = Button(self.root, text='Generate Gif', command=self.generateGif, bg="#80b929")
    self.action_button.grid(row=6, sticky=W+E+N+S,padx=5)

  def generateGif(self):
    vc = VideoConverter(fps=self.frames_input.get())
    vc.input_file_name(self.file_input.get())
    vc.output_file_name(self.file_output.get())
    vc.output_format(self.format_selection.get())
    vc.generate_gif()

  def selectFile(self):
    self.file_input.insert(0, tkFileDialog.askopenfilename())

  def outputFile(self):
    self.file_output.insert(0,tkFileDialog.asksaveasfilename(defaultextension=".gif"))

root = Tk()
file_ex = VcApp(root)
root.configure(bg="#2D8BC9")
root.resizable(0,0)
root.mainloop()