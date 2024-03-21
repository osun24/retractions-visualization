# Sort into ethical issues, data/results reliability, procedural issues, investigation, and other
import pandas as pd

# Define the categories
categories = {
    "ethical": ["Manipulation", "Ethical", "Falsification", "Fraud", "Plagiarism", "False", "False/Forged", "Breach", "Misconduct", "Taken", "Attributions", "Authorship", "Copyright Claims", "Patient Consent"],  
    "investigation": ["Investigation"],
    "journal" : ["Duplication of Article", "Publisher", "Journal", "Publisher/Journal", "Journal/Publisher"],
    "peer review": ["Peer Review"],
    "reliability": ["Randomly", "Data", "Results", "Unreliable", "Error in Data", "Error", "Error in Results", "Image"],
    "paper mill" : ["Paper Mill"],
    "unknown": ["Unknown", "Limited", "Information"]
}

# Load the data
df = pd.read_csv('retractions_by_reason.csv')

# Function to categorize reasons
def categorize_reason(reason):
    for category, keywords in categories.items():
        if any(keyword in reason for keyword in keywords):
            return category
    return "other"

# Apply the function to the 'reason' column
df['category'] = df['Reason'].apply(categorize_reason)

# Save the categorized data to a new CSV file
df.to_csv('retractions_by_category.csv', index=False)