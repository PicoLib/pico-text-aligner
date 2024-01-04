import math
import utime

class TextAlign:
    """Class to align long text accourding to screen viewport and generate lines of text into an array"""

    def __init__(self, screenwidth: int, screenheight: int, charsize: int):
        self._swidth = screenwidth
        self._sheight = screenheight
        self._charsize = charsize
        self._maxchar = math.floor(screenwidth/charsize)
        self._lineheight = round(charsize/2)
        self._maxlines = round(screenheight/(self._charsize+self._lineheight))

    def array(self, text: str):
        """This function will generate a array of possible lines"""

        text_array = text.split(' ')
        lines = []
        lnumber = 0
        for item in range(0, len(text_array)):

            if len(text_array[item]) > (self._maxchar-1):
                nt = []
                for i in range(0, len(text_array[item]), self._maxchar-1):
                    nt.append(text_array[item][i:i+self._maxchar-1]+"-")
                nt[len(nt)-1]=nt[len(nt)-1].replace("-","")
                text_array.pop(item)
                text_array[item:item] = nt

            if not lines:
                lines.append(text_array[item])
            else:
                if (len(lines[lnumber])+len(text_array[item])+1) < self._maxchar:
                    lines[lnumber] = lines[lnumber] + " " + text_array[item]
                else:
                    lines.append(text_array[item])
                    lnumber += 1

        return lines
    

    def show(self, text: str, xindex=0, yindex=0, scroll=True):
        """This function will show text in lines, you can make scroll:False to not scrolling through lines"""

        self._xindex = xindex
        self._yindex = yindex

        def rstIndex():
            self._xindex = xindex
            self._yindex = yindex

        #This part added to configure lcd or oled hardware (remove this part if configured it already)
        from ssd1306 import SSD1306_I2C
        from machine import Pin, I2C
        i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=1000000) #Change pins accourding to your config
        oled = SSD1306_I2C(self._swidth,self._sheight,i2c) #You can use other screens libraries too
        ###

        obj = self.array(text)
        oled.fill(0)
        
        if len(obj) > self._maxlines and scroll == True:    

            for i in range(0, len(obj)*(self._charsize+self._lineheight)):
                for y in range(0, len(obj)):
                    oled.text(obj[y], self._xindex, self._yindex-i)
                    self._yindex += self._charsize+self._lineheight
                    oled.show()
                rstIndex()
                utime.sleep(0.5)
                oled.fill(0)

        else:

            for i in range(0, len(obj)):
                oled.text(obj[i], xindex, yindex)
                oled.show()
                yindex += self._charsize+self._lineheight