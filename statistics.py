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


# Standardize column names across datasets
comments_df.rename(columns={'User id': 'user_id', 'Photo id': 'photo_id', 'created Timestamp': 'created_at'}, inplace=True)
likes_df.rename(columns={'user': 'user_id', 'photo': 'photo_id', 'created time': 'created_at'}, inplace=True)
users_df.rename(columns={'created time': 'created_at', 'private/public': 'account_status'}, inplace=True)
follows_df.rename(columns={'follower': 'follower_id', 'followee': 'followee_id', 'created time': 'created_at'}, inplace=True)
photo_tags_df.rename(columns={'user id': 'user_id'}, inplace=True)
photos_df.rename(columns={'user ID': 'user_id', 'created dat': 'created_at'}, inplace=True)

# Convert 'created_at' columns to datetime format (with dayfirst=True)
date_columns = ['created_at']
for df in [comments_df, follows_df, likes_df, photos_df, users_df]:
    df[date_columns] = df[date_columns].apply(lambda x: pd.to_datetime(x, errors='coerce', dayfirst=True))

print("\n✅ Date Parsing Completed without Warnings!")


# Check for missing values
for name, df in datasets.items():
    print(f"\n🔍 {name} Missing Values:\n{df.isnull().sum()}")

# Drop duplicates
for name, df in datasets.items():
    datasets[name] = df.drop_duplicates()

# Fill missing values
users_df.fillna({"account_status": "public", "post count": 0, "Verified status": "no"}, inplace=True)
comments_df.fillna({"comment": "No comment"}, inplace=True)

print("\n✅ Data Cleaning Completed!")


# Extract monthly signups
users_df['signup_month'] = users_df['created_at'].dt.to_period('M')

# Plot signups over time
plt.figure(figsize=(12, 5))
sns.countplot(x=users_df['signup_month'].astype(str), order=sorted(users_df['signup_month'].astype(str).unique()))
plt.xticks(rotation=45)
plt.title("Monthly User Signups on IGTV")
plt.xlabel("Month")
plt.ylabel("Number of Signups")
plt.show()


plt.figure(figsize=(12, 5))
sns.histplot(likes_df['photo_id'], bins=50, kde=True, color='blue', label='Likes')
sns.histplot(comments_df['photo_id'], bins=50, kde=True, color='red', label='Comments', alpha=0.6)
plt.legend()
plt.title("IGTV Engagement: Likes vs Comments")
plt.xlabel("Post ID")
plt.ylabel("Frequency")
plt.show()
