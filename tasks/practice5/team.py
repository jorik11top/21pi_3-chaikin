from typing import Set
from .employee import Employee, Manager
from .exception import NoSuchMemberError


class Team:
    """
    Класс - команда.
    У каждой команды есть менеджер, название и участники.

    Возможности:
    - добавление участников
    - удаление участника из команды
    - просмотр базовой информации об участниках
    - получение списка участников
    """

    name: str
    manager: Manager
    __members: Set[Employee]

    def __init__(self, name: str, manager: Manager):
        """
        Задача:
        Реализовать конструктор класса.
        Конструктор должен присвоить значения публичным атрибутам
        и инициализировать контейнер `__members`
        """
        self.name = name
        self.manager = manager
        self.__members = set()

        # пиши свой код здесь

    def add_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод добавления участника в команду.
        Добавить можно только работника.
        """
        if(isinstance(member,Employee)):
            self.__members.add(member)
        else:
            raise NoSuchMemberError
        # пиши свой код здесь

    def remove_member(self, member: Employee) -> None:
        """
        Задача: реализовать метод удаления участника из команды.
        Если в команде нет такого участника поднимается исключение `NoSuchMemberError`
        """
        # if(isinstance(member,Employee)):
        if(member in self.__members):
            self.__members.remove(member)
        else:
            if(isinstance(member,Employee)):
                raise NoSuchMemberError(self.name,member)
            else:
                raise NoSuchMemberError

        # return None


    def get_members(self) -> Set[Employee]:
        """
        Задача: реализовать метод возвращения списка участков команды та,
        чтобы из вне нельзя было поменять список участников внутри класса
        """
        s = self.__members.copy()
        return s
        # пиши свой код здесь

    def show(self) -> None:
        """
        DO NOT EDIT!
        Данный метод нельзя редактировать!

        Метод показывает информацию о команде в формате:
        `'team: {team_name} manager: {manager_name} number of members: {members_count)}'`

        Задача: доработать класс таким образом, чтобы метод выполнял свою функцию, не меняя содержимое
        этого метода
        """
        print(self)

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для строкового представления объекта.
        """
        return f"team: {self.name} manager: {self.manager.name} number of members: {len(self.__members)}"
    #