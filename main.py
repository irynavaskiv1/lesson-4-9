import package_functions
import package_images.Im_PIL
from package_classes import (MyClassFDigitDetector, MyClassCV,
                             MyClassCVFileReader, MyClassCVFileWriter)
from package_functions import module_1, module_2, module_3
import logging


logging.basicConfig(filename='main.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def package_functions_main_def():
    logger.info('Call module 1')
    a = 10.0
    h = 22.0
    test_1 = module_1.area_triangle(a, h)
    print('Area of triangle: ', ' S =', test_1, '\n')
    logger.info('Call module 2')

    module_2.my_fun(10)
    module_2.student(firstname='Python_1', lastname='C#_1')
    module_2.student(lastname='C#_2', firstname='Python_2')
    module_2.name_age("Python_1", 27)
    module_2.name_age(27, "Python_1")

    logger.info('Call module 3')
    a = 100.0
    h = 22.0
    in_s = dict(result='Area of triangle', triangle_parameter_a=a, triangle_parameter_h=h)
    package_functions.module_3.example_dict(in_s)
    # print(f'result =ckage_functions.module_3.example_dict(in_s)['out'])
    return


def package_class_main_def():
    obj_1 = MyClassCV()
    obj_2 = MyClassCVFileWriter()
    obj_3 = MyClassCVFileReader()
    obj_4 = MyClassFDigitDetector()

    FILE_NAME = "Vaskiv_CV.csv"
    my_cv_dict_out = obj_1.my_cv_dict()
    obj_2.my_cv_file_w(FILE_NAME, my_cv_dict_out)
    text_in = obj_3.my_cv_file_r(FILE_NAME)
    obj_4.f_digit_detector(text_in)

    return


def package_image_main_def():
    file_name_start = 'sentinel_2023.jpg'
    file_name_stop = "stop.jpg"
    file_name_filter = "stop_filter.jpg"

    transformations = {
        0: package_images.Im_PIL.shades_of_gray,
        1: package_images.Im_PIL.serpia,
        2: package_images.Im_PIL.negative,
        3: package_images.Im_PIL.noise,
        4: package_images.Im_PIL.brightness_change,
        5: package_images.Im_PIL.monochrome,
        6: package_images.Im_PIL.contour_im
    }

    print('Select the type of transformation:')
    print('0 - Shades of Gray')
    print('1 - Sepia')
    print('2 - Negative')
    print('3 - Noise')
    print('4 - Brightness Change')
    print('5 - Monochrome Image')
    print('6 - Contour Filter')

    try:
        mode = int(input('Mode: '))
        if mode in transformations:
            # Call the appropriate function based on the mode
            transformations[mode](file_name_start, file_name_stop) if mode < 6 else transformations[mode](file_name_stop, file_name_filter)
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a number.")

    return


if __name__ == '__main__':
    package_functions_main_def()
    package_class_main_def()
    package_image_main_def()
