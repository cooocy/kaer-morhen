import time
import sys
import oss2


def now():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def get_file_name(file_path):
    return file_path[file_path.rindex('/') + 1:] if file_path.__contains__('/') else file_path


def gen_oss_file_name(file_path):
    file_name = get_file_name(file_path)
    return now() + file_name[file_name.rindex('.'):]


# args: [oss_helper.py, put, x, y, ...]
args = sys.argv
if len(args) < 3:
    print('args error')
    sys.exit(1)

auth = oss2.Auth('x', 'y')
bucket = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'z')

action = args[1]

if action == 'put':
    for num in range(2, len(sys.argv)):
        file_path = sys.argv[num]
        res = bucket.put_object_from_file(gen_oss_file_name(file_path), file_path)
        print(res.resp.response.url.replace('http://', 'https://'))

if action == 'del':
    for num in range(2, len(sys.argv)):
        res = bucket.delete_object(sys.argv[num])
        print(res.resp.response.ok)
