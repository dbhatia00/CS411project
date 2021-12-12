# User Story 2 - Logout
At every point in the application there will be a button to logout. This should return the user to the main page.

## Happy path:
- At any screen the user will be given the option to sign out via a button click
- The button click will return the user to the login page, giving them the option to log back into the application
- This should also reset the application fully, wiping out the database



## Exceptions:
- If the user isn’t signed in (and therefore cannot be signed out), the application will return an error message and return the user to the login screen.