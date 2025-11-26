def move_disk(source, target, state):
    """
    Функція виконує фізичне переміщення диска у структурі даних
    і друкує інформацію про хід.
    """
    # Беремо верхній диск з початкового стрижня
    disk = state[source].pop()
    
    # Кладемо його на цільовий стрижень
    state[target].append(disk)
    
    # Виводимо повідомлення
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")

def hanoi(n, source, target, auxiliary, state):
    """
    Рекурсивна функція для розв'язання Ханойської вежі.
    n - кількість дисків
    source - початковий стрижень
    target - цільовий стрижень
    auxiliary - допоміжний стрижень
    state - словник з поточним станом стрижнів
    """
    if n == 1:
        # Базовий випадок: якщо диск один, просто переміщаємо його
        move_disk(source, target, state)
    else:
        # Крок 1: Перемістити n-1 дисків з source на auxiliary
        hanoi(n - 1, source, auxiliary, target, state)
        
        # Крок 2: Перемістити найбільший диск (n-й) з source на target
        move_disk(source, target, state)
        
        # Крок 3: Перемістити n-1 дисків з auxiliary на target
        hanoi(n - 1, auxiliary, target, source, state)

def main():
    try:
        # Введення кількості дисків
        n = int(input("Введіть кількість дисків (n): "))
        
        # Ініціалізація початкового стану
        # Створюємо список [n, n-1, ..., 1] для стрижня A
        initial_stack = list(range(n, 0, -1))
        
        towers_state = {
            'A': initial_stack,
            'B': [],
            'C': []
        }
        
        print(f"Початковий стан: {towers_state}")
        
        # Запуск алгоритму: перемістити n дисків з A на C, використовуючи B як допоміжний
        hanoi(n, 'A', 'C', 'B', towers_state)
        
        print(f"Кінцевий стан: {towers_state}")

    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()