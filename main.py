#go extensions and add ir makerbit-ir
Button1 = ""
basic.show_leds("""
    # . . . .
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    """)
basic.pause(1000)
basic.clear_screen()
while True:
    makerbit.connect_ir_receiver(DigitalPin.P8, IrProtocol.NEC)
    Button1 = convert_to_text(makerbit.ir_datagram())
    if Button1 == "0x00FFB04F":
        basic.show_number(0)
    if Button1 == "0x00FF08F7":
        basic.show_number(1)
    if Button1 == "0x00FF8877":
        basic.show_number(2)
    if Button1 == "0x00FF48B7":
        basic.show_number(3)
    if Button1 == "0x00FF28D7":
        basic.show_number(4)
    if Button1 == "0x00FFA857":
        basic.show_number(5)
    if Button1 == "0x00FF6897":
        basic.show_number(6)
    if Button1 == "0x00FF18E7":
        basic.show_number(7)
    if Button1 == "0x00FF9867":
        basic.show_number(8)
    if Button1 == "0x00FF58A7":
        basic.show_number(9)
    if Button1 == "0x00FF20DF":
        basic.show_string("turnLeft")
    if Button1 == "0x00FF00FF":
        basic.show_string("STOP")
    if Button1 == "0x00FF609F":
        basic.show_string("turnRight")
    if Button1 == "0x00FF40BF":
        basic.show_string("Light")