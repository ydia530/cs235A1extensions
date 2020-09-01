from typing import List


class Actor:
    def __init__(self, Actor_full_name: str):
        if Actor_full_name == "" or type(Actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = Actor_full_name.strip()
        self.__colleagues: List[Actor] = list()

    @property
    def director_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other,Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self,colleague):
        if isinstance(colleague, Actor):
            self.__colleagues.append(colleague)
            colleague.__colleagues.append(self)


    def check_if_this_actor_worked_with(self, colleague):
        for actor in self.__colleagues:
            if actor == colleague:
                return True
        return False






