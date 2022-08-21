import json
from json import JSONDecodeError


POST_PATH = "posts.json"
ALLOWED_EXTENSIONS = {'png', 'jpeg'}
UPLOAD_FOLDER = "uploads/images"  # Место хранения загружаемых файлов


def load_from_json(filename: str) -> list:
	"""
	Функция загружает данные из json файла
	:param filename: введите имя json файла
	:return: возвращает список словарей
	"""
	with open(filename, 'r', encoding='utf-8') as file:
		data = json.load(file)
		return data


def get_user_request_post(data: list, user_request: str) -> list | bool:
	"""
	Функция ищет совпадение слов в списке постов и возвращает список
	постов с совпадениями либо False
	"""
	result = []
	for i in data:
		if user_request.lower() in i['content'].lower():
			result.append(i)
	if result:
		return result
	return False


def allowed_file(filename: str) -> bool:
	"""
	Функция проверяет допустимость расширения файла
	"""
	return '.' in filename and \
	       filename.split('.', 1)[-1] in ALLOWED_EXTENSIONS


def picture_save(picture) -> str:
	"""
	Функция сохраняет картинку и возвращает путь сохранения
	"""
	filename = picture.filename
	path = f"{UPLOAD_FOLDER}/{filename}"
	picture.save(path)
	return path


def add_post(pic: str, text: str):
	"""
	Функция сохраняет пост в json файл
	"""
	new_post = {'pic': '/'+pic, 'content': text}
	try:
		data = load_from_json('posts.json')
		data.append(new_post)
		with open(POST_PATH, 'w', encoding='utf-8') as file:
			json.dump(data, file, ensure_ascii=False, indent=4)
	except FileNotFoundError:
		print("Файл не найден")
	except JSONDecodeError:
		print("Файл не удается преобразовать")
