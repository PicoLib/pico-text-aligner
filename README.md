# Text Aligner for Raspberry Pi Pico

With help of this module, you can show long text on a small screen without worry about overflowing text from screen.

## Usage

## How to use?

Download [`aligner.py`](./aligner.py) from this and use two function.

### Important Note

If you already configure your oled or lcd please remove this part and change "oled" variable to your given variable.  

```python
#This part added to configure lcd or oled hardware (remove this part if configured it already)
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=1000000) #Change pins accourding to your config
oled = SSD1306_I2C(self._swidth,self._sheight,i2c) #You can use other screens libraries too
###
```
