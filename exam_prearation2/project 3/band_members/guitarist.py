from exam_preparation.project3.band_members.musician import Musician

AVAILABLE_SKILLS = (
    'play metal',
    'play rock',
    'play jazz'
)


class Guitarist(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills = AVAILABLE_SKILLS

