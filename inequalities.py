from manim import *

def WW(T, self):
    self.play(Write(T))
    self.wait(2)
    self.play(FadeOut(T))

class Intro(Scene):
    def construct(self):
        t = Text("Desigualdades Cuadráticas Positivas")
        WW(t,self)

class Example(Scene):
    def construct(self):
        e1 = MathTex(r"2 \cdot 3 = 6")
        e2 = MathTex(r"(-3)\cdot (-2) = 6")
        e3 = MathTex(r"(-5) \cdot 2 = -10")
        e3.move_to(ORIGIN + UP)
        e4 = MathTex(r"2 \cdot (-5) = -10")
        e4.move_to(ORIGIN + DOWN)

        WW(e1,self)
        WW(e2,self)
        self.play(Write(e3), Write(e4))
        self.wait(2)
        self.play(FadeOut(e3), FadeOut(e4))

class Definition(Scene):
    def construct(self):
        e1 = MathTex(r"a \cdot b > 0")
        e2 = MathTex(r"a > 0 \land b > 0")
        e2.set_color(GREEN)
        e3 = MathTex(r"a < 0 \land b < 0")
        e3.set_color(RED)

        WW(e1,self)
        WW(e2,self)
        WW(e3,self)
        

class SolvingIntro(Scene):
    def construct(self):
        t1 = MathTex(r"(x+1)(x-1) > 0")
        WW(t1,self)

class ASolvingIntro(Scene):
    def construct(self):
        t2 = MathTex(r"x+1 > 0 \land x-1 > 0")
        t2b = MathTex(r"x+1 > 0 \land x-1 > 0")
        t2b[0][0:5].set_color(GREEN)
        t2b[0][6:11].set_color(RED)

        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2,t2b))
        self.wait(2)
        self.play(FadeOut(t2))


class ASolvingLeft(Scene):
    def construct(self):

        # LEFT SIDE
        t3 = MathTex(r"x+1 > 0")
        t3.set_color(GREEN)
        t3.move_to(ORIGIN + UP)
        t4 = MathTex(r"x +1 -1 > 0 -1 ")
        t4.move_to(ORIGIN)
        t5 = MathTex(r"x > -1 ")
        t5.move_to(ORIGIN - UP)

        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(t5))
        self.wait(2)
        self.play(FadeOut(t3,t4,t5))

class ASolvingRight(Scene):
    def construct(self):

        # LEFT SIDE
        t3 = MathTex(r"x-1 > 0")
        t3.set_color(RED)
        t3.move_to(ORIGIN + UP)
        t4 = MathTex(r"x -1 +1 > 0 +1")
        t4.move_to(ORIGIN)
        t5 = MathTex(r"x > 1")
        t5.move_to(ORIGIN - UP)

        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(t5))
        self.wait(2)
        self.play(FadeOut(t3,t4,t5))

class AConclusion1(Scene):
    def construct(self):
        t1 = MathTex(r"x+1 > 0 \land x-1 > 0")
        t1.move_to(ORIGIN + UP)

        t2 = MathTex(r"x > -1 \land x > 1")
        t2.move_to(ORIGIN + DOWN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)

class AConclusion2(Scene):
    def construct(self):
        t1 = MathTex(r"x = 0")
        t1.move_to(ORIGIN + UP)

        t2 = MathTex(r"x > -1 \land x > 1")
        t2P = ORIGIN + DOWN
        t2.move_to(t2P)

        t2a = MathTex(r"0 > -1 \land x > 1")
        t2a.move_to(t2P)
        t2a[0][0:4].set_color(GREEN)

        t2b = MathTex(r"0 > -1 \land 0 \ngtr 1")
        t2b.move_to(t2P)
        t2b[0][0:4].set_color(GREEN)
        t2b[0][5:8].set_color(RED)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2,t2a))
        self.wait(2)
        self.play(Transform(t2,t2b))
        self.wait(2)
        self.play(FadeOut(t1,t2))

class AConclusion3(Scene):
    def construct(self):
        t1 = MathTex(r"x = 2")
        t1.move_to(ORIGIN + UP)

        t2 = MathTex(r"x > -1 \land x > 1")
        t2P = ORIGIN + DOWN
        t2.move_to(t2P)

        t2a = MathTex(r"2 > -1 \land x > 1")
        t2a.move_to(t2P)
        t2a[0][0:4].set_color(GREEN)

        t2b = MathTex(r"2 > -1 \land 2 > 1")
        t2b.move_to(t2P)
        t2b[0][0:4].set_color(GREEN)
        t2b[0][5:8].set_color(GREEN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2,t2a))
        self.wait(2)
        self.play(Transform(t2,t2b))
        self.wait(2)
        self.play(FadeOut(t1,t2))

