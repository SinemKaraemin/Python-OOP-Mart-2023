from exam_preparation.project3.band_members.musician import Musician

AVAILABLE_SKILLS = (
    'sing high pitch notes',
    'sing low pitch notes'
)


class Singer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills = AVAILABLE_SKILLS
