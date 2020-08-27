# -*- coding: utf-8 -*-

from tkinter import *
from math import sqrt


class scheme:

    GENERAL_TRIANGLE = "Obecný trojúhelník"
    RIGHT_TRIANGLE = "Pravoúhly trojúhelník"
    EQUILATERAL_TRIANGLE = "Rovnostraný trojúhelník"

    def __init__( self, root ):

        self._root = root
        self._root.title( "Trojúhelník" )

        self._body = Frame( self._root )
        self._body.pack( fill = BOTH, expand = 1, padx = 4, pady = 4 )
        
        self._topBlock = Frame( self._body, relief = GROOVE, borderwidth = 2 )
        self._topBlock.pack( fill = BOTH, padx = 4, pady = 4, ipady = 1 )

        self._leftBlock = Frame( self._body, relief = GROOVE, borderwidth = 2 )
        self._leftBlock.pack( fill = Y, side = LEFT, padx = 4, pady = 4, ipady = 4 )

        self._rightBlock = Frame( self._body, relief = FLAT, borderwidth = 2  )
        self._rightBlock.pack( fill = BOTH, expand = 1, padx = 2, pady = 2 )

        self._rightBlockTop = Frame( self._rightBlock, relief = GROOVE, borderwidth = 2 )
        self._rightBlockTop.pack( fill = BOTH, expand = 1 )

        self._rightBlockRight = Frame( self._rightBlock, relief = FLAT )
        self._rightBlockRight.pack( fill = X, side = RIGHT, expand = 1 )

        self._rightBlockLeft = Frame( self._rightBlock, relief = FLAT )
        self._rightBlockLeft.pack( fill = X, side = LEFT, expand = 1 )


        self._labelA = Label( self._topBlock, text = "Obvod a obsah trojúhelníku." )
        self._labelA.pack( padx = 8, pady = 10 )

        self._labelB = Label( self._leftBlock, text = "Strana a =" )
        self._labelC = Label( self._leftBlock, text = "Strana b =" )
        self._labelD = Label( self._leftBlock, text = "Strana c =" )

        self._inputB = Entry( self._leftBlock, width = 14 )
        self._inputC = Entry( self._leftBlock, width = 14 )
        self._inputD = Entry( self._leftBlock, width = 14 )

        self._labelB.pack( fill = X, padx = 8, pady = 1 )
        self._inputB.pack( padx = 8, pady = 1 )
        self._labelC.pack( fill = X, padx = 8, pady = 1 )
        self._inputC.pack( padx = 8, pady = 1 )
        self._labelD.pack( fill = X, padx = 8, pady = 1 )       
        self._inputD.pack( padx = 8, pady = 1 )

        self._labelE = Label( self._rightBlockTop, text = "Výsledek ").pack()

        self._buttonA = Button( self._leftBlock, text = "Vymazat", command = self.reset, width = 10 )
        self._buttonA.pack( padx = 4, pady = 4 )
        
        self._ButtonB = Button( self._rightBlockLeft, text = "Vyřešit", command = self.solve, width = 10, height = 2 )
        self._ButtonB.pack( side = RIGHT, pady = 4, padx = 4 )

        self._buttonC = Button( self._rightBlockRight, text = "Konec", command = root.destroy, width = 10, height = 2 )
        self._buttonC.pack( side = LEFT, pady = 4, padx = 4 )

        self._resultPlace = Frame( self._rightBlockTop, relief = SUNKEN, background = "#BFBFBF", borderwidth = 2 )
        self._resultPlace.pack( fill = BOTH, expand = 1, padx = 8, pady = 8 )

        self._labelF = Label( self._resultPlace, text = "Zatím žádný výsledek", background = "#BFBFBF" )
        self._labelF.place( relx = 0.5, rely = 0.5, anchor = CENTER )
        
        self.reset()

        
    def reset( self ):

        self._inputB.delete( 0, END )
        self._inputC.delete( 0, END )
        self._inputD.delete( 0, END )

        self._inputB.insert( 0, "0" )
        self._inputC.insert( 0, "0" )
        self._inputD.insert( 0, "0" )

        self._inputB.focus_force()
        
    
    def solve( self ):

        try:

            aSize = float( self._inputB.get() )
            bSize = float( self._inputC.get() )
            cSize = float( self._inputD.get() )
            
            text = scheme.GENERAL_TRIANGLE

            if self.is_triangle( aSize, bSize, cSize ):

                if self.is_right_triangle( aSize, bSize, cSize ):

                    text = scheme.RIGHT_TRIANGLE

                if self.is_equilateral_triangle( aSize, bSize, cSize ):

                    text = scheme.EQUILATERAL_TRIANGLE

            else:

                text = "Tohle není trojúhelník!"
                self._labelF['foreground'] = "red"

            if text == "Tohle není trojúhelník!":

                self._labelF['foreground'] = "red"  

            else:
                text += self.compute_circumference( aSize, bSize, cSize )
                text += self.compute_area( aSize, bSize, cSize )
                self._labelF['foreground'] = "blue"  
            
            self._labelF['text'] = text
                

        except ValueError:

            self._labelF['text'] = "Tohle není ani číslo!"
            self._labelF['foreground'] = "red"
            pass
        
        
    def compute_circumference( self, a, b, c ):
        return "\n\nObvod: = " + str(a + b + c)
    
    
    def compute_area( self, a, b, c ):

        s = (a + b + c) / 2
        return "\nObsah: = {:.2f}".format( sqrt( s * ( s - a ) * ( s - b ) * ( s - c ) ) )
        
        
    def is_triangle( self, a, b, c ):

        if a + b + c > 2 * max( a, b, c ):

            return True

        return False
        
        
    def is_right_triangle( self, a, b, c ):

        if a**2 + b**2 + c**2 == 2* max( a,b,c )**2:

            return True

        return False
        
        
    def is_equilateral_triangle( self, a, b, c ):

        if( a == b or a == c or a == b):
        
            return True
        
        return False


def main(): 

    root = Tk()
    scheme( root )
    root.mainloop()


main ()