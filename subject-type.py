# Open retractions_by_subject and get the parentheses to determine the subject

import csv

# Create a dictionary to store the number of retractions by subject
retractions_by_subject = {}

# Open the file
with open('retractions_by_subject.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Loop through the rows of the file
    for row in reader:
        
        # Get the subject like "Physics (General);"
        subject = row['Subject']
        
        # Split the subject into a list
        subject = subject.split(')')
        
        subjectType = subject[0].replace("(", "").strip()
        
        if subjectType in retractions_by_subject:
            retractions_by_subject[subjectType] += int(row['Retractions'])
        else:
            retractions_by_subject[subjectType] = int(row['Retractions'])
                
# Sort dictionary
retractions_by_subject = dict(sorted(retractions_by_subject.items(), key=lambda item: item[1], reverse=True))

# Print and save
print(retractions_by_subject)

with open('subjectAreas.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Retractions'])
    for subject, retractions in retractions_by_subject.items():
        writer.writerow([subject, retractions])