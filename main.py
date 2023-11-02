if __name__ == '__main__':
    import requests
    from datetime import datetime
    from application.salary import calculate_salary
    from application.db.people import get_employees

    calculate_salary()
    get_employees()

    full_time = datetime.now()
    print(full_time.date())

    # print(datetime.now().date())   #или еще так

    def connect(url):
        """Проверяет доступность для работы сраницы и выводит  responce"""
        headers = {'User-Agent': 'HH-User-Agent'}  # по условиям использования API HH.ru иначе бедет 404
        response = requests.get(url, headers=headers)  # headers
        return response

    print(connect('https://ya.ru/').status_code)