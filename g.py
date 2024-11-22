def main():
    import sys
    
    # Чтение входных данных
    X = int(input().strip())
    A, B = map(int, input().strip().split())
    N = int(input().strip())
    
    yams = []
    for _ in range(N):
        start, width = map(int, input().strip().split())
        yams.append((start, start + width))
    
    # Возможные позиции треугольника
    positions = [
        (0, A),       # Позиция 1
        (A/2, A/2 + B),   # Позиция 2, с учетом, что B/2 - где выше угол
        (A, A + B)    # Позиция 3
    ]
    
    counts = []
    
    for base_left, base_right in positions:
        yams_needed = []
        for i, (start, end) in enumerate(yams):
            if base_left < end and base_right > start:
                yams_needed.append((start, end))

        # Храним количество и сумму для определения оптимальности
        counts.append((len(yams_needed), sum(start for start, _ in yams_needed), yams_needed))
    
    # Найдем минимальное количество ям для заделки
    counts.sort()  # Сначала сортим по количеству, потом по сумме

    best_count, _, best_yams = counts[0]
    
    # Сортируем ямы по началу
    best_yams.sort()
    
    print(best_count)
    for start, end in best_yams:
        print(start)

if __name__ == "__main__":
    main()
