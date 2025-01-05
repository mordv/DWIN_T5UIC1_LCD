from dwinlcd import DWIN_LCD

encoder_Pins = (27, 26)
button_Pin = 24
LCD_COM_Port = '/dev/ttyS0'
API_Key = 'XXXXXX'

DWINLCD = DWIN_LCD(
    '/home/orangepi/printer_data/comms/klippy.sock',
    LCD_COM_Port,
    encoder_Pins,
    button_Pin,
    API_Key
)
