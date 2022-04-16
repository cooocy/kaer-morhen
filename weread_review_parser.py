"""
将微信读书的笔记解析成 markdown.
"""
import json

# 笔记源文件名
src_review = '00.ignore'
# 输出的 markdown 文件名
dst_review = '01.ignore'

dst_md = ''
with open(src_review, 'r') as f:
    reviews = json.loads(f.read())['reviews']
    reviews.reverse()
    for r in reviews:
        review = r['review']
        src_content = '找不到源'
        if 'abstract' in review:
            src_content = review['abstract']
        else:
            src_content = '找不到源'
        if src_content.endswith('\n'):
            src_content = src_content[:len(src_content) - 1]
        review_content = review['content']
        if review_content.endswith('\n'):
            review_content = review_content[:len(review_content) - 1]
        dst_md = dst_md + '> %s\n> .\n> %s\n\n%s \n' % (review['chapterTitle'], src_content, review_content)

dst_file = open(dst_review, 'w+')
dst_file.write(dst_md)
