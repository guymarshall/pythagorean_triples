from math import hypot


def gcd(number_1, number_2):
    if number_2 == 0:
        return number_1
    else:
        return gcd(number_2, number_1 % number_2)

def main():
    number_triples_needed = int(input("Number of triples to calculate: "))
    number_triples_calculated = 0
    side_a = 1

    loop_a = number_triples_needed > 0
    result = []

    while loop_a:
        side_b = 1
        loop_b = True

        while side_b <= side_a and loop_b:
            if round(gcd(side_a, side_b)) == 1:
                side_c = round(hypot(side_a, side_b))

                if side_c ** 2 == (side_a ** 2 + side_b ** 2):
                    number_triples_calculated += 1
                    result = [side_b, side_a, side_c]
                    print(f"{number_triples_calculated}: {result}")

                    if number_triples_calculated == number_triples_needed:
                        loop_a = False
                        loop_b = False
            side_b += 1
        side_a += 1
    if number_triples_needed < 1:
        print(f"{number_triples_needed} is invalid.")
        main()

if __name__ == "__main__":
    main()