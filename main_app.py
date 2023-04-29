import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")

success_message = sg.Text("", size=(30, 1), text_color="yellow", key="success_message")
error_message = sg.Text("", size=(30, 1), text_color="red", key="error_message")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2], [compress_button],
                           [success_message], [error_message]])

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Compress":
        filepath = values['files'].split(';')
        folder = values['folder']
        try:
            make_archive(filepath, folder)
            success_text = "Success!"
            window['success_message'].update(success_text)
            window['error_message'].update("")  # Clear the error message if the operation was successful
        except Exception as e:
            error_text = f"Error: {str(e)}"
            window['error_message'].update(error_text)
            window['success_message'].update("")

    print('Event: ', event)
    print('Values: ', values)
    print('Type of \'values\' returned: ', type(values))

    print('Values chosen by \'files\' key: ', filepath)
    print('Values chosen by \'folder\' key: ', folder)
    print('Type of \'filepath\': ', type(filepath))
    print('Type of \'folder\': ', type(folder))
    print(filepath[0])
    # make_archive(filepath, folder)
    # success_text = "Success!"
    # window['success_message'].update(success_text)

window.close()
