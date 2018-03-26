# SFPD Dispatch: Predictor and Analyzer
This app was created for the Capital One Software Engineering Summit Spring 2018 Mindsumo Challenge.
Challenge Prompt: https://www.mindsumo.com/contests/sfpd-dispatch
A Live Demo of My Solution: http://sahilmayenkar.pythonanywhere.com/

## Description
### Technologies used:
Front-End: HTML, CSS, JavaScript, JQuery, Material Design Lite CSS Framework (and various sub-implementations), Google Charts API, Google Places API, Moment.js
Back-End: Python, Pandas,  Flask, Jinja2 Templating Engine

### Functionality
a)	Data Visuals: I provided three different visualizations: a pie chart of the distributions of incoming call types, the average response time for each task (where required) in responding to a particular incident, and a line graph visualizing call volumes per day.
b)	Predictions: A user starts by inputting an address into the appropriate field. Suggestions from the Google Places API pop up to assist the user in appropriately selecting the correct place. The user can also use the material design time tool to pick a time. Upon clicking the calculate button, the website submits an ajax request to my backend, which computes the most likely dispatch type. The app searches for instances within 2 hours in each direction and within a one mile radius. Distance is calculated based on this formula: http://janmatuschek.de/LatitudeLongitudeBoundingCoordinates
c)	I have graphed the average dispatch times of the highest three zip codes as well as the overall over all zip codes.

## Running the Code on Your Own System
NOTE: Because I developed this on a Windows machine, the instructions below apply to Windows computers. The app can probably still run on a Linux or Mac machine, but the commands may be slightly different and, as the Virtual Env is configured for Windows, you would need to download all the required libraries/packages separately.

1.	Navigate to the main project folder using your terminal. The folder name is ‘sfpd-dispatch’.
2.	Enter the command ‘venv\Scripts\activate’. Your terminal should now show ‘(venv)’ before your actual directory.
3.	Enter the command ‘set FLASK_APP=sfpd-dispatch.py’.
4.	Enter the command ‘flask run’
5.	After a minute or two, the application would’ve started up! You can now view it in your web browser at http://localhost:5000/ 
