# faceDraw Module
# Written by Aleko Khomasuridze on 04.12.2022
# This module provides drawing functions for visualizing face-related information in OpenCV.

import cv2 as cv

class faceDraw:
    def __init__(self):
        self.center_point
        self.shade
        self.bgshow

    @classmethod
    def circleFrame(cls, image, X, Y, W, H, radius, color, stroke):
        """
        Draw circles around the four corners of a rectangle.

        Parameters:
        - image: Input image.
        - X, Y: Coordinates of the top-left corner of the rectangle.
        - W, H: Width and height of the rectangle.
        - radius: Radius of the circles.
        - color: Color of the circles.
        - stroke: Thickness of the circles' outline.
        """
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.radius = radius
        cls.color = color
        cls.stroke = stroke

        cv.circle(image, (X, Y), radius, color, stroke)
        cv.circle(image, (X + W, Y), radius, color, stroke)
        cv.circle(image, (X, Y + H), radius, color, stroke)
        cv.circle(image, (X + W, Y + H), radius, color, stroke)

    @classmethod
    def frame(cls, image, X, Y, W, H, color, size, thickness):
        """
        Draw a frame (lines) around a rectangle.

        Parameters:
        - image: Input image.
        - X, Y: Coordinates of the top-left corner of the rectangle.
        - W, H: Width and height of the rectangle.
        - color: Color of the frame.
        - size: Size of the frame lines.
        - thickness: Thickness of the frame lines.
        """
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.size = size
        cls.thickness = thickness

        cv.line(image, (X, Y), (X + size, Y), color, thickness)
        cv.line(image, (X, Y), (X, Y + size), color, thickness)

        cv.line(image, (X + W, Y), (X + W - size, Y), color, thickness)
        cv.line(image, (X + W, Y), (X + W, Y + size), color, thickness)

        cv.line(image, (X, Y + H), (X + size, Y + H), color, thickness)
        cv.line(image, (X, Y + H), (X, Y + H - size), color, thickness)

        cv.line(image, (X + W, Y + H), (X + W - size, Y + H), color, thickness)
        cv.line(image, (X + W, Y + H), (X + W, Y + H - size), color, thickness)

    @classmethod
    def center(cls, image, X, Y, W, H, color, Type, size):
        """
        Draw a center point or crosshair in the center of a rectangle.

        Parameters:
        - image: Input image.
        - X, Y: Coordinates of the top-left corner of the rectangle.
        - W, H: Width and height of the rectangle.
        - color: Color of the center point or crosshair.
        - Type: Type of the visual element ("circle" or "crossHair").
        - size: Size of the visual element.
        """
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.Type = Type
        cls.size = size

        center_point = (X + W // 2, Y + H // 2)

        if Type == "circle":
            cv.circle(image, center_point, 5, color, 2)
        elif Type == "crossHair":
            hor_x_pt1 = X + W // 2 - size
            hor_y_pt1 = Y + H // 2

            hor_x_pt2 = X + W // 2 + size
            hor_y_pt2 = Y + H // 2

            cv.line(image, (hor_x_pt1, hor_y_pt1), (hor_x_pt2, hor_y_pt2), color, 2)

            ver_x_pt1 = X + W // 2
            ver_y_pt1 = Y + H // 2 - size

            ver_x_pt2 = X + W // 2
            ver_y_pt2 = Y + H // 2 + size

            cv.line(image, (ver_x_pt1, ver_y_pt1), (ver_x_pt2, ver_y_pt2), color, 2)

    @classmethod
    def label(cls, image, X, Y, W, H, color, text, text_color):
        """
        Draw a labeled rectangle with text.

        Parameters:
        - image: Input image.
        - X, Y: Coordinates of the top-left corner of the rectangle.
        - W, H: Width and height of the rectangle.
        - color: Color of the labeled rectangle.
        - text: Text to be displayed.
        - text_color: Color of the text.
        """
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.text = text
        cls.text_color = text_color

        bgshow = 3
        shade = 30

        cv.rectangle(image, (X + bgshow, Y + H + 8 + bgshow), (X + bgshow + len(text) * 12, Y + H + bgshow + 30),
                     (color[0] - shade, color[1] - shade, color[2] - shade), cv.FILLED)
        cv.rectangle(image, (X, Y + H + 8), (X + len(text) * 12, Y + H + 30), color, cv.FILLED)
        cv.putText(image, text.upper(), (X + 3, Y + H + 24), cv.FONT_HERSHEY_PLAIN, 1, text_color, 2)

    @classmethod
    def putTxt(cls, image, X, Y, W, H, color, text):
        """
        Draw text information about rectangle coordinates and size.

        Parameters:
        - image: Input image.
        - X, Y: Coordinates of the top-left corner of the rectangle.
        - W, H: Width and height of the rectangle.
        - color: Color of the text.
        - text: Boolean value indicating whether to display text information or not.
        """
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.text = text

        lab = ['X', 'Y', 'W', 'H']
        lab_start = 10

        if text == False:
            cv.putText(image, "{}: {}px".format(lab[0], X), (X + W + lab_start, Y + 10), cv.FONT_HERSHEY_PLAIN, 1,
                       color, 1)
            cv.putText(image, "{}: {}px".format(lab[1], Y), (X + W + lab_start, Y + 30), cv.FONT_HERSHEY_PLAIN, 1,
                       color, 1)
            cv.putText(image, "{}: {}px".format(lab[2], W), (X + W + lab_start, Y + 50), cv.FONT_HERSHEY_PLAIN, 1,
                       color, 1)
            cv.putText(image, "{}: {}px".format(lab[3], H), (X + W + lab_start, Y + 70), cv.FONT_HERSHEY_PLAIN, 1,
                       color, 1)

        else:
            for i in range(len(text)):
                cv.putText(image, text[i].upper(), (X + W + lab_start, Y + 10 + (20 * i)), cv.FONT_HERSHEY_PLAIN, 1,
                           color, 1)

def main():
    pass

if __name__ == "__main__":
    main()
