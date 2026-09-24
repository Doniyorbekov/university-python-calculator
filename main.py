import math

class Calculator:
    """Класс для выполнения математических операций."""
    
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        # Обработка исключения: деление на ноль
        if b == 0:
            raise ZeroDivisionError("Ошибка: Деление на ноль невозможно!")
        return a / b
        
    def power(self, a, b):
        return math.pow(a, b)

def main():
    calc = Calculator()
    print("--- Модульный калькулятор на Python ---")
    
    try:
        # Валидация входных данных
        num1 = float(input("Введите первое число: "))
        operator = input("Введите операцию (+, -, *, /, ^): ")
        num2 = float(input("Введите второе число: "))
        
        if operator == "+":
            print(f"Результат: {calc.add(num1, num2)}")
        elif operator == "-":
            print(f"Результат: {calc.subtract(num1, num2)}")
        elif operator == "*":
            print(f"Результат: {calc.multiply(num1, num2)}")
        elif operator == "/":
            print(f"Результат: {calc.divide(num1, num2)}")
        elif operator == "^":
            print(f"Результат: {calc.power(num1, num2)}")
        else:
            print("Ошибка: Неверный оператор!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числа!")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "main":
    main()
