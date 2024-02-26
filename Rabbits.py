def rabbits(n, k):
    print('infertile_n_1: 0 infertile: 1 fertile: 0 month number: 0')

    month_number = 1
    infertile = 0
    fertile = 1
    infertile_n_1 = 0

    print('infertile_n_1: ' + str(infertile_n_1) + ' infertile: ' + str(infertile) + ' fertile: ' + str(fertile)
          + ' month number: ' + str(month_number))

    while month_number != (n - 1):
        infertile_n_1 = infertile
        infertile = fertile * k
        fertile = fertile + infertile_n_1
        print('infertile_n_1: ' + str(infertile_n_1) + ' infertile: ' + str(infertile) + ' fertile: ' + str(fertile)
              + ' month number: ' + str(month_number + 2))
        month_number += 1

    pairs = infertile + fertile
    return pairs

print('Number of pairs: ' + str(rabbits(10, 6)))



