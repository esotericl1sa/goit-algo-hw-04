def get_cats_info(path):
    total_cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                temp = line.split(",")
                # create a new dictionary for each cat
                cat = {
                    "id": temp[0],
                    "name": temp[1],
                    "age": temp[2]
                }
                total_cats.append(cat)
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "Invalid data in file."

    return total_cats

test_path = "cats.txt"  # assuming cats.txt is in the same folder as the script
test_dict = get_cats_info(test_path)
print(test_dict)
