import pandas as pd

grades = pd.read_json("grades.json")
new_grades = grades.copy()

# Treat the 'id' column as row labels (index)
new_grades.set_index("id", inplace=True)

# --------------- BEGIN STUDENT CODE --------------- #

# Now it's easy to access rows by id"
new_grades.loc["ssund040", "grade"] = "A"


# ---------------- END STUDENT CODE ---------------- #

# Put the DataFrame back to its original shape
new_grades.reset_index(inplace=True)
new_grades.to_json("new_grades.json", index = False)
new_grades
