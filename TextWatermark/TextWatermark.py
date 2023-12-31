"""

Text watermark class
#100DaysOfCode with Python
Day: 84
Date: 2023-07-02

"""

from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image


class TextWatermark:

    # WATERMARK_TEXT_FONT = ImageFont.truetype('arial.ttf', 24)
    # WATERMARK_TEXT_FONT = ('Arial bold', 24)
    WATERMARK_TEXT_FONT = ('Arial bold', 24)
    WATERMARK_TEXT_FG = (255, 255, 255)

    def __init__(self):
        self.draw = None
        self.watermark_text = None
        self.fill_fg = self.WATERMARK_TEXT_FG
        self.font = ImageFont.truetype('NewYork.ttf', 36)
        # self.font = ImageFont.load_default()
        self.image = None

    def put_watermark_on_image(self,
                               image=None,
                               text_watermark=None,
                               fill_fg=None,
                               font=None):

        if image is not None:
            self.set_image(image)

        if text_watermark is not None:
            self.set_watermark_text(text_watermark)

        if fill_fg is not None:
            self.set_watermark_fill_fg(fill_fg)

        if font is not None:
            self.set_watermark_font(font)

        self.draw.text(
            (100, 100),
            self.watermark_text,
            fill=self.fill_fg,
            font=self.font,
            anchor='ms'
        )

    def save_watermark_image(self, path):
        if path is None:
            raise ValueError('Path must be set!')

        self.image.save(path)

    def set_image(self,
                  image):
        """
        set image to watermark ;)
        :param image:
        :return:
        """
        # if not isinstance(image, ImageDraw):
        #     raise ValueError("Incorrect value, must be ImageDraw")

        img = Image.open(image)
        self.image = img.copy()

        self.draw = ImageDraw.Draw(self.image)

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

    def get_watermark_fill_fg(self) -> list:
        """
        :return: fill list as RGB like (0, 0, 0)
        """
        return self.fill_fg

    def set_watermark_fill_fg(self,
                              fill: list):
        """
        set fill for watermark text as (0, 0, 0) RGB
        :param fill:
        :return:
        """
        if fill is None:
            raise ValueError("Fill must be set!")

        self.fill_fg = fill

    # def get_watermark_font(self) -> ImageFont.truetype:
    #     """
    #     :return: watermark text font as ImageFont.truetype
    #     """
    #     return self.font

    # def set_watermark_font(self,
    #                        font: ImageFont.truetype):
    #     """
    #     Set font like ImageFont.truetype('Arial bold', 24)
    #     :param font: ImageFont.truetype
    #     :return: None
    #     """
    #     if not isinstance(font, ImageFont.truetype):
    #         raise ValueError("Incorrect typy of variable")
    #
    #     self.font = font


# some testes
if __name__ == '__main__':
    x = TextWatermark()
    # x.set_watermark_font(ImageFont.truetype('arial.ttf', 24))
    x.set_watermark_text('chinek01')
    x.set_watermark_fill_fg((255, 0, 0))
    x.set_image('test_img/test_img.jpg')
    x.put_watermark_on_image()
    x.save_watermark_image('test_img/test_img_wm.jpg')
