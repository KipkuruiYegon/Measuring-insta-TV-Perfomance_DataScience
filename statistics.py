# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Enable inline plotting
%matplotlib inline

# Load datasets
comments_df = pd.read_csv("comments.csv")
follows_df = pd.read_csv("follows.csv")
likes_df = pd.read_csv("likes.csv")
photo_tags_df = pd.read_csv("photo_tags.csv")
photos_df = pd.read_csv("photos.csv")
tags_df = pd.read_csv("tags.csv")
users_df = pd.read_csv("users.csv")

# Store datasets in a dictionary for easy access
datasets = {
    "Comments": comments_df,
    "Follows": follows_df,
    "Likes": likes_df,
    "Photo Tags": photo_tags_df,
    "Photos": photos_df,
    "Tags": tags_df,
    "Users": users_df
}

# Display the first few rows of each dataset
for name, df in datasets.items():
    print(f"\n📊 Dataset: {name}")
    display(df.head())  # Use display() in Jupyter to render DataFrames properly
