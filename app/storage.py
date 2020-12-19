from pathlib import Path
import json
import os

data_file_path:Path = None

def init_data_path(arg_data_file_path:Path):
    global data_file_path
    data_file_path = arg_data_file_path

def get_likes_count_by_post(post_id):
    if not data_file_path:
        raise Exception('You should define data_file_path before')
    likes_by_post = get_likes_by_post()
    result = likes_by_post.get(str(post_id), 0)
    return result

def get_likes_by_post():
    if not os.path.exists(data_file_path):
        return {}

    with open(data_file_path, 'r') as fin:
        content = fin.read()
        try: 
            data = json.loads(content)
            likes_by_post = data.get('likes_by_post', {})
        except:
            likes_by_post = {}
        return likes_by_post

def increase_likes_count_by_post(post_id):
    if not data_file_path:
        raise Exception('You should define data_file_path before')
    current_value = get_likes_count_by_post(post_id)
    next_value = current_value + 1 
    likes_by_post = get_likes_by_post()
    likes_by_post[str(post_id)] = next_value
    full_data = {'likes_by_post': likes_by_post}
    str_data = json.dumps(full_data)
    with open(data_file_path, 'w') as fout:
        fout.write(str_data)
    # fout = open(data_file_path, 'w')
    # fout.write(str_data)
    # # fout.close()
