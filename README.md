# Eksperimen_SML_aren-syifa-nabilah

## Informasi Mahasiswa
- **Nama**: Aren Syifa Nabilah
- **Proyek**: Proyek Akhir – Membangun Sistem Machine Learning  
- **Kelas**: Membangun Sistem Machine Learning (MSML)  

## Deskripsi Proyek
Repository ini berisi eksperimen preprocessing dan persiapan data untuk proyek machine learning dengan tujuan **memprediksi apakah sebuah lagu akan menjadi populer** berdasarkan **fitur audio dan metadata lagu Spotify**.

## Dataset
- **Nama Dataset**: Spotify Most Streamed Songs  
- **Format**: CSV  
- **Sumber**: Kaggle

Dataset ini berisi informasi lagu-lagu yang paling sering diputar di Spotify beserta karakteristik audio dan performa chart-nya.

### Sumber Dataset:  
[Spotify Most Streamed Songs – Kaggle]([https://www.kaggle.com/](https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs))

---

### Informasi Dataset (Daftar Fitur)
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
- `tempo`  

#### Popularity Indicator
- `streams`  

### 🎯 Target
- **Popularitas Lagu**, ditentukan berdasarkan nilai `streams`  
  (misalnya diklasifikasikan menjadi **populer** dan **tidak populer** berdasarkan threshold tertentu)

---
