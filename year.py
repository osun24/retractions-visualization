# Count retractions by year and save as a CSV file

import csv

# Open the file
with open('retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of retractions by year
    retractions_by_year = {}
    
    # Loop through the rows of the file
    for row in reader:
        
        # Get the year
        year = row['Year']
        
        # If the year is already in the dictionary, add 1 to the count
        if year in retractions_by_year:
            retractions_by_year[year] += 1
        # If the year is not in the dictionary, add it with a count of 1
        else:
            retractions_by_year[year] = 1