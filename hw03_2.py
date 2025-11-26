import turtle

def koch_curve(t, order, size):
    """
    Рекурсивна функція для малювання однієї сторони кривої Коха.
    """
    if order == 0:
        t.forward(size)
    else:
        # Стандартна формула розбиття лінії для кривої Коха
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake():
    """
    Ініціалізує вікно, запитує рівень рекурсії та малює сніжинку.
    """
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Фрактал 'Сніжинка Коха'")

    # --- ДОДАНО: Запит рівня рекурсії у користувача ---
    # minval=0 (мінімум), maxval=7 (максимум, бо більше 7 малюватиметься дуже довго)
    order_input = window.numinput(
        title="Налаштування", 
        prompt="Введіть рівень рекурсії (0-6):", 
        default=3, 
        minval=0, 
        maxval=7
    )

    # Якщо користувач натиснув Cancel, виходимо
    if order_input is None:
        print("Скасовано користувачем.")
        return

    order = int(order_input)
    size = 400  # Розмір сніжинки

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.hideturtle() # Ховаємо курсор черепашки
    t.pensize(2)

    # Позиціонування по центру екрану
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # --- МАЛЮВАННЯ  ---
    
    # 1 сторона (верхня - синя)
    t.color("cyan")
    koch_curve(t, order, size)
    t.right(120)

    # 2 сторона (права - жовта)
    t.color("yellow")
    koch_curve(t, order, size)
    t.right(120)

    # 3 сторона (ліва - жовта)
    t.color("yellow")
    koch_curve(t, order, size)
    t.right(120)

    # Завершення: клік по екрану закриває вікно
    window.exitonclick()

if __name__ == "__main__":
    try:
        draw_snowflake()
    except turtle.Terminator:
        pass # Ігнорувати помилку при закритті вікна