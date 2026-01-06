# IT Technical Support Performance Dashboard (Dash + Plotly)

An interactive dashboard built in **Python** using **Dash** and **Plotly** to analyze IT technical support performance across offices, time periods, and technical problem categories.

This project visualizes operational ticket data (from `Bogdan.xlsx`) and provides KPI summaries, interactive filtering, and SLA compliance insights.

---

## Key Features

- **Time-based analysis:** response time and resolution time trends across months and offices  
- **Problem-based analysis:** workload and resolution impact by technical problem type and office  
- **SLA & efficiency page:** additional KPIs and charts focused on compliance and workload severity  
- **Interactive filters:** user-driven analysis through dropdown filters  
- **Clean modular structure:** separate `layouts`, `callbacks`, and `charts` folders

---

## Screenshots

### Home Page
![Home](screenshots/home.png)

### Time Analysis
![Time Analysis](screenshots/time_analysis.png)

### Problem Analysis
![Problem Analysis](screenshots/problem_analysis.png)

### SLA & Efficiency
![SLA](screenshots/sla.png)

---

## Tech Stack

- Python
- Dash
- Plotly
- Pandas
- OpenPyXL (Excel reading)

---

## ▶️ How to Run Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt

2.	Run the app: 
    python app.py

3. Open in your browser: 
    http://127.0.0.1:8050

---

## Project Structure

```text
app.py                  # Main Dash application entry point
codes/                  # Modular application logic
│   ├── callbacks/       # Dash callbacks for interactivity
│   ├── charts/          # Plotly chart definitions
│   ├── layouts/         # Page layouts and UI components
│   ├── data_loader.py   # Data loading and preprocessing
│   ├── kpis.py          # KPI calculation logic
│   └── config.py        # Styling and configuration constants
assets/                 # CSS styling for the dashboard
data/                   # Dataset and data manipulation scripts
screenshots/             # Dashboard screenshots for documentation
requirements.txt         # Python dependencies
README.md                # Project overview and instructions
Final_Report_Paul_Irigi.docx  # Final project documentation
```
---

## Author
**Paul Mathews Irigi**  
Purdue University Northwest  
ITS 46600 – Data Visualization Technology  