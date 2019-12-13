from tkinter import *
# from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
"""This code creates a canvas, pen, eraser, and thickness slider along with colors and instructions in order for the user to draw. It 
can be used to draw and get creative. You can just run it and close the window once you are done with the program. A very simple version of
MS Paint in homage to JigglyPuff, the Pokemon"""
"""ON TESTING: We created a skeleton for our GUI and tested as we kept adding, 
so this code has been progressively been tampered with. There are no actual calls or test files, but in the # comments,
you can see how we tested some parts. We used trial and error for the grid placement of buttons"""
class Paint(object):

   DEFAULT_PEN_SIZE = 5.0 #these two lines set the default color and thickness, so the user can get started
   DEFAULT_COLOR = 'black'

   def __init__(self):
      #This sets up our base for our game: Canvas, buttons, instructions, etc
       self.root = Tk()
       self.root.title("JigglyPuff's Drawing Palace")

       self.Title = Label(self.root, text = "JigglyPuff's Drawing Palace", font = "Arial 20 bold" , justify = CENTER,
                          bd = 2, relief = RAISED)
       self.Title.grid(row = 0, column = 5)                 #this creates the title label

       self.pen_button = Button(self.root, text='brush', command=self.use_pen)
       self.pen_button.grid(row=0, column=1)

       self.actualInstr = Label(self.root, text= " Instructons: \n Welcome to JigglyPuff's Drawing Palace! \n * Use the mouse to draw on the canvas.\n "
                                                 "* If you make a mistake, use the eraser button. \n * Click on the color icon to change the color of the pen."
                                                 "\n * If you want to change the thickness of your pen, move the slider.\n Let's get creating!", relief = RIDGE,
                                font = "Arial 18", bd= 2, justify = LEFT, height = 8)
       self.actualInstr.grid (rowspan = 2, row = 0, column = 6 )
      
       #from here to line 48 are the color buttons that assign a color to the pen, paired with callbacks that will activate them
         
       self.redLabel = Button(self.root, text = "Red", font = "Arial 12", fg = "red", justify = CENTER, command = self.redCallback)
       self.redLabel.grid(rowspan = 3, row = 5, column = 1, columnspan = 1)

       self.blueLabel = Button(self.root, text = "Blue", font = "Arial 12", fg = "blue", justify = CENTER, command = self.blueCallback)
       self.blueLabel.grid(rowspan = 3, row = 5, column = 2, columnspan =1)

       self.greenLabel = Button(self.root, text = "Green", font = "Arial 12", fg = "green", justify = CENTER, command = self.greenCallback)
       self.greenLabel.grid(rowspan = 3, row = 5, column = 3, columnspan = 1)

       self.yellowLabel = Button(self.root, text = "Yellow", font = "Arial 12", fg = "gold", justify = CENTER, command = self.yellowCallback)
       self.yellowLabel.grid(rowspan = 3, row = 5, column = 4, columnspan = 1)

       self.blackLabel = Button(self.root, text = "Black", font = "Arial 12", fg = "black", justify = CENTER, command = self.blackCallback)
       self.blackLabel.grid(rowspan = 3, row = 5, column = 5, columnspan = 1)

       self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)

       self.eraser_button.grid(row=0, column=2)

       self.choose_size_button = Scale(self.root, from_=1, to=10,orient = HORIZONTAL)
       self.choose_size_button.grid(row=0, column=3) #the thickness slider

       self.c = Canvas(self.root, bg='white', width=600, height=600,relief= RAISED, bd= 2)
       self.c.grid(row=1, columnspan=5, column=1, padx=20, pady=20, rowspan=2) #and our actual Canvas!


       self.setup()

       self.root.mainloop()
#from here, we start attributing actions to our buttons, pen, eraser, etc
   def setup(self):
       self.old_x = None
       self.old_y = None
       self.line_width = self.choose_size_button.get()
       self.color = self.DEFAULT_COLOR
       self.active_button = self.pen_button
       self.eraser_on = False
       self.c.bind('<B1-Motion>', self.paint)
       self.c.bind('<ButtonRelease-1>', self.reset)

   def use_pen(self):
       self.activate_button(self.pen_button)

   def use_eraser(self):
       self.activate_button(self.eraser_button, eraser_mode=True)

   def activate_button(self, some_button, eraser_mode=False):

       self.active_button.config(relief=RAISED)
       some_button.config(relief=SUNKEN)
       self.active_button = some_button
       self.eraser_on = eraser_mode
#Here, you can see the callbacks that activate our color buttons
   def redCallback(self):
       self.eraser_on = False
       self.color = "red"

   def blueCallback(self):
       self.erase_on = False
       self.color = "blue"

   def greenCallback(self):
       self.eraser_on = False
       self.color = "green"

   def yellowCallback(self):
       self.eraser_on = False
       self.color = "gold"

   def blackCallback(self):
       self.eraser_on = False
       self.color = "black"

   def paint(self, event):
       self.line_width = self.choose_size_button.get()

       paint_color = 'white' if self.eraser_on else self.color
       if self.old_x and self.old_y:

           self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                              width=self.line_width, fill=paint_color,
                              capstyle=ROUND, smooth=TRUE, splinesteps=36)

       self.old_x = event.x
       self.old_y = event.y


   def reset(self, event):
       self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
