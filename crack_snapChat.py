# Nested loops to generate 4-digit combinations
for i in range(10):  # First digit loop (0 to 9)
    for j in range(10):  # Second digit loop (0 to 9)
        for k in range(10):  # Third digit loop (0 to 9)
            for l in range(10):  # Fourth digit loop (0 to 9)
                combination = f'{i:02}{j:02}{k:02}{l:02}'  # Format digits to 2 digits with leading zeros if necessary
                print(combination)  # Print the generated combination

