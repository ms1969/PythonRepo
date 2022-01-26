def main(s):
    cost = int(60 * len(s))
    rubbles = cost // 100
    kop = cost % 100
    print(f"{rubbles} р. {kop} коп.")


if __name__ == '__main__':
    s = input()
    main(s)
