# Changes from Original Specifications

In this document , we aim to describe the ways in which we altered the application from the original design.

First and foremost, we eliminated the friend-finding and comparison side of the application. Though this would have been a nice addition,
we felt as though we would not have the time to implement it correctly. 

Second, instead of having the user select a song from their playlists we allow the user to enter the name of a song. This gives the user 
more freedom in entering the songs that they want, instead of just what appears to be in their playlist. 

Third, we utilized Genius Lyrics API and IBM's Watson ToneAnalyzer to produce the top three emotional and language tones of a song based on its lyrics.
Examples of tones include joy, sadness, tentative, etc.

Lastly, we altered the scope by producing a sentiment analysis report for a single user instead of a compatibility report between two users due 
to time restrictions and difficulty accessing playlists and user information from the Spotify API. 

A note about the Spotify API, the service does not store any lyrics or have them accessible. For this reason, we introduced another API - the Genius API. Given the title of a song (provided by the user) and the name of the artist (pulled from the Spotify API using the song title), Genius will return the lyrics of any song within their database. Introducing this allowed for us to pull lyrics to be sent to the Watson API.