class AConclusionGraph(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        num = NumberLine(
            include_numbers=True,
            include_tip=True,
            tip_height=0.1,
            tip_width=0.1,
            font_size=30,
        )
        num.set_color(BLACK)

        c1 = Rectangle(
            height=1.10,
            width=9,
            stroke_width = 0
        )
        c1.set_fill(PURE_BLUE, opacity=0.5)
        c1.move_to(ORIGIN + 0.05*DOWN+ 3.5*RIGHT)
        e1 = MathTex(r"x > -1")
        e1.move_to(ORIGIN + 2*UP)
        e1.set_color(BLACK)
        e1.scale(2)

        c2 = Rectangle(
            height=1.10,
            width=7,
            stroke_width = 0
        )
        c2.set_fill(PURE_RED, opacity=0.5)
        c2.move_to(ORIGIN + 0.05*UP + 4.5*RIGHT)
        e2 = MathTex(r"x > 1")
        e2.move_to(ORIGIN + 2*DOWN)
        e2.set_color(BLACK)
        e2.scale(2)

        pF = MathTex(r"x > 1")
        pF.set_color(BLACK)
        pF.move_to(ORIGIN + 2*UP)
        pF.scale(2)

        F = MathTex(r"x \in (1;\infty)")
        F.set_color(BLACK)
        F.move_to(ORIGIN + 2*UP)
        F.scale(2)

        self.play(Create(num))
        self.wait(2)
        self.play(Create(c1), Create(e1))
        self.wait(2)
        self.play(FadeOut(c1, e1), Create(c2), Create(e2))
        self.wait(2)
        self.play(FadeOut(c2, e2))
        self.play(FadeIn(c1,c2))
        self.play(Write(pF))
        self.play(Transform(pF, F))
        self.wait(3)
        self.play(FadeOut(c1,c2,pF,num))

class BSolvingIntro(Scene):
    def construct(self):
        t2 = MathTex(r"x+1 < 0 \land x-1 < 0")
        t2b = MathTex(r"x+1 < 0 \land x-1 < 0")
        t2b[0][0:5].set_color(GREEN)
        t2b[0][6:11].set_color(RED)

        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2,t2b))
        self.wait(2)
        self.play(FadeOut(t2))
class BSolvingLeft(Scene):
    def construct(self):

        # LEFT SIDE
        t3 = MathTex(r"x+1 < 0")
        t3.set_color(GREEN)
        t3.move_to(ORIGIN + UP)
        t4 = MathTex(r"x +1 -1 < 0 -1 ")
        t4.move_to(ORIGIN)
        t5 = MathTex(r"x < -1 ")
        t5.move_to(ORIGIN - UP)

        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(t5))
        self.wait(2)
        self.play(FadeOut(t3,t4,t5))

class BSolvingRight(Scene):
    def construct(self):

        # LEFT SIDE
        t3 = MathTex(r"x-1 < 0")
        t3.set_color(RED)
        t3.move_to(ORIGIN + UP)
        t4 = MathTex(r"x -1 +1 < 0 +1")
        t4.move_to(ORIGIN)
        t5 = MathTex(r"x < 1")
        t5.move_to(ORIGIN - UP)

        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(t5))
        self.wait(2)
        self.play(FadeOut(t3,t4,t5))

class BConclusion1(Scene):
    def construct(self):
        t1 = MathTex(r"x+1 < 0 \land x-1 < 0")
        t1.move_to(ORIGIN + UP)

        t2 = MathTex(r"x < -1 \land x < 1")
        t2.move_to(ORIGIN + DOWN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)

class BConclusion2(Scene):
    def construct(self):
        t1 = MathTex(r"x = 0")
        t1.move_to(ORIGIN + UP)

        t2 = MathTex(r"x < -1 \land x < 1")
        t2P = ORIGIN + DOWN
        t2.move_to(t2P)

        t2a = MathTex(r"0 \nless -1 \land x < 1")
        t2a.move_to(t2P)
        t2a[0][0:4].set_color(RED)

        t2b = MathTex(r"0 \nless -1 \land 0 < 1")
        t2b.move_to(t2P)
        t2b[0][0:4].set_color(RED)
        t2b[0][5:8].set_color(GREEN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2,t2a))
        self.wait(2)
        self.play(Transform(t2,t2b))
        self.wait(2)
        self.play(FadeOut(t1,t2))

