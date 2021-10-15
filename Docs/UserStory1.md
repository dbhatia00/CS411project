# User Story 1 - Login
The user must be able to log in through a Spotify account. The home page will be the login page, where the user can enter their information to log into our app through their Spotify account.

## Happy path:
The user can enter their Spotify account username and password in text boxes in the login page. If the account authenticates correctly, they will be logged into the app through their Spotify account, and will be brought to their playlists page (see user story 2).

## Exceptions:
- In case the user needs to reset their password, we will have a "forgot your password" link that will redirect them to the page where they can reset their Spotify password, and remain on the login page. 
- If the authentication fails, a message will appear notifying the user that their information was incorrect. We will remain on the login page so that the user can attempt to enter their information again, or use the "forgot your password" feature.