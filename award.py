# Ask for times in each event
swimming_time = float(input("Enter swimming time in minutes: "))
cycling_time = float(input("Enter cycling time in minutes: "))
running_time = float(input("Enter running time in minutes: "))

# Calculate total time
total_times = swimming_time + cycling_time + running_time

# Determine the award based on total time
if total_times <= 100:
    award = "Provincial Colours"
elif 101 <= total_times <= 105: # checks if total_time is between 101 and 105 minutes .
    award = "Provincial Half Colours"
elif 106 <= total_times <= 110: # checks if total_time is between 106 and 110 minutes .
    award = "Provincial Scroll"
else:
    award = "No award"


# Display the total time and award
print(f"Total time: {total_times} minutes")
print(f"Award: {award}")
