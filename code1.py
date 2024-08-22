import os
import re
import pandas as pd
from datetime import datetime

# Prompt user for the directory path
dir_path = '/home/saurav/Desktop/Unix_Timestamp'

# Check if the directory exists
if not os.path.isdir(dir_path):
    print("Directory does not exist.")
    exit(1)

# List to store data for the Excel sheet
data = []

# Regular expression to find a 10-digit Unix timestamp in the filename
timestamp_pattern = re.compile(r"\d{13}")

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    if filename.lower().endswith(".mp4"):
        # Search for the Unix timestamp in the filename
        match = timestamp_pattern.findall(filename)
        #print(match)
        if match:
            timestamp1 = int(match[0])
            timestamp2 = int(match[1])
            #print(timestamp)
            # Convert Unix timestamp to human-readable date format
            readable_date1 = datetime.utcfromtimestamp(timestamp1/1000.0).strftime('%Y-%m-%d-%H-%M-%S:%f')
            readable_date2 = datetime.utcfromtimestamp(timestamp2/1000.0).strftime('%Y-%m-%d-%H-%M-%S:%f')
            # Append the data to the list
            data.append([filename, readable_date1[:-3], readable_date2[:-3]])
            print(data)
        else:
            data.append([filename, "No timestamp found"])

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=["filename", "T1(yyyy-mm-dd-hh-mm-ss:mmm)","T2"])

# Define the output Excel file
output_file = "output.xlsx"

# Write the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Results have been saved to {output_file}")