class BConclusion3(Scene):
    def construct(self):
        t1 = MathTex(r"x = -2")
        t1.move_to(ORIGIN + UP)

        t2 = MathTex(r"x < -1 \land x < 1")
        t2P = ORIGIN + DOWN
        t2.move_to(t2P)

        t2a = MathTex(r"-2 < -1 \land x < 1")
        t2a.move_to(t2P)
        t2a[0][0:5].set_color(GREEN)

        t2b = MathTex(r"-2 < -1 \land -2 < 1")
        t2b.move_to(t2P)
        t2b[0][0:5].set_color(GREEN)
        t2b[0][6:10].set_color(GREEN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2,t2a))
        self.wait(2)
        self.play(Transform(t2,t2b))
        self.wait(2)
        self.play(FadeOut(t1,t2))

class BConclusionGraph(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        num = NumberLine(
            include_numbers=True,
            include_tip=True,
            tip_height=0.1,
            tip_width=0.1,
            font_size=30,
        )
        num.set_color(BLACK)

        c1 = Rectangle(
            height=1.10,
            width=9,
            stroke_width = 0
        )
        c1.set_fill(PURE_BLUE, opacity=0.5)
        c1.move_to(ORIGIN + 0.05*DOWN - 3.5*RIGHT)
        e1 = MathTex(r"x < -1")
        e1.move_to(ORIGIN + 2*UP)
        e1.set_color(BLACK)
        e1.scale(2)

        c2 = Rectangle(
            height=1.10,
            width=7,
            stroke_width = 0
        )
        c2.set_fill(PURE_RED, opacity=0.5)
        c2.move_to(ORIGIN + 0.05*UP - 4.5*RIGHT)
        e2 = MathTex(r"x < 1")
        e2.move_to(ORIGIN + 2*DOWN)
        e2.set_color(BLACK)
        e2.scale(2)

        F = MathTex(f"x \in (-\infty;-1)")
        F.set_color(BLACK)
        F.move_to(ORIGIN + 2*UP)
        F.scale(2)


        # self.add(num)
        # self.add(c1)
        # self.add(c2)
        self.play(Create(num))
        self.wait(1)
        self.play(Create(c1), Write(e1))
        self.wait(.5)
        self.play(FadeOut(c1,e1), Create(c2), Write(e2))
        self.wait(.5)
        self.play(FadeOut(c2,e2))
        self.play(FadeIn(c1,c2))
        self.play(Write(F))
        self.wait(1)
        self.play(FadeOut(c1,c2,F,num))

class GraphFinale(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        num = NumberLine(
            include_numbers=True,
            include_tip=True,
            tip_height=0.1,
            tip_width=0.1,
            font_size=30
        )
        num.set_color(BLACK)

        LEFT_COLOR = PURE_BLUE
        RIGHT_COLOR = PURE_RED

        c2 = Rectangle(
            height=1.10,
            width=7,
            stroke_width=0
        )
        c2.set_fill(LEFT_COLOR, opacity=0.25)
        c2.move_to(ORIGIN - 4.5*RIGHT)

        c1 = Rectangle(
            height=1.10,
            width=7,
            stroke_width=0
        )
        c1.set_fill(RIGHT_COLOR, opacity=0.3)
        c1.move_to(ORIGIN + 4.5*RIGHT)


        F = MathTex(r"x \in (-\infty, -1) \cup (1, \infty)")
        F.set_color(BLACK)
        F[0][2:9].set_color(LEFT_COLOR)
        F[0][2:9].set_opacity(0.35)
        F[0][10:15].set_color(RIGHT_COLOR)
        F[0][10:15].set_opacity(0.35)
        F.move_to(ORIGIN + 2*UP + LEFT)
        F.scale(2)

        # self.add(num)
        # self.add(c1)
        # self.add(c2)
        # self.add(index_labels(F[0]))
        # self.add(F)
        self.play(Create(num))
        self.wait(2)
        self.play(Create(c1))
        self.play(Create(c2))
        self.play(Write(F))
        self.wait(2)
        self.play(FadeOut(num,c1,c2,F))
