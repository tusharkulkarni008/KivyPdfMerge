# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:30:57 2022

@author: chanakya
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
import os
from PyPDF2 import PdfFileMerger
# set window size
Window.size = (300, 450)
# load the string for design
Builder.load_string("""
<CalLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        TextInput:
            id:input
            text:"0"
            halign:"right"
            font_size:30
            size_hint:(1, .10)
        GridLayout:
            cols:2
            rows:2
            # first row
            Button:
                size_hint:(.4, .2)
                font_size:32
                text:"Merge"
                on_press:root.Merge()
            Button:
                size_hint:(.4, .2)
                font_size:32
                text:"Clear"
                on_press:root.clear()
            
            
           
""")
# Create a class for calculator layout
class CalLayout(Widget):
    # function to clear text field
    def clear(self):
        self.ids.input.text=""
    # function to delete last number
    # from text field
    def Merge(self):
        x = [a for a in os.listdir(self.ids.input.text) if a.endswith(".pdf")]

        merger = PdfFileMerger()

        for pdf in x:
            merger.append(open(pdf, 'rb'))

        with open("result.pdf", "wb") as fout:
            merger.write(fout)
    # function take button inuputs pressed
    # by user
    def pressed(self, button):
        # expression to store all text field values
        expression = self.ids.input.text
        # if text field expression contains  
        # error then set it to empty field
        if "Error" in expression:
            expression = ""
        # if text filed expression contains
        # 0 then first set the field to empty and
        # display the button text pressed by user
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"
# class to create calculator app    
class CalculatorApp(App):
    # function to build app layout
    def build(self):
        return CalLayout()
# create an object of class
cal = CalculatorApp()
# run the app using object
cal.run()