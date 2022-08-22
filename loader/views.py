from flask import Blueprint, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

# from app import new_logger
from functions import allowed_file, picture_save, add_post

# Создаем новый блюпринт
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post")  # Вьюшка загрузки нового поста
def page_post():
	return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
	picture = request.files.get('picture')
	content = request.form.get('content')
	if not picture or not content:  # Проверка на ввод текста и картинки
		# new_logger.info("Все работает")
		return 'Нет картинки или текста'

	filename = secure_filename(picture.filename)
	if not allowed_file(filename):  # Проверка на допустимость расширения файла
		return 'Не допустимый формат файла'

	picture_path = picture_save(picture)  # Сохраняем картинку и получаем адрес ее хранения
	add_post(picture_path, content)  # Добавляем пост в json файл
	return render_template('post_uploaded.html', picture=picture_path, content=content)


@loader_blueprint.route("/uploads/<path:path>")  # Эта вьюшка для открытия доступа к картинкам
def static_dir(path):
	return send_from_directory("uploads", path)
