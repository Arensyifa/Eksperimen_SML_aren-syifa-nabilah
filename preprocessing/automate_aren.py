import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

logging.basicConfig(level=logging.INFO)

def load_dataset(path):
    logging.info("Loading dataset...")
    df = pd.read_csv(path)

    # Convert all numeric-like columns
    numeric_cols = [
        'artist_count',
        'in_spotify_playlists', 'in_spotify_charts',
        'streams',
        'in_apple_playlists', 'in_apple_charts',
        'in_deezer_playlists', 'in_deezer_charts',
        'in_shazam_charts',
        'bpm',
        'danceability_%', 'valence_%', 'energy_%',
        'acousticness_%', 'instrumentalness_%',
        'liveness_%', 'speechiness_%'
    ]

    # Convert columns to numeric
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna(subset=numeric_cols)
    logging.info("Converted all numeric columns and removed NA.")
    return df


def create_target(df):
    logging.info("Creating target column based on streams...")
    df['popular'] = df['streams'].apply(lambda x: 1 if x >= 10_000_000 else 0)
    return df


def select_features(df):
    logging.info("Selecting numerical features...")

    features = [
        'artist_count',
        'in_spotify_playlists', 'in_spotify_charts',
        'in_apple_playlists', 'in_apple_charts',
        'in_deezer_playlists', 'in_deezer_charts',
        'in_shazam_charts',
        'bpm',
        'danceability_%', 'valence_%', 'energy_%',
        'acousticness_%', 'instrumentalness_%',
        'liveness_%', 'speechiness_%'
    ]
    X = df[features]
    y = df['popular']
    return X, y, features


def scale_features(X):
    logging.info("Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled


def split_and_save(X, y, features):
    logging.info("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    train_df = pd.DataFrame(X_train, columns=features)
    train_df['popular'] = y_train.values

    test_df = pd.DataFrame(X_test, columns=features)
    test_df['popular'] = y_test.values

    logging.info("Saving final processed datasets...")
    train_df.to_csv("spotify_preprocessed_train.csv", index=False)
    test_df.to_csv("spotify_preprocessed_test.csv", index=False)


def run_all():
    df = load_dataset("spotify_raw/Spotify Most Streamed Songs.csv")  
    df = create_target(df)
    X, y, features = select_features(df)
    X_scaled = scale_features(X)
    split_and_save(X_scaled, y, features)
    logging.info("PREPROCESSING COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    run_all()
