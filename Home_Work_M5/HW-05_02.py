articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    articles_found = []
    for article in articles_dict:
        title = article["title"]
        author = article["author"]
        year = article["year"]
        if letter_case == False:
            title = title.lower()
            author = author.lower()
            key = key.lower()
        else:
            title = title
            author = author
            key = key
        if key in title or key in author:
            articles_found.append({
            "title" : article["title"],
            "author" : article["author"],
            "year" : article["year"]           
            })
                
            print(f'Key is: {key}')
            print(f'Following key has been found: {articles_found}')
    return articles_found

        
    
    
        
    
        
        
        
            
        
        
            
        
        
            
        
        
            
        
            
    