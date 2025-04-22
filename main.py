from src.head_hunter_api import HeadHunterApi
from src.vacancy import Vacancy

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = "NDCG"
    # search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    hh_api = HeadHunterApi()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    print(len(vacancies_list))

    for vacancy in vacancies_list:
        print(vacancy)

    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
