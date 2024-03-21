# Open retractions_by_category.csv and calculate the number of retractions by category. 

import csv

# Open the file
with open('retractions_by_category.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of retractions by category
    retractions_by_category = {}
    
    # Loop through the rows of the file and count number of retractions per category
    for row in reader:
        category = row['category']
        retractions = row['Retractions']
        if category in retractions_by_category:
            retractions_by_category[category] += int(retractions)
        else:
            retractions_by_category[category] = int(retractions)
                
# Sort
retractions_by_category = dict(sorted(retractions_by_category.items(), key=lambda item: item[1], reverse=True))

# Print the dictionary
print(retractions_by_category)

# Save as CSV
with open('categories.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Retractions'])
    for category, retractions in retractions_by_category.items():
        writer.writerow([category, retractions])