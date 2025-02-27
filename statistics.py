import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
comments_df = pd.read_csv("comments.csv")
follows_df = pd.read_csv("follows.csv")
likes_df = pd.read_csv("likes.csv")
photo_tags_df = pd.read_csv("photo_tags.csv")
photos_df = pd.read_csv("photos.csv")
tags_df = pd.read_csv("tags.csv")
users_df = pd.read_csv("users.csv")

# Display the first few rows of each dataset
datasets = {
    "Comments": comments_df,
    "Follows": follows_df,
    "Likes": likes_df,
    "Photo Tags": photo_tags_df,
    "Photos": photos_df,
    "Tags": tags_df,
    "Users": users_df
}

for name, df in datasets.items():
    print(f"Dataset: {name}")
    display(df.head())
    print("\n")


# Check for missing values
for name, df in datasets.items():
    print(f"{name} Missing Values:\n{df.isnull().sum()}\n")

# Check for duplicates
for name, df in datasets.items():
    print(f"{name} Duplicates: {df.duplicated().sum()}\n")

# Drop duplicates if any exist
for name, df in datasets.items():
    datasets[name] = df.drop_duplicates()

# Fill missing values with appropriate defaults
users_df.fillna({"bio": "No bio", "profile_picture": "default.jpg"}, inplace=True)
comments_df.fillna({"text": "No comment"}, inplace=True)

# Monthly User SignUps BarChart
users_df['signup_date'] = pd.to_datetime(users_df['created time'])
users_df['signup_month'] = users_df['signup_date'].dt.to_period('M')

plt.figure(figsize=(12, 5))
sns.countplot(x=users_df['signup_month'].astype(str), order=sorted(users_df['signup_month'].astype(str).unique()))
plt.xticks(rotation=45)
plt.title("Monthly User Signups on IGTV")
plt.xlabel("Month")
plt.ylabel("Number of Signups")
plt.show()
