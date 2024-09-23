import pandas as pd

data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'bedrooms': [3, 5, 4, 6, 2],
    'area': [1200, 2500, 1800, 3500, 1400],
    'listing_price': [450000, 1200000, 850000, 950000, 600000]
}

property_data = pd.DataFrame(data)

average_price_by_location = property_data.groupby('location')['listing_price'].mean()

properties_more_than_four_bedrooms = len(property_data[property_data['bedrooms'] > 4])

largest_area_property = property_data.loc[property_data['area'].idxmax()]

print("Average listing price by location:")
print(average_price_by_location)

print(f"\nNumber of properties with more than four bedrooms: {properties_more_than_four_bedrooms}")

print("\nProperty with the largest area:")
print(largest_area_property)
