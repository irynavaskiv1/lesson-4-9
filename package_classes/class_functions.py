import re
import sys


class MyClassCV:
    """ DESCRIPTION OF THE ALGORITHM by OPP mechanisms """

    def my_cv_dict(self) -> dict:
        """
        Creates a dictionary containing personal information and programming skills.

        Returns:
            dict: A dictionary with the following keys:
                - 'name': The name of the person.
                - 'birth_year': The year of birth.
                - 'age': The age of the person.
                - 'programming_languages': A list of programming languages known.
                - 'favorite_numbers': A set of favorite numbers.

        Prints:
            Information about the person, including their name, birth year,
            age, programming languages, and favorite numbers.
        """

        my_name = "Iryna Vaskiv"
        my_birth_year = "1996"
        age = "28"
        my_programming_languages = ["Python", "C#", "Java", "C++"]
        my_favorite_numbers = {3, 5, 7, 12}

        my_cv_dict = {
            "name": my_name,
            "birth_year": my_birth_year,
            "age": age,
            "programming_languages": my_programming_languages,
            "favorite_numbers": my_favorite_numbers,
        }

        print("My name is:", my_cv_dict["name"])
        print("My birth year is:", my_cv_dict["birth_year"])
        print("My age is:", my_cv_dict["age"])

        print("I can solve problems using these programming languages:")
        for lang in my_cv_dict["programming_languages"]:
            print(lang)

        print("My favorite numbers:")
        print(my_cv_dict["favorite_numbers"])

        return my_cv_dict


class MyClassCVFileWriter:
    """Class record my_cv to the file"""

    def my_cv_file_w(self, FILE_NAME_csv: str, my_cv_dict: dict) -> None:
        """
        Writes the CV information from a dictionary to a CSV file.

        Args:
            file_name_csv (str): The name of the CSV file to write to.
            my_cv_dict (dict): A dictionary containing CV information.

        Raises:
            PermissionError: If there is a permission issue with the file.
            Exception: For any other exceptions that may occur during file writing.
        """
        my_cv_str = str(my_cv_dict)
        try:
            with open(FILE_NAME_csv, "w", encoding="UTF-8") as file:
                file.writelines(my_cv_str)
        except PermissionError:
            print("Sorry, you have no access to this file")
        except Exception as error:
            print(f"It looks like something has happened. This is {error}")

        return


class MyClassCVFileReader:

    def my_cv_file_r(self, FILE_NAME: str) -> list:
        """
        Reads the contents of a specified file and returns them as a list of strings.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            list: A list containing the lines from the file, stripped of whitespace.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        text = []
        try:
            with open(FILE_NAME, 'r') as f:
                for j in f:
                    text.append(j.strip() + " ")
        except FileNotFoundError as exeption:
            print(f'Sorry, the file {exeption}')
            sys.exit(0)
        return text


class MyClassFDigitDetector:
    """" record mi_tsv to the fillet"""

    def f_digit_detector(self, text: list) -> None:
        """
        Detects digits in the provided list of strings, increments each detected digit by 25,
        and returns a list of the modified digits.

        Args:
            text (list): A list of strings to search for digits.

        Returns:
            list: A list of digits as strings, each incremented by 25.
        """
        digit_detector = re.findall('[0-9]+', str(text))

        for i in range((len(digit_detector))):
            digit_detector[i] = str(int(digit_detector[i]) + 25)
        return
