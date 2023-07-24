# -*- coding: utf-8 -*-
"""data_viz_using pie and line bars.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SFF_fQbvMfpdAru1UMxyPkyM6LajbcY3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

dataset=pd.read_csv('w.csv')
dataset.head(10)

dataset.describe()

dataset.info()

#sort and remove dublicates

dataset.sort_values('Title',inplace=True)
dataset.drop_duplicates(keep = 'first',inplace=True )

dataset.head(10)

#to see how many deleted

dataset.describe()

#to see how many each company offers jobs


numbofjobs=dataset['Company'].value_counts().head(5)
print(numbofjobs)

#pie chart
labels1=list(numbofjobs.keys()) #.keys get the name of each company
plt.pie(numbofjobs,labels= labels1)
plt.show()

#line bar

jobs=dataset['Title'].value_counts().head(5)
print(numbofjobs)
joblabels=list(numbofjobs.keys()) #.keys get the name of each company
plt.bar(joblabels,jobs,width=.50)

#line bar manpulation of font size

jobs=dataset['Title'].value_counts().head(5)
print(numbofjobs)
joblabels=list(numbofjobs.keys()) #.keys get the name of each company
plt.bar(joblabels,jobs,width=.50)
# Set the font size for the x-axis tick labels
plt.xticks(fontsize=6)  # Adjust the value as needed

# Optionally, set the font size for the y-axis tick labels
plt.yticks(fontsize=6)  # Adjust the value as needed

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Smaller Tick Labels')

# Display the plot
plt.show()

plt.show()

plt.bar(joblabels,jobs,width=.50)

# Set the font size for the x-axis and y-axis labels
plt.xlabel('Categories', fontsize=10)  # Adjust the value as needed
plt.ylabel('Values', fontsize=10)      # Adjust the value as needed

# Set the font size for the x-axis and y-axis tick labels
plt.xticks(fontsize=8)  # Adjust the value as needed
plt.yticks(fontsize=8)  # Adjust the value as needed

# Truncate x-labels to the first 10 characters
truncated_joblabels = [label[:10] for label in joblabels]

# Set the new tick labels with vertical alignment
plt.xticks(range(len(truncated_joblabels)), truncated_joblabels, rotation='vertical')

# Add bar labels (optional)
for index, jobs in enumerate(jobs):
    plt.text(index, jobs, str(jobs), ha='center', va='bottom', fontsize=8)  # Adjust the value as needed

# Add title
plt.title('Bar Chart with Vertical Text for X-Labels')

# Display the plot
plt.show()

#most popular area
area = dataset['Location'].value_counts().head()
labels1=list(area.keys())
plt.bar(labels1,area)
print(area)

#most wanted skills
skills=dataset['Skills'].value_counts().head()
label=list(skills.keys())
plt.pie(skills,labels=label)

#see the total skills wanted

from collections import Counter
dataset.sort_values('Skills',inplace=True)

skills_list = dataset['Skills'].str.split(',').sum()

# Count the occurrences of each skill
skill_counts = Counter(skills_list)

# Sort the skills by their counts in descending order
sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)

# Print the skills and their counts
for skill, count in sorted_skills:
    print(f"{skill}: {count} times")









