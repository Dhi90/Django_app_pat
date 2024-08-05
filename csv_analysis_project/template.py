import os
from pathlib import Path

# List of files and directories to create
files_and_directories = [
    "csv_analysis_project/csv_analysis_project/__init__.py",
    "csv_analysis_project/csv_analysis_project/settings.py",
    "csv_analysis_project/csv_analysis_project/urls.py",
    "csv_analysis_project/csv_analysis_project/wsgi.py",
    "csv_analysis_project/csv_analysis_project/asgi.py",
    "csv_analysis_project/manage.py",
    "csv_analysis_project/README.md",
    "csv_analysis_project/requirements.txt",
    "csv_analysis_project/sample.csv",
    "csv_analysis_project/csv_analysis/__init__.py",
    "csv_analysis_project/csv_analysis/admin.py",
    "csv_analysis_project/csv_analysis/apps.py",
    "csv_analysis_project/csv_analysis/forms.py",
    "csv_analysis_project/csv_analysis/models.py",
    "csv_analysis_project/csv_analysis/tests.py",
    "csv_analysis_project/csv_analysis/views.py",
    "csv_analysis_project/csv_analysis/urls.py",
    "csv_analysis_project/csv_analysis/templates/csv_analysis/upload.html",
    "csv_analysis_project/csv_analysis/templates/csv_analysis/result.html",
    "csv_analysis_project/csv_analysis/migrations/"
]

# Create files and directories
for item in files_and_directories:
    if item.endswith(".py") or item.endswith(".md") or item.endswith(".txt") or item.endswith(".csv") or item.endswith(".html"):  # Check if it's a file
        Path(item).parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if they don't exist
        with open(item, "w") as f:
            pass  # Create empty file
    else:
        os.makedirs(item, exist_ok=True)  # Create directory

print("Project setup complete. Navigate to the project directory and add your content.")
