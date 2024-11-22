def parse_azimuth(azimuth):
    direction = azimuth[0]
    angle = int(azimuth[1:-1])
    rotation = azimuth[-1]

    # Normalize the angle based on the starting direction and rotation
    if direction == 'N':
        if rotation == 'E':
            normalized_angle = (angle % 360)
        elif rotation == 'W':
            normalized_angle = (360 - angle) % 360
    elif direction == 'S':
        if rotation == 'E':
            normalized_angle = (180 + angle) % 360
        elif rotation == 'W':
            normalized_angle = (180 - angle) % 360
    elif direction == 'E':
        if rotation == 'N':
            normalized_angle = (90 - angle) % 360
        elif rotation == 'S':
            normalized_angle = (90 + angle) % 360
    elif direction == 'W':
        if rotation == 'N':
            normalized_angle = (270 + angle) % 360
        elif rotation == 'S':
            normalized_angle = (270 - angle) % 360
    
    return normalized_angle

K = int(input().strip())
recordings = input().strip().split()

frequency = {}
last_position = {}

# Count frequencies and last positions
for index, azimuth in enumerate(recordings):
    normalized_angle = parse_azimuth(azimuth)
    
    if normalized_angle not in frequency:
        frequency[normalized_angle] = 0
    frequency[normalized_angle] += 1
    last_position[normalized_angle] = index + 1  # Store 1-based index

# Determine the azimuth with the highest frequency and lowest angle
max_count = max(frequency.values())
candidate_angles = [angle for angle, count in frequency.items() if count == max_count]

# If there are multiple candidates, choose the smallest angle
chosen_angle = min(candidate_angles)

# Get the last position of the chosen angle
result_position = last_position[chosen_angle]

print(result_position)
