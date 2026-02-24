import pandas as pd

grades = pd.read_json("grades.json")
new_grades = grades.copy()

# --------------- BEGIN STUDENT CODE --------------- #


new_grades.loc["glin057","grade"] = "A"
new_grades.loc["Jiaqi","grade"] = "A+"
new_grades.loc["jtram003", "grade"] = "A"
new_grades.loc["flores", "grade"] = "A"
new_grades.loc[new_grades["student_id"] == "bmeft001", "grade"] = A
new_grades.loc["mpenu005","grades"]="A"
new_grades.loc["cluo042","grade"]="A"



# ---------------- END STUDENT CODE ---------------- #

new_grades.to_json("new_grades.json", index = False)
