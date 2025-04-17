import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns

train_path = "image-matching-challenge-2025/train" 
train_labels = pd.read_csv('image-matching-challenge-2025/train_labels.csv')

num_scenes = train_labels["scene"].nunique() # no of unique scenes
scene_counts = train_labels["scene"].value_counts() # no of images per scene
num_datasets = train_labels["dataset"].nunique() # no of datasets
dataset_counts = train_labels["dataset"].value_counts() # no of images per dataset

plt.figure(figsize=(12, 6))
sns.barplot(x=dataset_counts.index, y=dataset_counts.values, palette="viridis")
plt.xlabel("Dataset", fontsize=14)
plt.ylabel("Number of Images", fontsize=14)
plt.title("Number of Images per Dataset", fontsize=16)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# plt.show()


train_thresholds_path = "image-matching-challenge-2025/train_thresholds.csv"
train_thresholds = pd.read_csv(train_thresholds_path)

