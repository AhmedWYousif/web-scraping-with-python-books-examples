
with open('example.html') as infile:
    soup = BeautifulSoup(infile , 'html.parser')


    links = soup.find_all('a', href=True)
    for link in links:
        print(link['href'])
    
    images = soup.find_all('img', src=True)

    p = soup.find('p', id='first')
    p = soup.find_all('p', class_='paragraph')

    # all image tags that display GIF files.
    gif_images = soup.find('img', src=re.compile('\.gif$'))

    p = soup.find_all('p', text='paragraph')
    p = soup.find_all('p', text=re.compile('paragraph'))

    # search for all tags that start with an h.
    for tag in soup.find_all(re.compile('h')):
        print(tag.name)
    
    # find all tags that contain the text “paragraph.”
    soup.find_all(True, text=re.compile('paragraph'))

    # insert the new tag, h2, into the soup at first place.
    h2 = soup.new_tag('h2')
    h2.string = 'This is a second-level header'
    soup.insert(0, h2)

    # appends the new tag at the end of the tag.
    soup.append(soup.new_tag('p'))

    # change the contents of paragraphs to be bold
    for p in soup.find_all('p', text=True):
        p.string.wrap(soup.new_tag('b'))

    # retain the contents, you can use the unwrap function.
    soup = BeautifulSoup('<p> This is a <b>new</b> paragraph!</p>')
    p = soup.p.b.unwrap()
    print(soup.p)

    # changes (or adds) the class withid to all tags that have an id attribute.
    for t in soup.findAll(True, id=True):
        t['class'] = 'withid'
        print(t)
     
    
    # extract() removes the tag from the tree and returns it, so you can use it in the future or add it to the HTML content at a different position.
    # decompose() deletes the selected tag permanently. No return values, no later usage; it is gone forever.
    print(soup.title.extract())
    print(soup.head)
    # <title>Your Title Here</title>
    # <head> </head>

    print(soup.title.decompose())
    print(soup.head)
    # None
    # <head> </head>

    # remove this display attribute from each tag
    for tag in soup.find_all(True, display=True):
        del tag['display']

    # finds and prints contents of all comments
    import Comments from the bs4
    for comment in soup.find_all(text=lambda text:isinstance(text, Comment)):
        print(comment)

    # Converting a Soup to HTML Text
    print(soup.find('p').prettify())