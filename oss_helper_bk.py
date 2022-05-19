import oss2
import sys
import time


def now():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def get_file_name(file_path):
    return file_path[file_path.rindex('/') + 1:] if file_path.__contains__('/') else file_path


def gen_oss_file_name(file_path):
    file_name = get_file_name(file_path)
    return now() + file_name[file_name.rindex('.'):]


# args: [oss_helper.py, put, x, y, ...]
args = sys.argv
args_len = len(args)

if args_len < 3:
    print('args error')
    sys.exit(1)

auth = oss2.Auth('x', 'y')
bucket = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'z')

action = args[1]

if action == 'put':
    for num in range(2, args_len):
        file_path = args[num]
        res = bucket.put_object_from_file(gen_oss_file_name(file_path), file_path)
        print(res.resp.response.url.replace('http://', 'https://'))

if action == 'del':
    for num in range(2, args_len):
        res = bucket.delete_object(args[num])
        print(res.resp.response.ok)
