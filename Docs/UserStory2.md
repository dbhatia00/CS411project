# User Story 2 -Playlists
The playlists page will allow the user to select which of their playlists they would like to include in their profile (store in our database). 

## Happy path:
- After logging in (see user story 1) the user must be able to choose playlists to include in their profile for compatibility testing. This screen will show a list of their Spotify playlists with a checkbox to the left of each playlist. By default, none of the playlists will be selected. The user can decide for each playlist whether they wish to include it, by either checking the box or leaving it unchecked. 
- After the list of playlists, there will be a save changes button. When this button is pressed, any playlists that were newly unchecked will be unloaded from the database, and any playlists that were newly checked will be loaded into the database.
- At the bottom of the page, there will be a "Friends list" button which will redirect the user to the friends list page (see user story 3) where they can measure compatibility with friends.
- There will also be a "logout" button, which will log the user out of their Spotify account then redirect them to the login page (see user story 1).


## Exceptions:
- If the user doesn’t have any playlists available, we will show a warning that no playlists were found on the user's Spotify account.