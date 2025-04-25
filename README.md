# ACLF Tools

A small collection of Streamlit-based tools for liver-related clinical decision support.

## Included Apps

- **ACLF Classification Tool** (`aclf_app.py`):  
  Classifies patients based on EASL-CLIF criteria with mortality estimates and organ failure explanation.

- **Rotterdam Score for Acute Budd-Chiari Syndrome** (`rotterdam_score_app.py`):  
  Calculates the Rotterdam score using a fixed formula.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run aclf_app.py  # or rotterdam_score_app.py
```

## Deploy on Streamlit Cloud

1. Push this folder to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click "New app", select your repo and script (e.g. `aclf_app.py`).