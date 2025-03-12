# AI Development Environment

A Django-based development environment for AI applications.

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Create and activate virtual environment:
```bash
python -m venv ai-dev-env
source ai-dev-env/bin/activate  # On Windows use: ai-dev-env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start development server:
```bash
python manage.py runserver
```

## Project Structure

- `ai_dev_env_project/`: Main Django project directory
- `myapp/`: Main application directory
- `RooFlow/`: RooFlow integration

## Features

- Django-based web application
- AI development environment integration
- RooFlow workflow support
- Extensible architecture