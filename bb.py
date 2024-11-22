K = int(input())
A = input().split()

counts = {}
first_occurrence = {}
angles = []

# Map starting letters to initial angles
direction_angles = {'N': 0, 'E': 90, 'S': 180, 'W': 270}

# Map pairs of starting and ending letters to measurement direction
direction_map = {
    ('N', 'E'): 1,
    ('N', 'W'): -1,
    ('S', 'W'): 1,
    ('S', 'E'): -1,
    ('E', 'S'): 1,
    ('E', 'N'): -1,
    ('W', 'N'): 1,
    ('W', 'S'): -1
}

# Valid ending letters for each starting letter
valid_endings = {
    'N': ['E', 'W'],
    'S': ['E', 'W'],
    'E': ['N', 'S'],
    'W': ['N', 'S']
}

for idx, reading in enumerate(A):
    L1 = reading[0]
    L2 = reading[-1]
    angle_str = reading[1:-1]

    θ1 = int(angle_str)

    # Validate starting and ending letters
    if L2 not in valid_endings[L1]:
        continue  # Skip invalid readings

    # Determine measurement direction
    direction = direction_map[(L1, L2)]

    θ0 = direction_angles[L1]
    if direction == 1:
        θ = (θ0 + θ1) % 360
    else:
        θ = (θ0 - θ1) % 360

    # Record the count and first occurrence
    if θ not in counts:
        counts[θ] = 1
        first_occurrence[θ] = idx + 1  # Indexing starts from 1
    else:
        counts[θ] += 1

# Find the angle(s) with maximum frequency
max_count = max(counts.values())
max_angles = [angle for angle, count in counts.items() if count == max_count]

# Select the angle with the smallest value (from North clockwise)
min_angle = min(max_angles)

# Output the earliest occurrence of this angle
print(first_occurrence[min_angle])