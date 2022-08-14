import json
from class_candidate import Candidate

def load_candidates(path):
    """
    :param path: json файл
    :return: список объектов класса Candidate
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    list_of_candidates = []
    for i in data:
        man = Candidate(i["id"], i["name"], i["picture"], i["position"], i["gender"], i["age"], i["skills"])
        list_of_candidates.append(man)

    return list_of_candidates

def get_candidate(candidate_id, data):
    """
    Возвращает по id объект класса Candidate
    :param candidate_id: вводимый идентификатор кандидата
    :param data: список объектов класса Candidate
    :return: карточка кандидата
    """
    for i in data:
        if i.id == candidate_id:
            return i

def get_candidates_by_name(candidate_name, data):
    """
    Возвращает по вводимому имени объект класса Candidate
    :param candidate_name: вводимое имя кандидата
    :param data: список объектов класса Candidate
    :return: карточка кандидата
    """
    names = []
    for i in data:
        if candidate_name.lower() in i.name.lower():
            names.append(i)
    return names

def get_candidates_by_skill(skill_name, data):
    """
    Возвращает по вводимому скиллу карточки кандидатов, которые им обладают
    :param skill_name: вводимое название скилла
    :param data: список объектов класса Candidate
    :return: карточки кандидатов
    """
    skills = []
    for i in data:
        if skill_name.lower() in i.skills.lower():
            skills.append(i)
    return skills
