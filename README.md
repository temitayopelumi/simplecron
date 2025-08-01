# Cron Parser

A simple **cron expression parser** written in Python.  
It takes a standard cron string (with 5 time fields + command) and expands each field to show the exact values when it will run.

---

## Features

- Parses the standard 5-field cron format:

- Expands wildcards (`*`), ranges (`1-5`), lists (`1,15`), and steps (`*/15`).
- **Minute:** 0–59  
- **Hour:** 0–23  
- **Day of Month:** 1–31  
- **Month:** 1–12  
- **Day of Week:** 0–6 (0 = Sunday)

---

## Installation

To get started with the Cron Parser, follow these steps:

1. **Clone the repository**  
   Download the project files to your local machine using Git:
   ```bash
   git clone https://github.com/yourusername/cron-parser.git
   cd cron-parser
   ```

2. **Create and activate a virtual environment**  
   This helps keep dependencies isolated from your system Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Run the parser or tests**  
   - To use the parser, run:
     ```bash
     python cron_praser.py "<your-cron-string> <your-command>"
     ```
   - To run the test suite:
     ```bash
     python -m unittest
     ```

---
