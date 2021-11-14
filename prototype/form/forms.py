from django import forms

class SongForm(forms.Form):
    song_title = forms.CharField(label='song title', max_length=100)

    