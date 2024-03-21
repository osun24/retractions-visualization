# Analyze retractions.csv and count the number of retractions by country

# Papers with multiple countries are separated by a ; in the country field

import csv

# Open the file
with open('retractions.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to store the number of retractions by country
    retractions_by_country = {}
    
    # Loop through the rows of the file
    for row in reader:
        
        # Split the countries by ;
        countries = row['Country'].split(';')
        
        # Loop through the countries
        for country in countries:
            
            # Remove leading and trailing spaces
            country = country.strip()
            
            # If the country is already in the dictionary, add 1 to the count
            if country in retractions_by_country:
                retractions_by_country[country] += 1
            # If the country is not in the dictionary, add it with a count of 1
            else:
                retractions_by_country[country] = 1
                
# Print the dictionary
print(retractions_by_country)

# Save as CSV
with open('retractions-visualization/retractions_by_country.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Country', 'Retractions'])
    for country, retractions in retractions_by_country.items():
        writer.writerow([country, retractions])