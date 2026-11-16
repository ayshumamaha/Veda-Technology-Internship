# Build a Data Processing Pipeline Using Python

## 1. Project Description

This project implements a basic data-processing pipeline using Python and Pandas. It reads raw CSV data, identifies and removes duplicate records, handles missing and invalid values, transforms fields, calculates summary statistics, and exports a cleaned dataset.

The pipeline demonstrates the basic stages of a real-world data-processing workflow.

---

## 2. Objectives

- Understand the structure of a data-processing pipeline.
- Read and process raw CSV files.
- Handle missing and invalid values.
- Remove duplicate records.
- Validate numeric and date fields.
- Transform and standardize data.
- Calculate summary metrics.
- Export cleaned data and reports.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and cleaning |
| CSV | Data storage format |

---

## 4. Project Structure

```text
Data-Processing-Pipeline/
│
├── raw_dataset.csv
├── data_processing_pipeline.py
├── cleaned_dataset.csv
├── summary_report.txt
└── data_cleaning_documentation.txt
```

---

## 5. Pipeline Workflow

1. **Data Loading:** Read raw CSV data using Pandas.
2. **Data Cleaning:** Remove duplicate records and handle missing or invalid values.
3. **Data Validation:** Validate numeric fields, dates, age ranges, and salary values.
4. **Data Transformation:** Standardize names and departments and create a salary category.
5. **Summary Generation:** Calculate average age, average salary, minimum salary, maximum salary, and department-wise record counts.
6. **Data Export:** Save the cleaned dataset and generated reports.

---

## 6. Features Implemented

- CSV file reading.
- Missing-value handling.
- Duplicate record removal.
- Numeric data validation.
- Date validation.
- Text standardization.
- Salary categorization.
- Summary statistics generation.
- Cleaned CSV export.
- Data-cleaning documentation.

---

## 7. Installation and Execution

Install the required library:

```bash
pip install pandas
```

Run the program:

```bash
python data_processing_pipeline.py
```

Ensure that `raw_dataset.csv` and the Python script are in the same folder.

---

## 8. Expected Output

The pipeline generates:

- `cleaned_dataset.csv` – contains the cleaned and transformed records.
- `summary_report.txt` – contains calculated summary metrics.
- `data_cleaning_documentation.txt` – describes the cleaning and transformation steps.

The sample dataset contains 11 records. After processing, 1 duplicate record and 6 invalid or incomplete records are removed, leaving 4 valid records.

---

## 9. Conclusion

The project demonstrates how raw CSV data can be converted into a structured and usable dataset through a systematic processing pipeline. It introduces essential data-preprocessing techniques and provides practical experience with Python and Pandas.

## Author
M. Ayshwarya
