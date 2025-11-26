import turtle

def koch_curve(t, order, size):
    """Рекурсивна функція для малювання однієї сторони."""
    if order == 0:
        t.forward(size)
    else:
        # Стандартна формула кривої Коха
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def run_snowflake_app():
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Восьмикутна Різдв'яна Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    
    #  розмір сторони, їх 8
    size = 180  

    while True:
        order_input = window.numinput(
            title="Налаштування",
            prompt="Введіть рівень рекурсії (0-5):\n(Cancel для виходу)",
            default=2,
            minval=0,
            maxval=5 # Для 8 сторін краще не ставити велику рекурсію, буде довго
        )

        if order_input is None:
            print("Роботу завершено користувачем.")
            break
        
        order = int(order_input)
        t.clear()
        
        # --- Центрування для восьмикутника ---
        # Потрібно піднятися вище і лівіше, щоб фігура була по центру
        t.penup()
        t.setheading(0)
        t.goto(-size * 0.5, size * 1.3) 
        t.pendown()

        # --- МАЛЮВАННЯ 8 СТОРІН ---
        sides = 8
        angle = 360 / sides  # 360 / 8 = 45 градусів

        for i in range(sides):
            # Перші 4 сторони - сині, останні 4 - жовті
            if i < 4:
                t.color("cyan")
            else:
                t.color("yellow")
            
            koch_curve(t, order, size)
            t.right(angle) # Поворот на 45 градусів

    window.bye()

if __name__ == "__main__":
    try:
        run_snowflake_app()
    except turtle.Terminator:
        pass