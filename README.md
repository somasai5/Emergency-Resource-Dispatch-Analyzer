# Emergency-Resource-Dispatch-Analyzer
This project is a Python program that classifies resource requests into demand categories, validates them, and applies a personalization rule based on the zone name entered.

## 📌 Features

- Accepts a zone name and resource request inputs
- Classifies requests into:
  - **Low Demand** (1–20)
  - **Moderate Demand** (21–50)
  - **High Demand** (>50)
- Detects **invalid requests** (negative values)
- Handles **zero-demand** separately
- Applies a personalization rule based on zone name length

## 🛠️ How the Program Works

### Step 1 — Input

User provides:
- Zone name
- Number of resources
- Integer resource values

### Step 2 — Classification Rules

| Value | Category |
|------|----------|
| 1–20 | Low Demand |
| 21–50 | Moderate Demand |
| >50 | High Demand |
| 0 | No Demand |
| <0 | Invalid |


### Step 3 — Personalization Logic

Spaces are removed from the zone name.

L = length of zone name 
PLI = L % 4

## 🎯 Personalization Rules

| PLI | Applied Rule |
|-----|--------------|
| 1 | Remove all Low Demand requests |
| 2 | Remove all Moderate Demand requests |
| 3 | Remove all High Demand requests |
| 0 | Remove all Invalid requests |

The number of removed requests is stored as:

personalization = removed count

## 📊 Output Summary

The program displays:

- Demand categories before personalization
- Demand categories after personalization
- Total valid requests
- Total invalid requests
- Total zero-demand requests
- Requests removed due to personalization


## ✅ Example Personalization Details

L value : 17
PLI value : L%4=1
Applied rule : Low Demand removed
## ▶️ How to Run

python filename.py
