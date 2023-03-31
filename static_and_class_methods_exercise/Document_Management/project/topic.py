class Topic:
    def __init__(self, id: int, topic: str, storage_folder: str):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    @classmethod
    def edit(cls, new_topic: str, new_storage_folder: str):
        cls.topic = new_topic
        cls.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
