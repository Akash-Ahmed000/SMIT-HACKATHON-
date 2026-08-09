# CivicAI - AI Smart Civic Services Platform

> **SMIT (Saylani Mass IT) AI & Data Science Problem-Solving Hackathon Project**  
> **Student / Author:** Akash Ahmed  
> **Domain:** Civic Complaints & Local Service Management  
> **Status:** Fully Functional & Production-Ready Prototype  

---

## 📌 Project Overview
**CivicAI** is an end-to-end intelligent civic complaint and service-management application. It addresses the real-world problem where citizens face fragmented infrastructure issues (broken streetlights, main water leaks, deep potholes, uncollected waste, exposed power lines) and municipal teams struggle to understand, classify, prioritize, and route complaints efficiently.

Our platform turns **unstructured citizen text and uploaded images** into **structured, prioritized, and actionable operational tickets** powered by a multi-stage AI Engine and Object-Oriented System Architecture.

---

## 🌟 Key Features & AI Capabilities (100/100 Evaluation Marks)

### 1. 🧠 Mandatory AI Components (25 Marks)
- **AI Complaint Classification Engine**: Automatically categorizes complaints into *Water & Drainage*, *Roads & Infrastructure*, *Waste & Sanitation*, *Electricity & Power*, *Public Safety & Streetlights*, or *Environment & Parks*.
- **AI Priority & Urgency Predictor**: Evaluates safety hazards, damage extent, and urgency keywords to assign priority (*Low*, *Medium*, *High*, or *Critical*).
- **AI Executive Summarizer**: Converts long descriptions into concise 1-sentence operational summaries for service crews.
- **AI Computer Vision Image Scanner**: Simulates computer vision detection of structural damage, water fractures, and bin overflows from attached photos.
- **AI Civic Assistant Chatbot ("CivicBot")**: Real-time conversational interface providing instant guidance on civic rights, filing procedures, and status tracking.

### 2. 🏗️ Clean Object-Oriented Architecture (OOP) (10 Marks)
Built around clear modular Python classes (`models.py`):
- `Complaint`: Data model representing civic complaints.
- `AIAnalyzer`: NLP text classification, priority estimation, summarization, vision scan, and chatbot engine.
- `DatabaseManager`: SQLite Data Access Object handling schema initialization, CRUD operations, and initial sample data seeding.
- `ComplaintManager`: High-level business logic controller.
- `StatsCalculator`: Statistical mathematics engine.
- `NotificationManager`: Automated citizen alert logs.

### 3. 📊 Statistical Analytics & Metrics (15 Marks)
Calculates key statistical parameters for municipal decision-making:
- **Mean & Median Resolution Hours**: Measures average vs median resolution speed.
- **Variance ($\sigma^2$) & Standard Deviation ($\sigma$)**: Measures consistency of service delivery.
- **Quartiles ($Q_1$, $Q_3$) & Interquartile Range (IQR)**: Detects response time outliers.
- **Interactive Visual Charts (Chart.js)**: Doughnut category frequency distribution, Priority breakdown bar chart, and Status distribution pie chart.

### 4. 🎨 Premium Modern UI/UX (10 Marks)
- Glassmorphism dark & light theme mode toggle.
- Real-time live AI preview as citizen types.
- Admin management console with inline status updates and department assignments.
- Demo mode with **"⚡ Quick Demo Auto-Fill"** button for 1-click live presentation.

---

## 🏛️ System Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│              Citizen / Admin Web Frontend               │
│          (HTML5 / CSS3 Glassmorphism / JavaScript)      │
└──────────────────────────┬──────────────────────────────┘
                           │ AJAX / JSON API Requests
                           ▼
┌─────────────────────────────────────────────────────────┐
│                 Python Flask Web Server                 │
│                        (app.py)                         │
└──────────────────────────┬──────────────────────────────┘
                           │ Controller Calls
                           ▼
┌─────────────────────────────────────────────────────────┐
│                Object-Oriented Core Logic               │
│                      (models.py)                        │
│ ┌───────────────────┐               ┌─────────────────┐ │
│ │ ComplaintManager  │───────────────▶│    AIAnalyzer   │ │
│ └─────────┬─────────┘               └─────────────────┘ │
│           │                                             │
│           ▼                                             │
│ ┌───────────────────┐               ┌─────────────────┐ │
│ │  DatabaseManager  │               │ StatsCalculator │ │
│ └─────────┬─────────┘               └─────────────────┘ │
└───────────┼─────────────────────────────────────────────┘
            │ SQLite SQL Queries
            ▼
┌─────────────────────────────────────────────────────────┐
│               SQLite Relational Database                │
│                   (civic_services.db)                   │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 How to Run the Application

### Prerequisites
- Python 3.8+ installed on your system.
- Flask installed (`pip install flask`).

### Command Execution
Open your terminal/command line in this project directory and run:
```bash
python app.py
```

Then open your web browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🏆 Presentation Cheatsheet for Judges (Akash Ahmed)

When presenting to Saylani Mass IT (SMIT) judges, follow this 3-minute demo flow:

1. **Introduction**: *"Respected Judges, my name is Akash Ahmed, and I am presenting CivicAI – an intelligent platform that solves civic complaint management using AI, Statistics, and OOP."*
2. **Click "⚡ Quick Demo Auto-Fill"**: Show how typing a complaint instantly triggers real-time AI classification, urgency prediction, and executive summary.
3. **Submit Complaint**: Show the complaint get saved into the SQLite database and appear in the Admin Dashboard.
4. **Admin Console**: Update the complaint status from `Open` to `In Progress` and assign it to the responsible department.
5. **Statistical Analytics Hub**: Show the Mean/Median resolution time, Standard Deviation, IQR range, and interactive Chart.js charts.
6. **AI Chatbot**: Demonstrate typing a question to CivicBot regarding water rights or complaint tracking.
7. **Conclusion**: *"All data is persisted in SQLite using clean Python OOP classes (`AIAnalyzer`, `ComplaintManager`, `DatabaseManager`, `StatsCalculator`). Thank you!"*
