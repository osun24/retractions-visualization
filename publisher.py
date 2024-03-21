# Retractions by publisher

import csv

# Open the file
with open('retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of retractions by publisher
    retractions_by_publisher = {}
    
    # Loop through the rows of the file
    for row in reader:
        
        if row['RetractionNature'] == 'Retraction':
            # Get the publisher
            publisher = row['Publisher']
            
            if publisher in retractions_by_publisher:
                retractions_by_publisher[publisher] += 1
            else:
                retractions_by_publisher[publisher] = 1
            
# Print the dictionary
print(retractions_by_publisher)

# Sort dictionary
retractions_by_publisher = dict(sorted(retractions_by_publisher.items(), key=lambda item: item[1], reverse=True))

# Save as CSV
with open('retractions_by_publisher.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Publisher', 'Retractions'])
    for publisher, retractions in retractions_by_publisher.items():
        writer.writerow([publisher, retractions])