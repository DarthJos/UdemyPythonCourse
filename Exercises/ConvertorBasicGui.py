import PySimpleGUI as sg

window_title = "Convertor"
enter_fee_label = sg.Text("Enter feet:")
enter_inches_label = sg.Text("Enter inches:")
enter_fee_input = sg.Input()
enter_inches_input = sg.Input()
convert_button = sg.Button("Convert")

window = sg.Window(window_title,
                   layout=[
                       [enter_fee_label, enter_fee_input],
                       [enter_inches_label, enter_inches_input],
                       [convert_button]
                   ])

window.read()
window.close()