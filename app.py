from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

# Импортируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


if __name__ == "__main__":
    app.run()

