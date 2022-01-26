def main(n1, n2):
    indexmas = n1 / n2 ** 2
    if 18.5 <= indexmas <= 25:
        print('Оптимальная масса')
    elif indexmas > 25:
        print("Избыточная масса")
    elif indexmas < 18.5:
        print("Недостаточная масса")
    return indexmas


if __name__ == '__main__':
    n1 = float(input())
    n2 = float(input())
    main(n1, n2)
