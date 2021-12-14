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
