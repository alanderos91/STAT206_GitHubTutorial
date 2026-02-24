import pandas as pd

grades = pd.read_json("grades.json")
new_grades = grades.copy()

# --------------- BEGIN STUDENT CODE --------------- #


new_grades["grade"] = "A"


# ---------------- END STUDENT CODE ---------------- #

new_grades.to_json("new_grades.json", index = False)
