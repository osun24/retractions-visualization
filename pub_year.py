# Count retractions by year and save as a CSV file

import csv

# Open the file
with open('retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of retractions by year
    retractions_by_year = {}
    
    # Loop through the rows of the file
    for row in reader:
        # Ensure it is a retraction
        if row['RetractionNature'] == 'Retraction':
            # Get the date like "1/11/24 0:00"
            date = row['OriginalPaperDate']
            
            # Convert the date to a year
            year = date.split('/')[2].split(' ')[0]
            
            if (len(year) > 2):
                year = year
            elif int(year) > 24:
                year = '19' + str(year)
            else:
                year = '20' + str(year)
            
            if year in retractions_by_year:
                retractions_by_year[year] += 1
            else:
                retractions_by_year[year] = 1
        
# Print the dictionary
print(retractions_by_year)

# Sort dictionary by year
retractions_by_year = dict(sorted(retractions_by_year.items(), key=lambda item: item[0]))

# Save as CSV
with open('retractions_by_year_of_pub.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Year Published', 'Retractions'])
    for year, retractions in retractions_by_year.items():
        writer.writerow([year, retractions])