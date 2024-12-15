class Author:
    _authors_table = []
    _id_counter = 1

    def __init__(self, id: int, name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string.")
        
        self._id = id
        self._name = name

        self.__class__._authors_table.append({"id": self._id, "name": self._name})
        self.__class__._id_counter += 1

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @classmethod
    def get_all_authors(cls):
        return cls._authors_table
    
    @property
    def articles(self):
        associated_articles = [article for article in associated_articles._articles_table if article["author_id"] == self._id]
        return associated_articles

    @property
    def magazines(self):
        associated_articles = self.articles
        associated_magazines = []
        for article in associated_articles:
            for magazine in magazine._magazines_table:
                if magazine["id"] == article["magazine_id"]:
                    associated_magazines.append(magazine)
        return associated_magazines

    def __repr__(self):
        return f'<Author {self._name}>'
