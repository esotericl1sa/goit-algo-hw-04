def total_salary(path):
    total = 0
    counter = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                total += float(line.split(",")[-1])
                counter += 1
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "Invalid data in file."

    if counter == 0:
        return "No data to process."
    avg = total / counter
    return total, avg

test_path = "salaries.txt"  # assuming salaries.txt is in the same folder as the script
test_total, test_avg = total_salary(test_path)
print(f"Total salary: {test_total}\nAverage salary: {test_avg}")
