"""
将微信读书的书评解析成 markdown.
"""
import json

# 笔记源文件名
src_review = '00_s.ignore'
# 输出的 markdown 文件名
dst_review = '00_d.ignore'

dst_md = ''
with open(src_review, 'r') as f:
    reviews = json.loads(f.read())['reviews']
    reviews.reverse()

    for r in reviews:
        review = r['review']

        review_content = review['content']
        if review_content.endswith('\n'):
            review_content = review_content[:len(review_content) - 1]

        # 4: 全书评, 相当于对这本书的总评
        if 4 == review['type']:
            dst_md = dst_md + '> %s\n\n%s \n' % ('总评', review_content)

        # 1: 针对选中文本的评论
        elif 1 == review['type']:
            chapter_title = review['chapterTitle']
            src_content = '找不到源'
            if 'abstract' in review:
                src_content = review['abstract']
            if src_content.endswith('\n'):
                src_content = src_content[:len(src_content) - 1]
            dst_md = dst_md + '> %s\n> .\n> %s\n\n%s \n\n' % (chapter_title, src_content, review_content)

with open(dst_review, 'w+') as f:
    f.write(dst_md)
