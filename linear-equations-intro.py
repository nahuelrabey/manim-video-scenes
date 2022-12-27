
from manim import *


def writebatch(texts: list, scene: 'Scene', wait: int | float = 2):
    for t in (texts):
        scene.play(Write(t))
        scene.wait(wait)
        scene.play(FadeOut(t))


def transform_batch(texts: list, scene: 'Scene', wait: int | float = 2, delete: bool = True):
    prev = texts[0]
    scene.play(Write(prev))
    for t in (texts[1:]):
        scene.play(Transform(prev, t))
        scene.wait(wait)

    if (delete):
        scene.play(FadeOut(prev))


def end_write(text: Text, scene: Scene, wait=3):
    scene.play(Write(text))
    scene.wait(wait)
    scene.play(FadeOut(text))


class Intro(Scene):
    def construct(self):
        t1 = Text("Si un choripan cuesta 300$")
        t2 = Text("¿Cuantos me puedo comprar con 1000$")
        t3 = Text("Si quiero una docena ¿Cuánto tengo que gastar?")
        e1 = MathTex(r"costo(x) = 300 \cdot x")

        writebatch((t1, t2, t3), scene=self, wait=0)
        end_write(e1, scene=self, wait=4)


class Example1(Scene):
    def construct(self):
        sequence = [
            MathTex(r"costo(x) = 1000"),
            MathTex(r"300 \cdot x = 1000"),
            MathTex(r"\frac{300}{300} \cdot x = \frac{1000}{300}"),
            MathTex(r"x = \frac{1000}{300}"),
            MathTex(r"x = \frac{10}{3}"),
        ]
        end = MathTex(r"x = 3 + \frac{1}{3}")

        transform_batch(sequence, scene=self, wait=1)
        end_write(end, scene=self, wait=4)
