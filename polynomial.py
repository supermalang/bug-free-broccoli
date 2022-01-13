from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = coeffs

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        assert isinstance(other, Poly2)
        coeffa = self.coeffs[0] + other.coeffs[0]
        coeffb = self.coeffs[1] + other.coeffs[1]
        coeffc = self.coeffs[2] + other.coeffs[2]
        return coeffa +"x^2 + " + coeffb +"x +" + coeffc


    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        assert isinstance(other, Poly2)
        coeffa = self.coeffs[0] - other.coeffs[0]
        coeffb = self.coeffs[1] - other.coeffs[1]
        coeffc = self.coeffs[2] - other.coeffs[2]
        
        return coeffa +"x^2 + " + coeffb +"x +" + coeffc

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """

        coeffa = self.coeffs[0]
        coeffb = self.coeffs[1]
        coeffc = self.coeffs[2]
        
        coeffa_sign = " - "  if coeffa < 0  else " + "
        coeffb_sign = " - "  if coeffb < 0  else " + "
        coeffc_sign = " - "  if coeffc < 0  else " + "

        """
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        Je remarque que l'ordre des coeffs est inverse sur le print 🤔
        """
        return coeffc +"x^2 " + coeffb_sign + " " + abs(coeffb) +"x " + coeffa_sign + " " + abs(coeffa)

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        pass

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        pass

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        pass


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
