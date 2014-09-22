from random import randint, random, choice
import re


class Term():
    """
    represent one element in polynomial
    """

    def __init__(self, const=1, power=1):
        self.const = const
        self.power = power

    def copy(self):
        return Term(self.const, self.power)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return other + self
        if isinstance(other, Term):
            if self.power == other.power:
                return Polynomial(Term(self.const + other.const, self.power))
            else:
                return Polynomial(self, other)
        elif isinstance(other, int):
            return Polynomial(self, Term(other, 0))
        else:
            raise TypeError("Term can addition only with term or integer")

    def __sub__(self, other):
        return self + other * (-1)

    def __neg__(self, other):
        return self.copy() * (-1)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            return other * self
        if isinstance(other, Term):
            return Polynomial(
                Term(self.const * other.const, self.power + other.power))
        elif isinstance(other, int):
            return Polynomial(Term(self.const * other, self.power))
        else:
            raise TypeError("Term can addition only with term or integer")

    def __eq__(self, other):
        return self.power == other.power and self.const == other.const

    def __repr__(self):
        if not self.const:
            return ""
        elif not self.power:
            return str(self.const)
        elif self.power == 1:
            if self.const == 1:
                return "x"
            elif self.const == -1:
                return "-x"
            else:
                return str(self.const) + "*x"
        elif self.power > 1:
            if self.const == 1:
                return "x**" + str(self.power)
            elif self.const == -1:
                return "-x**" + str(self.power)
            else:
                return str(self.const) + "*x**" + str(self.power)
        else:
            return str(self.const) + "*" + "*".join(['x'] * self.power)


class Polynomial():
    """
    Represent polynomial as list of terms
    """

    def __init__(self, *terms):
        self.terms = []
        for term in terms:
            self.add(term.copy())

    def copy(self):
        """
        I little paranoid about moving objects
        """
        res = Polynomial()
        for term in self.terms:
            res.terms.append(term.copy())
        return res

    def add(self, other):
        """
        It's using for create new polynomial
        """
        if isinstance(other, Term) and other.const:
            for term in self.terms:
                if term.power == other.power:
                    term.const += other.const
                    if not term.const:
                        self.terms.remove(term)
                    break
            else:
                self.terms.append(other)

    def __add__(self, other):
        if isinstance(other, Term):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            raise TypeError("Second operand must be Polynomial")
        res = self.copy()
        for term in other:
            res.add(term)
        return res

    def __sub__(self, other):
        return self + other * (-1)

    def __mul__(self, other):
        res = Polynomial()
        if isinstance(other, Term):
            other = Polynomial(other)
        if isinstance(other, int):
            other = Polynomial(Term(other, 0))
        if isinstance(other, Polynomial):
            for term1 in self.terms:
                for term2 in other.terms:
                    res += term1 * term2
        return res

    def __iter__(self):
        for term in self.terms:
            yield term

    def __repr__(self):
        res_str = ""
        for term in sorted(self.terms, key=lambda x: x.power, reverse=True):
            res_str += ("+" + str(term)) if term.const > 0 else str(term)
        if res_str and res_str[0] == "+":
            res_str = res_str[1:]
        return res_str if res_str else "0"


def simplify(expr):
    #change all variables and numbers to Term instance
    expr = expr.replace("x", "Term()")
    expr = re.sub(r"(\d+)", r"Term(\1, 0)", expr)
    res = eval(expr)
    return str(res)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"

T = [
    # "(x-1)*(x-1)",
    # "(x+3)*(x+3)",
    # "(x+4)*x*3-x*x",
    # "x+x*x+x*x*x*x",
    # "2*(2*x+3)-x+x*x*x*x",
    # "3+4*x-24-2*x",
    # "(x+1)*x*(x+1)",
    # "x*x*x*x*x+100-2",
    # "(x-500)*(x+500)",
    # "(x-2)*(x+2)*(x+2)",
    None,
    None,
    None,
    None,
    None,
    None,
]

data = [str(i) for i in range(100)] + ["x"] * 1000

for t in T:
    if t is None:
        to_close = 0
        lenght = randint(1, 40)
        res = ""
        need_close = False
        for _ in range(lenght):
            bracket = random() < 0.2
            if bracket:
                res += "("
                to_close += 1
                need_close = True
            res += choice(data)
            if need_close and random() < 0.2 + to_close / 100:
                res += ")"
                need_close = False
                to_close -= 1
            res += choice("*-+")
        res = res[:-1]
        res += ")" * to_close
        t = res
        # print(t)

    ans = simplify(t)
    print("""{{
    "input": "{}",
    "answer": "{}",
    }},""".format(t, ans))