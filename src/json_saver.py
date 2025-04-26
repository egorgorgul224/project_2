import json
from pathlib import Path
from typing import Any

from src.base_files import BaseFiles
from src.vacancy import Vacancy

BASEDIR = Path(__file__).resolve().parent.parent


class JsonSaver(BaseFiles):
    """Класс JsonSaver предназначен для получения данных из файла, удаления и добавления данных."""

    file_path: str

    def __init__(self, file_path: str = "data") -> None:
        """Метод для инициализации экземпляра класса JsonSaver."""

        self.__file_path = Path(BASEDIR / "data" / file_path)

    def get_data_from_file(self) -> Any:
        """Метод для получения данных из файла."""
        try:
            with open(f"{self.__file_path}.json", "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def add_data_to_file(self, data: Any) -> None:
        """Метод для добавления данных в файл."""
        json_file_data = self.get_data_from_file()
        instance_info = Vacancy.transform_to_dict(data)
        if instance_info not in json_file_data:
            json_file_data.append(instance_info)

        with open(f"{self.__file_path}.json", "w", encoding="utf-8") as json_file:
            json.dump(json_file_data, json_file, indent=4, ensure_ascii=False)

    def delete_data_from_file(self, data: Any) -> None:
        """Метод для удаления данных из файла."""
        json_file_data = self.get_data_from_file()
        try:
            delete_info = Vacancy.transform_to_dict(data)
            json_file_data.remove(delete_info)
        except ValueError:
            print("Данные не найдены")

        with open(f"{self.__file_path}.json", "w", encoding="utf-8") as json_file:
            json.dump(json_file_data, json_file, indent=4, ensure_ascii=False)
