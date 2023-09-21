age_in_years = int(input("Enter your age :"))

maximum_heart_rate_in_beats_per_minutes = 220 - age_in_years
print("Your maximum target heart rate is ", maximum_heart_rate_in_beats_per_minutes)
target_heart_rate = int((50/100 * maximum_heart_rate_in_beats_per_minutes) and 85/100 * maximum_heart_rate_in_beats_per_minutes)

if (50/100 * maximum_heart_rate_in_beats_per_minutes) <= target_heart_rate <= (85/100 * maximum_heart_rate_in_beats_per_minutes):
    print("Your heart rate is fine!", ".Your target heart rate is", target_heart_rate)


if target_heart_rate > (0.85 * maximum_heart_rate_in_beats_per_minutes):
    print("Kindly consult your physician!")

if target_heart_rate < (50/100 * maximum_heart_rate_in_beats_per_minutes):
    print("Kindly consult your physician!")




age = int(input("Enter your age:"))
maximum_heart_rate = 220 - age
print("Your maximum target heart rate is ", maximum_heart_rate)
target_heart_rate1 = 50/100 * maximum_heart_rate
target_heart_rate2 = 85/100 * maximum_heart_rate
Range = " "
target_heart_rate1 <= Range <= target_heart_rate2
print(Range)