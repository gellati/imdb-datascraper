#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Button, Entry, Text, END
from MovieDataSearcher import MovieDataSearcher

frameWidth=300
frameHeight = 300

class MainFrame(Frame):
    def __init__(self, parent):
        frame = Frame(parent, width=frameWidth, height=frameHeight)
        frame.pack()

        self.inputArea = InputArea(frame)
        self.outputArea = OutputArea(frame)
        self.searchButton = SearchButton(frame)        

        self.inputArea.setSearcher(MovieDataSearcher())
        self.inputArea.setButton(self.searchButton)
        self.inputArea.setOutputArea(self.outputArea)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)

        self.inputArea.pack()
        self.searchButton.pack()
        self.outputArea.pack()
        self.quitButton.pack()
       
        
class InputArea(Entry):
    def __init__(self, parent):
        Entry.__init__(self, parent)

    def setOutputArea(self, outputArea):
        self.outputArea = outputArea

    def setSearcher(self, searcher):
        self.movieSearcher = searcher

    def setButton(self, searchButton):
        self.searchButton = searchButton
        self.searchButton.bind('<Button-1>', self.buttonClicked)

    def buttonClicked(self, evt):
        text = self.get()
#        print text
        results  = self.movieSearcher.searchMovie(text)
        self.outputArea.writeText(results)
#        print results


class OutputArea(Text):
    def __init__(self, parent):
        Text.__init__(self, parent)

    def clearText(self):
        self.delete("1.0", END)

    def writeText(self, text):
        self.clearText()
        self.insert("1.0", text)
    
class SearchButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent, text="Get movie data")

root = Tk()
root.wm_title("IMDb searcher")
mf = MainFrame(root)
root.mainloop()
root.destroy()
