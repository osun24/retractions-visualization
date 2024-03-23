# Sort into ethical issues, data/results reliability, procedural issues, investigation, and other
import pandas as pd
import csv, re

# Define the categories - dictionary is ordered, ranked by importance
categories = {
    "Ethical": ["Manipulation", "Ethical", "Falsification", "Fraud", "Plagiarism", "False", "False/Forged", "Breach", "Misconduct", "Taken", "Attributions", "Authorship", "Copyright Claims", "Patient Consent", "Sabotage", "Lack of Approval", "Lack of IRB/IACUC Approval", "Criminal", "Duplication of", "Conflict of Interest", "Salami Slicing", "Welfare", "Rogue Editor"],  
    "Investigation": ["Investigation"],
    "Contamination": ["Contamination"],
    "Journal Error" : ["Duplication of Article", "Duplicate Publication", "Error by Journal/Publisher", "Miscommunication by Journal/Publisher"],
    "Peer Review": ["Peer Review"],
    "Paper Mill" : ["Paper Mill"],
    "Doing the Right Thing" : ["Doing the Right Thing"],
    "Unknown": ["Unknown", "Limited", "Information", "Unable", "Notice", "Notice – Lack of"],
    "Reliability": ["Bias", "Randomly", "Error in Data", "Falsification/Fabrication", "Results", "Unreliable", "Concerns/Issues About Image", "Error in Image", "Error by Third Party", "Error in Analyses", "Error in Cell Lines/Tissues", "Error in Data", "Contamination", "Materials", "Error in Text", "Methods", "Cites Retracted", "Contamination", "Original Data not Provided", "Sabotage", "Concerns/Issues About Data", "Manipulation", "Peer Review", "Paper Mill", "Hoax Paper", "Retract and Replace", "Updated to Retraction", "False/Forged Authorship"],
}

# Categorize the reason based on the keywords with regex for exact word matching
def categorize_reason(reason):
    reason_lower = reason.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', reason_lower):
                return category
    return "other"

# Check for reliability with whole word matching
def check_for_reliability(reason):
    reason_lower = reason.lower()
    for keyword in categories["Reliability"]:
        if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', reason_lower):
            return True
    return False

# Categorize each retraction by category
# Ensures that a retraction is only counted once in a category but allows for multiple categories

# Read the data
retractions = pd.read_csv('raw_data/retractions.csv', encoding='ISO-8859-1')

# Create a dictionary to store the number of retractions by category
retractions_by_category = {}

# Specific details for each retraction
retractions_with_details = {}

# Loop through the rows of the file
for index, row in retractions.iterrows():
    if row['RetractionNature'] == 'Retraction':
        # Get the reasons like "+Concerns/Issues about Referencing/Attributions;+Concerns/Issues with Peer Review;+Investigation by Journal/Publisher;+Rogue Editor;+Unreliable Results;"
        reasons = row['Reason'].split(';')

        # Prevent duplicate counting
        added_to_categories = []

        # Loop through the reasons
        for reason in reasons:
            # Remove the '+' from the reasons and leading/trailing whitespace
            reason = reason.replace('+', '').strip()

            # Ensure reason is not empty
            if reason == "":
                continue

            category = categorize_reason(reason)
            reliability = check_for_reliability(reason)

            # If the category is unknown and there are other categories, skip
            if category == "unknown" and added_to_categories != []:
                continue
            # If the category is already in the dictionary, add 1 to the count
            elif category in retractions_by_category and category not in added_to_categories:
                retractions_by_category[category] += 1
                added_to_categories.append(category)
            # If the category is not in the dictionary, set the count to 1
            elif category not in added_to_categories:
                retractions_by_category[category] = 1
                added_to_categories.append(category)

            # Separate check for reliability to ensure that a more specific reliability category does not remove from the general reliability category
            if reliability:
                if "Reliability" in retractions_by_category and "Reliability" not in added_to_categories:
                    retractions_by_category["Reliability"] += 1
                    added_to_categories.append("Reliability")
                elif "Reliability" not in added_to_categories:
                    retractions_by_category["Reliability"] = 1
                    added_to_categories.append("Reliability")

        # Store the details for each retraction
        retractions_with_details[row['Record ID']] = {
            'Reason': row['Reason'],
            'Categories': added_to_categories
        }

# Print the dictionary
print(retractions_by_category)

# Print all the reasons that were not categorized
printed_already = []
for index, row in retractions.iterrows():
    if row['RetractionNature'] == 'Retraction':
        reasons = row['Reason']
        reasons = reasons.split(';')
        for reason in reasons:
            reason = reason.replace('+', '')
            reason = reason.strip()
            category = categorize_reason(reason)
            if category == "other" and reason != "" and reason not in printed_already:
                print(reason)
                printed_already.append(reason)

# Sort dictionary
retractions_by_category = dict(sorted(retractions_by_category.items(), key=lambda item: item[1], reverse=True))

# Save as CSV
with open('new_retractions_by_category.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Retractions'])
    for category, retractions in retractions_by_category.items():
        writer.writerow([category, retractions])

# Save the details for each retraction
retractions_with_details_df = pd.DataFrame(retractions_with_details).T

retractions_with_details_df.to_csv('retractions_with_details_on_category.csv')

# Print the details for each retraction
print(retractions_with_details_df)