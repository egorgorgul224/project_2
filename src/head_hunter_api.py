from typing import Any

import requests

from src.base_api import BaseApi


class HeadHunterApi(BaseApi):
    """Класс HeadHunterApi для подключения и получения вакансий с сайта HeadHunter."""

    per_page: int

    def __init__(self, per_page: int = 50) -> None:
        """Метод для инициализации экземпляра класса HeadHunterApi."""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.per_page = per_page
        self.__vacancies = []

    def api_connect(self) -> Any:
        """Метод возвращает json-данные, полученные из приватного метода __api_connect."""
        return self.__api_connect()

    def __api_connect(self) -> Any:
        """Приватный метод для подключения по API, возвращает json-данные через get-запрос."""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            error_message = f"Ошибка: {response.status_code}: {response.text}"
            raise requests.exceptions.HTTPError(error_message)
        else:
            return response.json()

    def get_vacancies(self, keyword: str) -> Any:
        """Метод возвращает список словарей с вакансиями по заданному ключевому слову(keyword)."""
        self.__params["text"] = keyword
        self.__vacancies.clear()
        while self.__params.get("page") < self.per_page:
            try:
                data = self.api_connect()
                vacancies = data.get("items", [])
            except requests.exceptions.HTTPError:
                break
            else:
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1

        return self.__vacancies
