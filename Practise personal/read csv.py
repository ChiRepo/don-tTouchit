import csv
with open('Result.csv','r') as f:
    a=f.readlines()
    print(a)
def wonCount():
    count = 0
    # Open the CSV file for reading
    with open('Result.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Count the number of students who won any event
        for row in reader:
            print("Row:", row)  # Debugging statement
            if row[3] == 'won':
                count += 1
                print("Count incremented. New count:", count)  # Debugging statement

    return count
# Example usage:
print('Number of students who won any event:', wonCount())