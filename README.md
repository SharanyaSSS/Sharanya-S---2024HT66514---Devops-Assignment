### DevOps Assignment – Fitness Tracker App

This repository contains a simple Flask-based fitness tracker application developed as part of the 2024HT66514 DevOps assignment. It allows users to log workouts and view them, with additional support for GUI interaction via Tkinter. The project demonstrates best practices in version control, testing, containerization, CI/CD automation, and documentation.

---

### Project Structure

├── ACEest_Fitness.py         # Flask application  
├── gui_app.py                # Optional GUI version using Tkinter  
├── test_app.py               # Pytest unit tests  
├── requirements.txt          # Python dependencies  
├── Dockerfile                # Containerization setup  
├── .github/  
│   └── workflows/  
│       └── ci.yml            # GitHub Actions CI/CD pipeline  
└── README.md                 # Project documentation  


### How to Run the Application Locally

**Prerequisites**  
- Python 3.8+  
- `pip` for installing dependencies  

**Setup Instructions**
```bash
git clone https://github.com/SharanyaSSS/Sharanya-S---2024HT66514---Devops-Assignment.git  
cd Sharanya-S---2024HT66514---Devops-Assignment  
pip install -r requirements.txt  
```

**Run the Flask App**
```bash
python ACEest_Fitness.py  
```

This will start the fitness tracker web app locally. You can log workouts and view them via the browser interface.

---

### How to Run Tests Locally

Unit tests are written using **Pytest**. To execute them:

```bash
pytest test_app.py  
```

This will run all test cases and display results in the terminal.

---

### Docker Containerization

To build and run the application using Docker:

```bash
docker build -t fitness-tracker .  
docker run -p 5000:5000 fitness-tracker  
```

This will expose the Flask app on `localhost:5000`.

---

### GitHub Actions CI/CD Pipeline

This repository includes a CI/CD pipeline configured via **GitHub Actions**:

- Triggered on every push to the `master` branch  
- Automatically installs dependencies  
- Runs Pytest to validate application logic  
- Builds the Docker image to ensure containerization works as expected  

You can view the workflow file at `.github/workflows/ci.yml` and check the **Actions** tab for recent successful runs.

---

### Extra Features

- A GUI version of the app (`gui_app.py`) is included for desktop use  
- All commits follow meaningful naming conventions  
- The repository is public and accessible for review  

---
