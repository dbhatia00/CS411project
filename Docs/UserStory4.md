# User Story 4 - Analyze Compatibility
From the friends list page (see user story 3) the user will be able to select a specific friend to calculate their compatibility with.

## Happy Path - 

The app will perform a sentiment analysis based on the lyrics of the songs in the user's selected playlist(s) and the friend’s selected playlist(s). The general flow should be as follows -

- User sees a list of their spotify friends, and selects a friend
- User confirms that they would like a compatibility rating with their friend
- The application performs a sentiment analysis on all songs in the user's playlist(s) and all songs in the friend’s playlist(s)
- The application returns a rating based on the sentiment analysis. 

## Exceptions - 
- If the songs in the playlist do not have lyrics available, an error message should be displayed
- If the user has no playlists selected, the application should display an error, and redirect the user to the playlist page (see user story 2)
- If the user has no friends registered in the app, the user will not be able to select anybody for a compatibility rating