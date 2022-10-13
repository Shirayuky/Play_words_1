import json
import sys


stud_path = 'students.json'
prof_path = 'professions.json'

list_stud_name = []  # имена студентов
list_prof_title = []  # названия специальностей

list_stud_skills = []  # навыки студентов
list_prof_skills = []  # инфа о специальностях


# Students list
def load_students():
    """
    Загружает студентов из файла в список
    """
    with open(stud_path) as file:
        json_stud_file = list(json.load(file))

        for f in json_stud_file:
            full_name_path = f['full_name']
            list_stud_name.append(full_name_path)

        return list_stud_name


# Professions list
def load_professions():
    """
    Загружает навыки из файла в список
    """
    with open(prof_path) as file:
        json_prof_file = json.load(file)

        for f in json_prof_file:
            title_path = f['title']
            list_prof_title.append(title_path)

        return list_prof_title  # возвращает названия профессий


# Students skills
def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    """
    with open(stud_path) as file:
        json_prof_file = json.load(file)

        for inf in json_prof_file:
            stud_skills_path = inf['skills']
            if pk == inf['pk']:
                for skills in stud_skills_path:
                    list_stud_skills.append(skills)

                return list_stud_skills


# Professions skills
def get_profession_by_title(title):
    """
    Получает словарь с инфо о профессии по названию
    """
    with open(prof_path) as file:
        json_prof_file = json.load(file)

        for f in json_prof_file:
            prof_skills_path = f['skills']
            if title == f['title']:
                for inf in prof_skills_path:
                    list_prof_skills.append(inf)

                return list_prof_skills  # возвращает инф о специальностях по названию проф


# Fit percent
def check_fitness(student, profession):
    """
    Оценка студента
    """
    # 1. Что он знает из профессии - ПЕРЕСЕЧЕНИЕ - st.intersection(prof)
    # 2. Чего не знает из профессии - ВЫЧИТАНИЕ - prof.difference(st)
    # 3. Процент пригодности по профессии - if prof.issubset(st) != True, то ((a / 0.1) / b) / 0.1

    set_student = set(student) # set для дальнейшей работы
    set_profession = set(profession) # set для дальнейшей работы

    # Пересечение
    has_list = list(set_student.intersection(set_profession))

    # Вычитание
    lacks_list = list(set_profession.difference(set_student))

    # Процент пригодности
    fit_percent_list = len(has_list) / len (set_profession)

    total_percent = round(fit_percent_list*100)

    set_data = dict(has=has_list, lacks=lacks_list, fit_percent=total_percent)
    for k, v in set_data.items():
        if type(v) == list:
            v = ', '.join(v)

        print(f'{k}: {v}')

    return set_data


# Welcome
print('Добро пожаловать в наше консольное hh.ru!\n'
      'Мы только на стадии развития и, в принципе, планируем в ней остаться ;)')

user_pk = int(input('Введите pk студента: '))

load_students() # возвращает имена студентов
get_student_by_pk(user_pk)  # возвращает скилл студента по пк

if user_pk <= len(list_stud_name):
      print(f'\nВаш выбор: студент {list_stud_name[user_pk - 1]}')

      skills_str = ''
      for skill in list_stud_skills:
          skills_str += skill + ', '
          sk_rs = skills_str.rstrip(', ') # или метод join
      print(f'Знает: {sk_rs}\n')
elif user_pk > len(list_stud_name):
      print('Студент в списке не значится...')
      sys.exit()


user_title = input('Выберите специальность для оценки: ')

load_professions() # возвращает названия профессий
get_profession_by_title(user_title)

if user_title in list_prof_title:
      list_prof_skills_join = (', ').join(list_prof_skills)

      print(f'Выбранная специальность: {user_title}')
      print(f'Требуемые навыки: {list_prof_skills_join}\n')
else:
      print('Данная специальность отсутствует...')
      sys.exit()

print('Оценка студента: ')

check_fitness(list_stud_skills, list_prof_skills)
