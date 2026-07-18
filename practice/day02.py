# nAndX = input()
# n = int(nAndX.split(" ")[0])
# x = int(nAndX.split(" ")[1])

# mark = []
# for i in range(0, n):
#     mark.append(input().split(" "))
# avg = []
# for i in range(0, x):
#     avgMark = 0.0
#     for j in range(0, n):
#         avgMark += float(mark[j][i])
#     avg.append(avgMark / n)
# print(*avg, sep="\n")


import os

with open("data.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file contains some sample data.\n")
    file.write("End of the file.\n")


try:
    with open("data.txt", "r") as file:
        print(file.read(10))
except Exception as e:
    print(f"Error opening file: {e}")

# if os.path.exists("data.txt"):
#     os.remove("data.txt")
#     print("File deleted successfully.")


# ----------------------------
import json

data = {
    "name": "Abdallah",
    "age": 25,
    "major": "Computer Science",
    "gpa": 94.1,
    "courses": ["Data Structures", "Algorithms", "AI"],
}
a = json.loads(json.dumps(data))
print(a)


with open("data.json", "w") as file:
    print(json.dump(data, file))


x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

print(json.dumps(x, indent=4, separators=("+", " => "), sort_keys=True))
