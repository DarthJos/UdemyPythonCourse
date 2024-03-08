import PySimpleGUI as sg
import BonusExamples.ConverterMethods as converter

window_title = "Convertor"

enter_feet_label = sg.Text("Enter feet:")
enter_inches_label = sg.Text("Enter inches:")

enter_feet_input = sg.Input(key="feet_input")
enter_inches_input = sg.Input(key="inches_input")

convert_button = sg.Button("Convert", key="convert_btn")
output_label = sg.Text(key="output")

window = sg.Window(window_title,
                   layout=[
                       [enter_feet_label, enter_feet_input],
                       [enter_inches_label, enter_inches_input],
                       [convert_button, output_label]
                   ])

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    feet = float(values['feet_input'])
    inches = float(values['inches_input'])

    meters = converter.convert(feet, inches)
    window['output'].update(value=f"{meters} m")


window.close()
