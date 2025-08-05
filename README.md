# DjangoDocker

A simple dockerized Django application for rapid development and deployment using Docker. This project provides a ready-to-use Django setup with Docker, Gunicorn, and MariaDB/MySQL integration, allowing you to quickly launch a Django site with best practices for containerization.

## Features

- Django 3.2.4 running in a Python 3.9 Alpine container
- Gunicorn for robust production-ready serving
- MariaDB/MySQL support via `mysqlclient`
- Automated migrations and static file collection on container startup
- Sample admin interface with static assets and fonts handled via Docker volumes

## Quickstart

### Requirements

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- (Optional) MariaDB/MySQL server if you wish to connect to an external database

### Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/theonlykingpin/DjangoDocker.git
    cd DjangoDocker
    ```

2. **Build and run the container:**
    ```bash
    docker build -t djangodocker ./app
    docker run -p 8000:8000 djangodocker
    ```

3. **Access the application:**
    - Open [http://localhost:8000](http://localhost:8000) in your browser.

## Structure

- `/app/Dockerfile` - The main Dockerfile to build the Django application container.
- `/volumes/static/admin/` - Static files for Django admin, including fonts and images.
- `/volumes/static/admin/fonts/README.txt` - Details on fonts used for the admin interface.
- `/volumes/static/admin/img/README.txt` - Details on icons and images for the admin interface.
- `/volumes/static/admin/js/` - JavaScript files for Django admin utilities.

## Environment Variables

- `DJANGO_SUPERUSER_PASSWORD` - Password for the Django superuser (`admin` by default in the Dockerfile, change for production).
- `PYTHONDONTWRITEBYTECODE`, `PYTHONUNBUFFERED` - Set for best practices in the container.

## Customization

- Modify Django settings and your own apps as needed in the `/app` directory.
- Static files and fonts can be replaced or extended in `/volumes/static/admin/`.

## Licensing

- Font Awesome icons: [SIL OFL 1.1](https://scripts.sil.org/OFL)
- Font-Awesome-SVG-PNG: [MIT License](https://github.com/encharm/Font-Awesome-SVG-PNG)
- Roboto webfont: [Google Fonts](https://www.google.com/fonts/specimen/Roboto)
- All code/assets are distributed under their respective licenses as listed in the `LICENSE` and asset README files.

## Credits

- Docker/Django setup by [theonlykingpin](https://github.com/theonlykingpin)
- Admin assets adapted from Font Awesome and Google Fonts

## Contributing

Feel free to fork and submit pull requests for improvements or new features!

---

**Note:** This project is intended as a template for Dockerized Django apps. Please update environment variables, secrets, and settings before deploying to production.
