class complex_number:

    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return complex_number(real, imaginary)

    def __iadd__(self, other):
        self.real_part += other.real_part
        self.im_part += other.im_part
        return self