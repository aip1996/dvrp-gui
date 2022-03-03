def greedy_distribution(car_number, tour):
    solution = []
    stock = [0] * car_number
    tour.sort(reverse=True)
    for c in range(car_number):
        solution.append([])

    for t in tour:
        car_idx = stock.index(min(stock))
        stock[car_idx] += t
        solution[car_idx].append(t)

    return solution, stock


if __name__ == '__main__':
    tour = [5, 6, 4, 8, 2, 7, 13, 10, 3, 7, 8]
    car_number = 2
    solution, stock = greedy_distribution(car_number, tour)
    print("solution:", solution)
    print("stock", stock)
