# Sportsera

This web application enables the user to book a sporting venue of their choice, which are recommended based on the safety guidelines published by the Government. This application also provides a feature of monitoring the correctness while performing an exercise rotine at home itself.
## Installation & Setup

### NodeJs: 
Use the [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) registry to install all the required NodeJs libraries to run this project.

```bash
npm install
```

### Python:
To install python to the system, refer this link - [Python](https://www.python.org/downloads/)

To install anaconda to the system, refer this link - [Anaconda](https://docs.anaconda.com/anaconda/install/)

Open Anaconda Prompt and type the command (to make a new virtual environment). 

```bash
conda create -n ENVNAME
```

To activate the new virtual environment.

```bash
conda activate ENVNAME
```
Now one should download the necessary libraries (in this virtual environment) as follows:

#### Opencv
```bash
conda install opencv
```

#### SQLite3
```bash
conda install -c blaze sqlite3
```

#### face-recognition
Since, the project has been executed in Windows, the following link would be helpful to provide guidance on installing 'face_recognition' library in Windows systems - [Youtube video](https://youtu.be/xaDJ5xnc8dc)

### SQLite database browser:
The following link is from where remote SQLite database browser can be downloaded - [SQLite](https://sqlitebrowser.org/dl/)

Data of different grounds must be filled into the GROUNDS table of the database and the time slots should be mentioned in the TIMESLOTS table. An example of this data is as follows -

![Alt Text](/public/images/Capture1.JPG)

![Alt Text](/public/images/Capture2.JPG)

### Speech interface:
Install "Handsfree for web" google chrome extensipn, which would be present in the chrome extension store.


## Usage
To run the project, go to the root directory of the project (within the conda virtual environment setup for the project) and type
```bash
nodemon server.js
```
The application takes atleast 3 min to start. Along with that, open the 'Handsfree for Web" extension, which is installed in the Chrome browser.
Once the message in the console prints "App started on port 3000", in the URL section of the browser, type [http://localhost:3000/](http://localhost:3000/)
