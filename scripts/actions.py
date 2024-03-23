# Count number of actions - retractions, corrections, expressions of concern, and withdrawals - and save as a CSV file

import csv

# Open the file
with open('raw_data/retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of actions
    actions = {}
    
    # Loop through the rows of the file
    for row in reader:
        # Get the action
        action = row['RetractionNature']
        
        if action in actions:
            actions[action] += 1
        else:
            actions[action] = 1

# Print the dictionary
print(actions)

# Save as CSV
with open('actions.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Action', 'Count'])
    for action, count in actions.items():
        writer.writerow([action, count])