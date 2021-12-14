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

Spotify keys are needed for authentication via Spotify and should be inserted in settings.py at lines 128-9.

An IBM Watson API key is needed for sentiment analysis and should be inserted in views.py at line 127.