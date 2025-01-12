# Data Management Project 
## Team Leaders Contact Information 
- Team Leader: Hugo Ngo
- Email: hugongo@cmail.carleton.ca
## Date 
- 9th December , 2022
## Software Name and Version 
- Python Version 3.10.7 [https://www.python.org/]
- Numpy Library Version 1.23.0 [https://numpy.org/]
- MatPlot Library Version 3.6.0 [https://matplotlib.org/]
- Spicy Library Version 1.9.3 [https://docs.scipy.org/doc/scipy/reference/optimize.html]
## Description 
>This project organizes data from a spreadsheet into multiple dictionaries (each organized based on one specific aspect of information about the student). These dictionaries were tested to make sure that they contain all the information from the csv file. Functions were created that sort the dictionaries based on one specific aspect of the information about the students (for example, a user could sort the information from lowest to highest grade average (G_Avg). Polynomial functions were then created to graph the data into histograms to easily view the data. Functions were created that dispaly the x and y coordinate of the local maximum and minimum of the graph for any given piece of information. Finally, UI allows the user to type in exactly what is needed to be displayed. Data can be viewed in organized and simplified ways, depending on the choice typed into UI. 

## Installation
- Latest version of all softwares are provided with detail in the "Software Name and Version" section.
- A python IDE to open the folder.
- The IDE which was used to create the project was WING 101.8 [https://wingware.com/downloads/wing-101]
- Project application is delivered in form of T038_data_analyzer.zip folder. Unzip for usage. Or run this bash:

  ```bash
  git clone https://github.com/hugoTheVoidBoy/Data_Management
  cd Data_Management
  cd T038_data_analyzer
  pip install matplotlib
  pip install scipy
  python T038_M3_text_ui.py

  
## Usage 
> The application is delivered in T038_data_analyzer.zip folder. Unzip in your desired location where the data file is located.
**Make sure T038_data_analyzer folder is in the same folder with the data file!**
To use Data Analyzer, run '*text_ui.py*' file. A User Interface will show up. Type in the letter to use the commands. Case does not matter. 
- Always load "L" the data from a file first, based on which key is needed to load data. 
- Load "S" is to sort data from low to high, based on the categories listed on the menu.
- Load "H" to show histogram of the overall statistics of the categories listed on the menu.
- Load "W" to show the worst Average Grade data of the category listed on the menu.
- Load "B" to show the best Average Grade data of the category listed on the menu.
- Load 'Q' to quit user interface. 
- *If un unrecognized command is entered, user can choose to type in another command*

```bash 
        The available commands are:
        1. L) oad Data
        2. S) ort Data
         'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg'
        3. H) istogram
         'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences'
        4. W) orst ______ for Grades
         'Age', 'StudyTime', 'Failures', 'Health', 'Absences'
        5. B) est ______ for Grades
         'Age', 'StudyTime', 'Failures', 'Health', 'Absences'
        6. Q) uit
        Please type your command:
```
> Batch_ui.py is a user interface for batching a text file for commands. 
**All inputs are seperated by a ' ; ' semicolon**.
An example test.txt file is given.

```txt
L;student-mat.csv;Age
s;G1;Y
b;Age
w;Health
h;StudyTime
h;Failures
c;School
Q
s;School;Y
```

> <L> Load data must always come first, followed by the data file name and then the key to load data.
'S','H','B','W','Q' does the same functions as the Text User Interface *text_ui.py*
## Credits 
|Team Member| Role |
| ------ | ------ |
| Amber Boies | Student Ages Dictionary, Values of Dictionaries Test, Selection Sort, Function, Text UI |
| Ashley Tran| Student School Dictionary, Keys of Dictionaries Test,  Histogram Function, Maximum Function  |
| Lucas Hallam | Student Health Dictionary, Size of List Test, Bubble Sort, Minimum Function
| Hugo Ngo | Student Failures Dictionary, G_Avg Test, Curve Fit Function, Batch UI  |
