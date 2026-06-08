import time

def my_coroutine():
    # Инициализируем переменную состояния
    current_value = 0
    
    print("Корутина запущена")
    
    while True:
        # yield приостанавливает выполнение и ждет .send()
        # received_value - это то, что пришло через .send()
        # Если использовали next(), received_value будет None
        received_value = yield current_value
        
        if received_value is not None:
            # Если прислали число, обновляем текущее значение
            current_value = received_value
            print(f"Получено новое значение: {current_value}")
        else:
            # Если ничего не прислали (next()), просто увеличиваем на 1
            current_value += 1
            
        print(f"Следующее возвращаемое значение будет: {current_value}")

def my_timer(label):
    print(f"--- Таймер {label} ---")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.5) # Ускорил для наглядности

# --- Запуск ---
g = my_coroutine()

# 1. Первый запуск всегда через next() или send(None), 
#    чтобы дойти до первого yield
next(g) 

# Цикл взаимодействия
try:
    while True:
        my_timer("Пауза")
        
        # Отправляем новое значение в корутину
        # Например, квадрат предыдущего или просто фиксированное число
        val = g.send(100) 
        print(f"Генератор вернул: {val}\n")
        

        
        
except StopIteration:
    print("Корутина завершена")