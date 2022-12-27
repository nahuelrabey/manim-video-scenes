from manim import *

chem_template = TexTemplate()
chem_template.add_to_preamble(r"\usepackage[version=3]{mhchem}")


def ChemTex(str: str):
    return MathTex(str, tex_template=chem_template)


formula = ChemTex(
r"\ce{N2} + 3\ce{H2} \rightarrow 2\ce{NH3}",
)
equivalence1 = ChemTex(
r"3mol\ce{H2} \Large \bumpeq 2 mol\ce{NH3}"
)
equivalence2 = ChemTex(
r"1mol\ce{N2} \Large \bumpeq 2 mol\ce{NH3}"
)
equivalences = VGroup(equivalence1, equivalence2)
group = VGroup(formula, equivalences)

proportion1 = ChemTex(
    r"\frac{2mol\ce{NH3}}{3mol\ce{H2}"
)
proportion2 = ChemTex(
    r"\frac{3mol\ce{H2}}{2mol\ce{NH3}"
)
proportions = VGroup(proportion1, proportion2)

class EquivalenciaEstequiometrica(Scene):
    def construct(self):
        equivalence1.next_to(formula, DOWN)
        equivalence2.next_to(equivalence1, DOWN)

        group.move_to(ORIGIN)

        self.wait(1)
        self.play(Write(formula))
        self.wait(1)
        self.play(Write(equivalence1))
        self.play(equivalence1.animate.set_color(GREEN))
        self.wait(1)
        self.play(
            Write(equivalence2),
            equivalence1.animate.set_color(WHITE),
        )
        self.play(
            equivalence2.animate.set_color(GREEN)
        )
        self.play(equivalence2.animate.set_color(WHITE))
        self.play(FadeOut(equivalences))
        self.wait(2)


class FactoresDeConversion(Scene):
    def construct(self):
        equivalence1.next_to(formula, RIGHT)
        equivalence2.next_to(equivalence1, RIGHT)
        group.scale(0.75)
        group.move_to(ORIGIN + 3.25*UP)

        self.wait(1)
        self.play(FadeIn(group))
        self.wait(1)

        proportion1.move_to(ORIGIN)
        proportion2.next_to(proportion1, 6*RIGHT)
        proportions.move_to(ORIGIN)

        self.play(Write(proportion1))
        self.wait()
        self.play(Write(proportion2))
        self.wait(2)

class Ejemplo1(Scene):
    def construct(self):
        return super().construct()