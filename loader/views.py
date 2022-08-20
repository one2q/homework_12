from flask import Blueprint, render_template, request, send_from_directory
from functions import allowed_file, picture_save, add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post")
def page_post():
	return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
	picture = request.files.get('picture')
	content = request.form.get('content')
	if not picture or not content:
		return 'Нет картинки или текста'

	filename = picture.filename
	if not allowed_file(filename):
		return 'Не допустимый формат файла'

	picture_path = picture_save(picture)
	add_post(picture_path, content)
	return render_template('post_uploaded.html', picture=picture_path, content=content)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
	return send_from_directory("uploads", path)
