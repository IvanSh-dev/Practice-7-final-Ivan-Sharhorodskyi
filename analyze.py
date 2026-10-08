INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_sum = 0
python_sum = 0
english_sum = 0
student_count = 0
best_student = ""
best_average = -1

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f, None)

    for line in f:
        line = line.strip()

        name, math, python, english = line.split(",")

        math = float(math)
        python = float(python)
        english = float(english)

        math_sum += math
        python_sum += python
        english_sum += english
        student_count += 1
        average = (math + python + english) / 3

        if average > best_average:
            best_average = average
            best_student = name.strip()

result = (
    "Середній бал по класу:\n"
    f"math: {math_sum / student_count:.1f}\n"
    f"python: {python_sum / student_count:.1f}\n"
    f"english: {english_sum / student_count:.1f}\n"
    "\n"
    f"Найкращий студент: {best_student} ({best_average:.1f})\n"
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(result, end="")