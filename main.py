Temperatura_corregida = 0
Temperatura = 0
Valor_correccion = 3

def on_forever():
    global Temperatura, Temperatura_corregida
    Temperatura = input.temperature()
    Temperatura_corregida = Temperatura - Valor_correccion
    basic.show_number(Temperatura_corregida)
    basic.pause(1000)
basic.forever(on_forever)
