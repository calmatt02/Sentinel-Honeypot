import folium

log_file_path = "failed_rdp.log"

# Read the log file and extract latitude, longitude, and description
log_data = []
with open(log_file_path, 'r') as file:
    for line in file:
        entry = {}
        parts = line.strip().split(',')
        for part in parts:
            key_value = part.split(':')
            if len(key_value) == 2:
                key, value = key_value
                entry[key.lower()] = value.strip()

        # Check if all required fields are present
        if 'latitude' in entry and 'longitude' in entry and 'label' in entry:
            try:
                latitude = float(entry['latitude'])
                longitude = float(entry['longitude'])
                description = entry['label']
                log_data.append({'latitude': latitude, 'longitude': longitude, 'description': description})
            except ValueError:
                print(f"Skipping invalid line (ValueError): {line}")
        else:
            print(f"Skipping line with missing required fields: {line}")

# Check if there is at least one entry in the log data
if log_data:
    # Create a folium map centered at the mean of the coordinates
    map_center = [sum(entry['latitude'] for entry in log_data) / len(log_data),
                  sum(entry['longitude'] for entry in log_data) / len(log_data)]

    my_map = folium.Map(location=map_center, zoom_start=4)

    # Add markers to the map for each log entry
    for entry in log_data:
        folium.Marker([entry['latitude'], entry['longitude']], popup=str(entry['description'])).add_to(my_map)

    # Save the map to an HTML file
    my_map.save("log_map.html")
else:
    print("No valid log entries found.")
