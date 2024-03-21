# Retractions by subject

import csv

# Open the file
with open('retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of retractions by subject
    retractions_by_subject = {}
    
    # Loop through the rows of the file
    for row in reader:
        
        if row['RetractionNature'] == 'Retraction':
            # Get the subject
            subject = row['Subject']
            
            # Split the subject by semicolon
            subjects = subject.split(';')
            
            for i in range(len(subjects)): subjects[i] = subjects[i].strip()
            
            # Loop through the subjects
            for s in subjects:
                if s in retractions_by_subject:
                    retractions_by_subject[s] += 1
                else:
                    retractions_by_subject[s] = 1
                
# Print the dictionary
print(retractions_by_subject)

# Sort dictionary
retractions_by_subject = dict(sorted(retractions_by_subject.items(), key=lambda item: item[1], reverse=True))

# Save as CSV
with open('retractions_by_subject.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Retractions'])
    for subject, retractions in retractions_by_subject.items():
        writer.writerow([subject, retractions])