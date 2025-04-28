import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies_list() -> list[Vacancy]:
    return [
        Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 10, 20, "Требования: опыт работы от 3 лет..."),
        Vacancy("Java Developer", "<https://hh.ru/vacancy/123457>", 0, 15, "Требования: опыт работы от 3 лет..."),
        Vacancy("Python Developer", "<https://hh.ru/vacancy/123458>", 50, 70, "Требования: опыт работы от 3 лет..."),
    ]


@pytest.fixture
def vacancies_list_from_file() -> list:
    return [Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 10, 20, "Требования: опыт работы от 3 лет")]
