## Dataset
- **Nama Dataset**: Spotify Most Streamed Songs  
- **Format**: CSV  
- **Sumber**: Kaggle

Dataset ini berisi informasi lagu-lagu yang paling sering diputar di Spotify beserta karakteristik audio dan performa chart-nya.

### Sumber Dataset:  
[Spotify Most Streamed Songs – Kaggle]([https://www.kaggle.com/](https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs))

---

### Informasi Dataset (Daftar Fitur)
| Column | Description |
|------|-------------|
| `track_name` | Song title |
| `artist(s)_name` | Name of the artist(s) |
| `artist_count` | Number of artists involved |
| `released_year` | Year the song was released |
| `released_month` | Month the song was released |
| `released_day` | Day the song was released |
| `in_spotify_playlists` | Number of Spotify playlists containing the song |
| `in_spotify_charts` | Position in Spotify charts |
| `streams` | Total number of streams |
| `in_apple_playlists` | Number of Apple Music playlists containing the song |
| `in_apple_charts` | Position in Apple Music charts |
| `in_deezer_playlists` | Number of Deezer playlists containing the song |
| `in_deezer_charts` | Position in Deezer charts |
| `in_shazam_charts` | Position in Shazam charts |
| `bpm` | Tempo of the song (beats per minute) |
| `key` | Musical key of the song |
| `mode` | Musical mode (1 = Major, 0 = Minor) |
| `danceability_%` | Danceability level (%) |
| `valence_%` | Positivity of the song (%) |
| `energy_%` | Energy level (%) |
| `acousticness_%` | Acoustic level (%) |
| `instrumentalness_%` | Instrumental level (%) |
| `liveness_%` | Live performance likelihood (%) |
| `speechiness_%` | Amount of spoken words (%) |
| `cover_url` | URL of the song cover image |

#### Metadata Lagu
- `track_name`  
- `artist_name`  
- `artist_count`  
- `released_year`  
- `released_month`  
- `released_day`  

#### Performa Platform Streaming
- `in_spotify_playlists`  
- `in_spotify_charts`  
- `in_apple_playlists`  
- `in_apple_charts`  
- `in_deezer_playlists`  
- `in_deezer_charts`  
- `in_shazam_charts`  

#### Audio Features
- `danceability`  
- `energy`  
- `key`  
- `loudness`  
- `mode`  
- `speechiness`  
- `acousticness`  
- `instrumentalness`  
- `liveness`  
- `valence`  
- `bpm`  

#### Popularity Indicator
- `streams`  

### 🎯 Target
- **Popularitas Lagu**, ditentukan berdasarkan nilai `streams`  
  (misalnya diklasifikasikan menjadi **populer** dan **tidak populer** berdasarkan threshold tertentu)

---
