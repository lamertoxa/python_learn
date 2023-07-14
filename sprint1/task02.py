def filterBible(scripture, book, chapter):
    findVerse = book + chapter
    findedVerseList = []
    for item in scripture:
        if findVerse in item[:len(findVerse)]:
            findedVerseList.append(item)
    return sorted(findedVerseList)

scripture = ["01001001",
             "01001002",
             "01002001",
             "01002002",
             "01002003",
             "02001001",
             "02001002",
             "02001003",
             "66022021"]
book = "01"
chapter = "001"
print(filterBible(scripture,
                  book,
                  chapter))