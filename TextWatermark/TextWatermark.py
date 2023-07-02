"""

Text watermark class
#100DaysOfCode with Python
Day: 84
Date: 2023-07-02

"""

from PIL import ImageFont
from PIL import ImageDraw


class TextWatermark:

    WATERMARK_TEXT_FONT = ImageFont.truetype('Arial bold', 24)
    WATERMARK_TEXT_FG = (255, 255, 255)

    def __init__(self):
        self.draw = None
        self.watermark_text = None
        self.fill_fg = self.WATERMARK_TEXT_FG
        self.font = self.WATERMARK_TEXT_FONT

    def set_image(self,
                  image: ImageDraw):
        """
        set image to watermark ;)
        :param image:
        :return:
        """
        if not isinstance(image, ImageDraw):
            raise ValueError("Incorrect value, must be ImageDraw")

        self.draw = ImageDraw.Draw(image)

    def set_watermark_text(self,
                           watermark_text: str):
        """
        Set watermark text
        :param watermark_text: text as watermark
        :return: None
        """
        if not isinstance(watermark_text, str):
            raise ValueError('Watermark text must be str type!')

        self.watermark_text = watermark_text

    def get_watermark_text(self) -> str:
        """
        :return: watermark text
        """
        return self.watermark_text

    def get_watermark_fill_fg(self) -> list(int):
        """
        :return: fill list as RGB like (0, 0, 0)
        """
        return self.fill_fg

    def set_watermark_fill_fg(self,
                              fill: list(int)):
        """
        set fill for watermark text as (0, 0, 0) RGB
        :param fill:
        :return:
        """
        if fill is None:
            raise ValueError("Fill must be set!")

        self.fill_fg = fill

    def get_watermark_font(self) -> ImageFont.truetype:
        """
        :return: watermark text font as ImageFont.truetype
        """
        return self.font

    def set_watermark_font(self,
                           font: ImageFont.truetyp):
        """
        Set font like ImageFont.truetype('Arial bold', 24)
        :param font: ImageFont.truetype
        :return: None
        """
        if not isinstance(font, ImageFont.truetype):
            raise ValueError("Incorrect typy of variable")

        self.font = font
