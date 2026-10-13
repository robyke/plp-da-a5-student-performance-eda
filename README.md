# Student Performance EDA for a County Education Office

## Project Summary

This project performs exploratory data analysis on a synthetic student-performance dataset containing 1,200 learners. The analysis examines data structure, score distributions, relationships between attendance, study hours and performance, school-type differences, county-level risk patterns, and factors associated with stronger academic results.

## How to Run

1. Run `python generate_data.py` to create `student_performance.csv`.
2. Open `student_eda.ipynb` in Google Colab or Jupyter Notebook.
3. Run all cells from top to bottom.
4. The notebook creates the required analysis tables and saves charts inside the `figures/` folder.

## Five Key Insights

1. Higher attendance and more study hours are associated with higher average student scores.
2. Private-school students have higher average scores than public-school students.
3. The school-type gap remains visible within attendance bands, so attendance alone does not explain the difference.
4. The school-type gap also persists across study-hour quartiles, suggesting that study time alone does not fully explain the difference.
5. The proportion of At Risk learners varies by county, which can help guide where learner-support resources should be targeted.

## Outputs

The notebook includes:

- Structure analysis
- Univariate analysis
- Bivariate analysis
- Multivariate analysis
- Hypotheses and interpretation
- Correlation matrix
- School-type gap pivot tables
- Trend line with slope and R²
- Findings, Recommendations and Limitations
- At least three saved PNG charts in the `figures/` folder
