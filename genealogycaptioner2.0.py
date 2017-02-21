from tkinter import Frame, Tk, BOTH, Text, Menu, END, ttk
from tkinter import filedialog
from tkinter import *
import PIL
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import Tk    
from tkinter import simpledialog
from PIL import ImageFont
from PIL import ImageDraw
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageTk, ImageChops
import textwrap



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        #global variable declaration for entry and combobox
        global e1
        global fontevar

        #Titles the window and chooses grid geometry manager
        self.parent.title("Captioning Tool")
        self.grid()

        #the file menu with the open file option
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        #Text Size Entry box

        Label(self, text="Text Size").grid(row=0)
        e1 = Entry(self)
        e1.grid(row=0, column=1)
        e1.insert(10,"30")

        #Apply button
        Button(self, text='Apply', command=self.change_text_size).grid(row=6, column=0, sticky=W, pady=4)

        #combobox
        Label(self, text="Font Type").grid(row=4)
        fontevar = StringVar()
        fonte = ttk.Combobox(self, textvariable=fontevar)
        fonte.state(['readonly'])
        fonte.bind('<<ComboboxSelected>>', self.which_font)
        fonte['values'] = ('Normal', 'Bold', 'Italicized', 'Bold and Italicized')
        fonte.grid(row=4, column=1)

        


    def onOpen(self):
            global font
            im = Image.open(askopenfilename())          #opens dialog for user to select an image
            caption = simpledialog.askstring("Label", "What would you like the label on your picture to say?") #user input for text
                               #font size, font color, math for determining pixel size of courrier font 
            fontcolor = (0,0,0)
            pixelw = int(0.6 * fontsize)
    
            if (font == 'Normal'):
                font = ImageFont.truetype('cour.ttf', fontsize)
            elif (font == 'Bold'):
                font = ImageFont.truetype('courbd.ttf', fontsize)
            elif (font == 'Italicized'):
                font = ImageFont.truetype('couri.ttf', fontsize)
            elif (font == 'Bold and Italicized'):
                font = ImageFont.truetype('courbi.ttf', fontsize)
            if im.mode != "RGBA":           #converts image to correct color format
                im = im.convert("RGBA")
            txt = Image.new('RGBA', im.size, (255,255,255,0))   #creates a temporary image, draws text on it, then determines the height needed for the caption from the total height of the text
            draw = ImageDraw.Draw(txt)

            fontfinal = font
            
            w ,h =txt.size
            tempimg = Image.new("RGBA", (1,1))
            draw2 = ImageDraw.Draw(tempimg)
            width= int((w/pixelw))
            text = textwrap.fill(caption,width)
            textsize = draw.textsize(text, font)
            [W,H] =textsize


            txt = Image.new('RGBA', (w,H), (255,255,255,0))
            draw = ImageDraw.Draw(txt)
            
            w ,h =txt.size
            text = textwrap.fill(caption,width)
            draw.text((0,0), text, font=font, fill="Black")

            


            

            images = [im , txt]
            widths, heights = zip(*(i.size for i in images))
            total_width = max(widths)
            max_height = sum(heights)

            new_im = Image.new('RGB', (total_width, max_height))
            y_offset = 0
            for im in images:
                new_im.paste(im, (0,y_offset))
                y_offset += im.size[1]





            file = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
            if file:
                abs_path = os.path.abspath(file.name)
                out = new_im
                out.save(abs_path) # saves the image to the input file name. 
            

    def change_text_size(self):
        global fontsize
        fontsize = int(e1.get())
    def which_font(self,fonte):
        global font
        font = str(fontevar.get())
        print(font)
        

def main():

    root = Tk()

    
    
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  
