from src.additional import get_top_vacancies, print_vacancies
from src.head_hunter_api import HeadHunterApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем. В функции проверяются следующие возможности: получение вакансий
    по ключевому запросу на сайте HeadHunter.ru, вывод топ N ваканский по средней зарплате(N задает пользователь),
    добавление и удаление вакансий, сохранение созданных вакансий в файл и вывод их из файла в консоль."""
    search_query = "Python Developer"  # input("Введите поисковый запрос: ")
    top_n = 3  # int(input("Введите количество вакансий для вывода в топ N: "))
    hh_api = HeadHunterApi()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    print(f"Вакансии с сайта HeadHunter по запросу {search_query}:")
    print_vacancies(vacancies_list)

    # new_vacancy = Vacancy(
    #     "Python Developer", "<https://hh.ru/vacancy/123456>", 100000, 150000, "Требования: опыт работы от 3 лет..."
    # )
    #
    # json_saver = JsonSaver()
    # json_saver.add_data_to_file(new_vacancy)
    # vacancy_from_file = json_saver.get_data_from_file()
    # json_saver.delete_data_from_file(new_vacancy)
    # print("Список вакансий из файла:")
    # print_vacancies(vacancy_from_file)

    top_vacancies = get_top_vacancies(vacancies_list, top_n)
    print("Отсортированные вакансии по средней зарплате:")
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
