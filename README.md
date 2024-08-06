# Django CSV Analysis Project

## Overview

This Django project allows users to upload CSV files and perform basic data analysis. It provides a simple web interface for uploading CSV files, which are then processed and stored in the application.

## Features

- Upload CSV files through a web interface.
- Store uploaded CSV files and analyze their contents.
- View and manage uploaded files.

## Requirements

- Python 3.x
- Django 4.x or higher
- pandas seaborn matplotlib

## Installation

1. **Clone the repository:**

   ```bash
   git clone <[repository_url](https://github.com/Dhi90/Django_app_pat.git)>
   ```

2. **Navigate to the project directory:**

   ```bash
   cd <[project_directory](https://github.com/Dhi90/Django_app_pat/tree/main)>
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Update the `settings.py` file:**

   Ensure that the following settings are configured:

   ```python
   # settings.py
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

2. **Add the media URL configuration to `urls.py`:**

   ```python
   # urls.py
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       # Your URL patterns
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

## Usage

1. **Run migrations to set up the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Start the Django development server:**

   ```bash
   python manage.py runserver
   ```

3. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:8000/
   ```

4. **Upload CSV files:**

   - Go to the upload page at `/upload/`.
   - Select a CSV file and click "Upload."

## File Structure

- `csv_analysis/`: Contains the app for CSV analysis, including models, forms, and views.
- `media/`: Directory where uploaded CSV files are stored.
- `static/`: Directory for static files like CSS (make sure static files are properly configured).
- `templates/`: Directory for HTML templates.
- `manage.py`: Django's command-line utility for administrative tasks.

## Troubleshooting

- **Issue with file uploads:** Ensure that the `MEDIA_ROOT` directory exists and has the correct permissions.
- **Static files not loading:** Make sure you have configured `STATIC_URL` and `STATICFILES_DIRS` correctly and run `python manage.py collectstatic` if needed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/en/stable/) for Django features and configurations.
```
