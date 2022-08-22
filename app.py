import logging

from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

new_logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log.txt")

new_logger.addHandler(console_handler)
new_logger.addHandler(file_handler)

# Импортируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


if __name__ == "__main__":
    app.run()

