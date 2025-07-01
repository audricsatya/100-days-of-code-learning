# Day 46: Spotify Playlist Automation

This project demonstrates how to automate the creation and management of Spotify playlists using Python and the [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) library.

## Features

- Authenticate with Spotify using OAuth
- Create a new playlist
- Search for tracks by name or artist
- Add tracks to the playlist

## Requirements

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)
- Spotify Developer Account (for API credentials)

## Setup

1. Install Spotipy:

   ```bash
   pip install spotipy
   ```

2. Create a Spotify app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and note your `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI`.

3. Set your credentials as environment variables:
   ```bash
   export SPOTIPY_CLIENT_ID='your_client_id'
   export SPOTIPY_CLIENT_SECRET='your_client_secret'
   export SPOTIPY_REDIRECT_URI='your_redirect_uri'
   ```

## Notes

- Update the `tracks` list with your desired songs.
- The script will print the link to your new playlist.

## References

- [Spotipy Documentation](https://spotipy.readthedocs.io/en/2.22.1/)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
