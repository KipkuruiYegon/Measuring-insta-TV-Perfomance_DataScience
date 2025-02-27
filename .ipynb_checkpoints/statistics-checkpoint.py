import pandas as pd
import numpy as np
import warnings
import seaborn as sns
import matplotlib.pyplot as plt

# Load all datasets
comments_df = pd.read_csv("comments.csv")
follows_df = pd.read_csv("follows.csv")
likes_df = pd.read_csv("likes.csv")
photo_tags_df = pd.read_csv("photo_tags.csv")
photos_df = pd.read_csv("photos.csv")
tags_df = pd.read_csv("tags.csv")
users_df = pd.read_csv("users.csv")

# Configure warnings
warnings.simplefilter("ignore", UserWarning)

# Display basic info
dfs = {"Comments": comments_df, "Follows": follows_df, "Likes": likes_df,
       "Photo Tags": photo_tags_df, "Photos": photos_df, "Tags": tags_df, "Users": users_df}

for name, df in dfs.items():
    print(f"{name} Dataset:\n", df.head(), "\n")
