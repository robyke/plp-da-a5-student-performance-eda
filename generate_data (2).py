
import numpy as np
import pandas as pd

rng = np.random.default_rng(55)

n = 1200

students = pd.DataFrame({
    "student_id": range(1, n + 1),
    "county": rng.choice(
        ["Nairobi", "Kisumu", "Nakuru", "Mombasa", "Nyeri", "Turkana"],
        n
    ),
    "school_type": rng.choice(
        ["Public", "Private"],
        n,
        p=[0.75, 0.25]
    ),
    "gender": rng.choice(
        ["F", "M"],
        n
    ),
    "attendance_rate": rng.beta(
        8,
        2,
        n
    ).round(2),
    "study_hours": rng.gamma(
        2.5,
        2.0,
        n
    ).round(1),
})

base = (
    35
    + 30 * students["attendance_rate"]
    + 2.2 * students["study_hours"]
    + np.where(students["school_type"] == "Private", 6, 0)
)

students["math"] = (
    base + rng.normal(0, 8, n)
).clip(0, 100).round(0)

students["english"] = (
    base + rng.normal(3, 7, n)
).clip(0, 100).round(0)

students["science"] = (
    base + rng.normal(-2, 9, n)
).clip(0, 100).round(0)

students.to_csv(
    "student_performance.csv",
    index=False
)
