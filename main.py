from manim import *


class CreateCircle(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

        # square.next_to(circle, UP)


class Fractions(Scene):
    def construct(self):

        square1 = Square(side_length=4)
        half = Rectangle(width=4, height=2)
        quarter = Rectangle(width=2, height=2)

        square1.set_color(GREEN)
        half.set_color(YELLOW)
        half.generate_target()
        half.next_to(square1, LEFT * 2)

        quarter.set_color(RED)
        quarter.generate_target()
        quarter.next_to(square1, RIGHT * 2)

        tex_one = MathTex("1")
        tex_one.generate_target()
        tex_half = MathTex(r"\frac{1}{2}")
        tex_half_copy = tex_half.copy()
        tex_quarter = MathTex(r"\frac{1}{4}")
        tex_quarter_copy = tex_quarter.copy()

        tex_half.add_updater(
            lambda x: x.move_to(half.get_center() + LEFT)
        )

        tex_quarter.add_updater(
            lambda x: x.move_to(quarter.get_center())
        )

        # square1.generate_target()
        # square1.target.move_to(ORIGIN)

        # group = Group(square1, half, quarter)
        # group.scale(0.75)

        # self.add(square1, half, quarter)
        self.play(Create(square1), Write(tex_one))
        self.wait()

        self.play(Create(half), Create(quarter),
                  Write(tex_quarter), Write(tex_half))
        self.wait()

        half.target.move_to(ORIGIN + DOWN)
        quarter.target.move_to(ORIGIN + UP + RIGHT)
        self.play(MoveToTarget(half), MoveToTarget(quarter), FadeOut(tex_one))
        self.wait()

        tex_half_copy.move_to(ORIGIN + UP)
        tex_quarter_copy.move_to(ORIGIN + DOWN + LEFT)
        quarter.target.move_to(ORIGIN + DOWN + RIGHT)
        self.play(MoveToTarget(quarter), ReplacementTransform(
            tex_half, tex_quarter_copy), Write(tex_half_copy))
        self.wait(3)


class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT
        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        angle = Angle(line1, line_moving, radius=0.5)

        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 10 * SMALL_BUFF
            )  # .point_from_proportion(0.5)
        )
        self.add(line1, line_moving, angle, tex)

        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        angle.add_updater(
            lambda x: x.become(
                Angle(line1, line_moving, radius=0.5)
            )
        )

        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 10 * SMALL_BUFF
                )
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(110))
