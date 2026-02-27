Business Problem

A travel company wants to classify customers into segments
and estimate expected revenue based on booking behavior.

Hotel Customer Estimator

This project builds a **rule-based customer segmentation and price estimation system**
using hotel sales data using Python and Pandas.

---

Project Overview

The aim of this project is to estimate expected customer value by creating
persona-based customer segments.

Customers are grouped based on:

- City
- Hotel Concept
- Season

Then segmented into price levels using quartile segmentation.

---

Methodology

Data Understanding
- Dataset inspection
- Data types analysis
- Missing value check

Feature Engineering
- Early Booking Score (`EB_Score`)
- Persona generation (`sales_level_based`)

Aggregation
Average prices calculated by:
SaleCityName + ConceptName + Seasons

Segmentation
Customers segmented using:
pd.qcut()


Segments:
- **A** → Highest value customers
- **B**
- **C**
- **D** → Lowest value customers

---

Example Persona
ANTALYA_HERŞEY DAHIL_HIGH


System estimates:
- Customer segment
- Expected average price

---

Technologies

- Python
- Pandas
- NumPy

---

How to Run

```bash
pip install pandas numpy openpyxl

Run the Python script:
hotel_customer_estimator.py


Key Skills Demonstrated

- Customer Segmentation
- Feature Engineering
- Data Aggregation
- Rule-Based Prediction
- Business Analytics Thinking
