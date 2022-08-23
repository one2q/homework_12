from flask import Blueprint, render_template, request
from functions import load_from_json, get_user_request_post

POST_PATH = "posts.json"

# Создаем новый блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')  # Вьюшка главной страницы
def main_page():
	return render_template('index.html')


@main_blueprint.route("/post_list", methods=["GET"])  # Вьюшка поиска постов
def page_search():
	user_request = request.args['s']  # Запрос пользователя
	if not user_request:  # Проверяем ввел ли пользователь строку и если нет ничего не происходит
		return render_template('index.html')
	post_list = get_user_request_post(load_from_json(POST_PATH), user_request)
	return render_template('post_list.html', user_request=user_request, post_list=post_list)
