import pandas as pd

grades = pd.read_json("grades.json")
new_grades = grades.copy()
new_grades.set_index("id", inplace=True)

# --------------- BEGIN STUDENT CODE --------------- #

new_grades.loc["jong029", "grade"] = "A"
new_grades.loc["glin057","grade"] = "A"
new_grades.loc["jwang1155","grade"] = "A+"
new_grades.loc["jtram003", "grade"] = "A"
new_grades.loc["eflor141", "grade"] = "A"
new_grades.loc["bmeft001", "grade"] = "A"
new_grades.loc["mpenu005","grade"]="A"
new_grades.loc["cluo042","grade"]="A"
new_grades.loc["agarc714", "grade"] = "A"
new_grades.loc["kcald019", "grade"] = "A"
new_grades.loc["anago001", "grade"] = "A"
new_grades.loc["jkaur011", "grade"] = "A"

# ---------------- END STUDENT CODE ---------------- #

new_grades.reset_index(inplace=True)
new_grades.to_json("new_grades.json", index = False)
new_grades
