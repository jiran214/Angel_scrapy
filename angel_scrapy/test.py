# 打印文档树

import os


def join(path, item):
    if path == '.':
        return item
    return os.path.join(path, item)


def print_file_tree(path='.', level=1):
    items = os.listdir(path)
    for item in items:
        fill_path = join(path, item)
        print('|' * level, '-', item)
        if os.path.isdir(fill_path):
            print_file_tree(fill_path, level + 1)


if __name__ == '__main__':
    print_file_tree()

