# Random Destination game
![image alt](https://github.com/Aranzaavila/python-project/blob/08dd9e78529fa28cbb3194756999804e8cc6ac67/bg.webp)
This project is a simple graphical user interface (GUI) application created using the Tkinter library in Python. It functions as a "Random Destination Game" where users can select a type of weather (warm or cold) to receive a random travel destination and then view activities available in that destination

## Table of contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Error Handling](#error_handling)
- [How to run](#how_to_run)
- [Usage](#usage)
- [Future Enhancements](#future_enhancements)
- [License](#license)
- [Author](#author)


## Features
- Choose between warm or cold weather for your vacation.
- Get a random destination based on your selection.
- View popular activities associated with the selected destination.
- User-friendly graphical interface built with Tkinter.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)
- JSON file (`data.json`) containing destination data

## Error Handling
- If the data.json file is not found, an error message will be displayed, and the program will exit.
- If no activities are available for a selected destination, the user is notified via a warning.

## Installation
1. Clone this repository or download the project files.
2. Ensure you have Python 3.x installed on your machine.
3. Create a JSON file named `data.json` in the same directory as the script, structured as follows:
![image alt](https://github.com/Aranzaavila/python-project/blob/f44fd51999ff4dccf16acc5ec02ecdd05786a007/ss.png)



## How to Run
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using:
`python script_name.py`

5. Follow the on-screen instructions to select your preferred vacation type and view the results.

## Usage
1. Launch the App: Start the program to see the main window.
2. Select Weather: Click the Warm or Cold button to receive a suggested destination.
3. View Activities: Once a destination is suggested, click Show Activities to see a list of popular activities.
4. Exit: Click the Exit button to close the application

## Future Enhancements
- Add more destinations and activities.
- Include more weather types or filters (e.g., adventure destinations, family-friendly places).
- Save user preferences and history for future sessions

## Lisence
This project is licensed under the MIT License. Feel free to use, modify, and share it as you like.


## Author
Aranza Avila :)


