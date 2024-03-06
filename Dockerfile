FROM python:3.12.0 as python-base

ENV PYTHONDONTWRITEBYTECODE = 1 \
    PYTHONUNBUFFERED = 1

WORKDIR /reviro
COPY poetry.lock pyproject.toml /reviro/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

COPY . /reviro/
VOLUME /reviro/media

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" \
    && python manage.py collectstatic --no-input \
    && gunicorn config.wsgi:application --bind 0.0.0.0:8000
#CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000




