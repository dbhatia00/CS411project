# Song Sentiment Analysis

by Ciaran, Dana, Dev, and Prath

## App Description

Our web app allows an user to login through Spotify, then search for songs so that lyrics can be pulled from the Genius API and analyzed through the IBM Watson API. The tone of songs are displayed on the reports page, and additional songs can be searched for on the songs page. 

## Docs Organization

Project Proposal.md - This is the original project proposal which includes both options we considered.

The following user stories were updated to reflect the final project version:

UserStory1.md - Login

UserStory2.md - Logout

UserStory3.md - Songs Page

UserStory4.md - Reports Page

changesFromOriginalSpec.md - This document describes the changes we made in the scope of the project.

prototypeTechChoice.md - This document is for assignment 3 and descibes the frameworks we considered, and how we came to choose Django for the project.

prototypeVideoDemo.mkv - This is the video for assignment 3 showing the working prototype.

## Code Organization

The project was done progressively through the Git Repo, and all major changes are recorded there. The 'prototype' branch contains the code for the assignment 3 prototype, and master contains the final version.

## Keys Required

Spotify keys are needed for authentication via Spotify (create one [here](https://developer.spotify.com/) and should be inserted in settings.py at lines 128-9.

You must have an IBM cloud account to use the ToneAnalyzer which can be found [here](https://cloud.ibm.com/registration). 
Additionally, a subscription to ToneAnalyzer is required for an API key which can be found [here](https://cloud.ibm.com/catalog/services/tone-analyzer). Insert the API key into views.py at line 127.

## Running the Application

To run the application, activate the virtual environment which can be found in prototype/venv. 
Next, run 'python manage.py runserver' and type 'localhost:8000' into your browser. 
