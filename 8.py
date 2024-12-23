class Menu:
    def __init__(self):
        self.text = None
        self.result = None

    def display_menu(self):
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.input_data()
            elif choice == '2':
                self.execute_algorithm()
            elif choice == '3':
                self.display_result()
            elif choice == '4':
                print("Завершение работы программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def input_data(self):
        print("Выберите способ ввода данных:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать данные случайным образом")
        input_choice = input("Выберите способ ввода: ")
        if input_choice == '1':
            print("Ввод данных вручную (пока не реализовано)")
        elif input_choice == '2':
            print("Генерация данных случайным образом (пока не реализовано)")
        else:
            print("Неверный выбор. Попробуйте снова.")

    def execute_algorithm(self):
        print("Выполнение алгоритма (пока не реализовано)")

    def display_result(self):
        print("Вывод результата (пока не реализовано)")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
