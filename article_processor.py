def process_li(article):
    url = ''
    title = ''
    description = ''
    for child in article.children:
        if child.name == 'a':
            url = child['href']
            title = child.text
        elif child.name == 'p':
            description = child.text
    return url, title, description

