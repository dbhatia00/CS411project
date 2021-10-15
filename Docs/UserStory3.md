# User Story 3 - Friends List
The Friends list shows all the user's friends from Spotify so that they can select one to request a compatibility rating with. 

## Happy path:
- As a logged in user, the user wants to be able to see my friends list to be able to select friends that will be used for compatibility testing.
- My friends list should have 2 sections: friends who have songs in the database (logged in through the app), and all other friends in Spotify
- There will also be a "logout" button, which will log the user out of their Spotify account then redirect them to the login page (see user story 1).
- At the bottom of the page, there will be a "Playlist list" button which will redirect the user to the playlist page (see user story 2) where they can see their playlists.

## Exception:
- If the user has no friends on this page, then that means they have no friends in Spotify. This is because the friends page should show all their friends on Spotify even if they haven't registered in our app yet.