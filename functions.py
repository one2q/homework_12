import json

ALLOWED_EXTENSIONS = {'png', 'jpeg'}
UPLOAD_FOLDER = "uploads/images"


def load_from_json(filename: str) -> list:
	with open(filename, 'r', encoding='utf-8') as file:
		data = json.load(file)
		return data


def get_user_request_post(data: list, user_request: str) -> list | bool:
	result = []
	for i in data:
		if user_request.lower() in i['content'].lower():
			result.append(i)
	if result:
		return result
	return False


def allowed_file(filename):
	return '.' in filename and \
	       filename.split('.', 1)[-1] in ALLOWED_EXTENSIONS


def picture_save(picture) -> str:
	filename = picture.filename
	path = f"{UPLOAD_FOLDER}/{filename}"
	picture.save(path)
	return path


def add_post(pic: str, text: str):
	new_post = {'pic': '/'+pic, 'content': text}
	data = load_from_json('posts.json')
	data.append(new_post)
	with open('posts.json', 'w', encoding='utf-8') as file:
		json.dump(data, file, ensure_ascii=False, indent=4)


# add_post('1231', 'sdgsdgag')
