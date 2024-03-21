# Count reasons for retractions and save as a CSV file

import csv

# Create a dictionary to store the number of retractions by reason
retractions_by_reason = {}

# Open the file
with open('retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Loop through the rows of the file
    for row in reader:
        
        # Get the reasons like "+Concerns/Issues about Referencing/Attributions;+Concerns/Issues with Peer Review;+Investigation by Journal/Publisher;+Rogue Editor;+Unreliable Results;"
        reasons = row['Reason']
        
        if row['RetractionNature'] == 'Retraction':
            # Split the reasons into a list
            reasons = reasons.split(';')
            
            # Loop through the reasons
            for reason in reasons:
                
                # Remove the '+' from the reasons
                reason = reason.replace('+', '')
                
                # Remove the leading and trailing whitespace
                reason = reason.strip()
                
                # If the reason is already in the dictionary, add 1 to the count
                if reason in retractions_by_reason:
                    retractions_by_reason[reason] += 1
                # If the reason is not in the dictionary, set the count to 1
                else:
                    retractions_by_reason[reason] = 1

# Print the dictionary
print(retractions_by_reason)

# Sort dictionary
retractions_by_reason = dict(sorted(retractions_by_reason.items(), key=lambda item: item[1], reverse=True))

# Save as CSV
with open('retractions_by_reason.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Reason', 'Retractions'])
    for reason, retractions in retractions_by_reason.items():
        writer.writerow([reason, retractions])