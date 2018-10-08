'''Создать класс Fraction, который должен иметь два поля:
числитель a и знаменатель b. Оба поля должны быть типа int.
Реализовать методы: сокращение дробей, сравнение, сложение и умножение.'''


def nod(x, y):
    if y == 0:
        return x
    return nod(y, x % y)


class Fraction(Exception):
    def __init__(self, a, b):
        Exception.__init__(self)
        try:
            self.numerator_a = a
            self.denominator_b = b
            if not b:
                raise ZeroDivisionError()
        except:
            print("ERROR: DENOMINATOR IS ZERO")

    def print_fr(self):
        print(self.numerator_a)
        print('-')
        print(self.denominator_b)

    def reduction(self):
        tmp = nod(self.numerator_a, self.denominator_b)
        self.numerator_a //= tmp
        self.denominator_b //= tmp
        return self

    def compare(self, B):
        a = self.numerator_a * B.denominator_b
        b = B.numerator_a * self.denominator_b
        if a > b:
            return self.print_fr()
        elif a < b:
            return B.print_fr()
        else:
            return print("EQUAL")

    def __add__(self, other):
        new_denom = self.denominator_b
        a = self.numerator_a
        b = other.numerator_a
        if self.denominator_b != other.denominator_b:
            new_denom = self.denominator_b * other.denominator_b
            a *= new_denom
            b *= new_denom
        return (Fraction(a + b, new_denom)).reduction()

    def __mul__(self, other):
        return Fraction(self.numerator_a * other.numerator_a, self.denominator_b * other.denominator_b).reduction()

    def __str__(self):
        return '{} \n-\n{}'.format(self.numerator_a, self.denominator_b)

def main():
    with open("input.txt", "r") as f:
        a, b = map(int, f.read().split())
        A = Fraction(2, 3)
        A.reduction()
        B = Fraction(2, 5)
        B.reduction()
        A.compare(B)
        C = A + B
        print(C)


if __name__ == '__main__':
    main()
