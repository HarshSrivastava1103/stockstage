import PySimpleGUI as sg

# Define the layout of the signup form with styling
layout = [
    [sg.Text('Signup Form', size=(20, 1), justification='center', font=('Helvetica', 30), text_color='white',
             relief=sg.RELIEF_RIDGE, background_color='black')],
    [sg.Text('Username:', size=(15, 1), font=('Helvetica', 20), text_color='white'),
     sg.InputText(key='username', size=(30, 1), font=('Helvetica', 20))],
    [sg.Text('Email:', size=(15, 1), font=('Helvetica', 20), text_color='white'),
     sg.InputText(key='email', size=(30, 1), font=('Helvetica', 20))],
    [sg.Text('Password:', size=(15, 1), font=('Helvetica', 20), text_color='white'),
     sg.InputText(key='password', size=(30, 1), font=('Helvetica', 20), password_char='*')],
    [sg.Button('Sign Up', size=(15, 2), font=('Helvetica', 20), button_color=('white', 'green'), pad=((200, 0), 20)),
     sg.Button('Cancel', size=(15, 2), font=('Helvetica', 20), button_color=('white', 'red'))],
    [sg.Text('', size=(40, 1), font=('Helvetica', 14), text_color='red', key='error_message')]
]

# Create the signup form window
window = sg.Window('Signup Form', layout, element_justification='c', background_color='black')

# Event loop to capture form submissions
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Sign Up':
        username = values['username']
        email = values['email']
        password = values['password']

        # Simple input validation
        if not username or not email or not password:
            window['error_message'].update('All fields are required.')
        elif '@' not in email:
            window['error_message'].update('Invalid email address.')
        else:
            # Process signup data here

            print("Signup Successful!")
            print("Username:", username)
            print("Email:", email)
            # Avoid printing password in real-world scenarios for security reasons

            # Close the signup form window
            window.close()

            # Open a new window with welcome message
            welcome_layout = [
                [sg.Text('Welcome to Stock Stage: Start today', size=(40, 1), justification='center',
                         font=('Helvetica', 30), text_color='white', relief=sg.RELIEF_RIDGE, background_color='black')]
            ]
            sg.Window('Welcome Message', welcome_layout, element_justification='c',
                      background_color='black').finalize().read(close=True)
            break

# Close the window
window.close()
