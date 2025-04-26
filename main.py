from src.head_hunter_api import HeadHunterApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def user_interaction():
    # search_query = "NDCG"
    # # search_query = input("Введите поисковый запрос: ")
    # # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # hh_api = HeadHunterApi()
    # hh_vacancies = hh_api.get_vacancies(search_query)
    # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # print(len(vacancies_list))

    # for vacancy in vacancies_list:
    #     print(vacancy)

    new_vacancy = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", 100000, 150000, "Требования: опыт работы от 3 лет..."
    )

    json_saver = JsonSaver()
    json_saver.add_data_to_file(new_vacancy)
    json_saver.delete_data_from_file(new_vacancy)

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
