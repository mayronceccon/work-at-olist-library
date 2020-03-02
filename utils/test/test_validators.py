from django.test import TestCase
from django.core.exceptions import ValidationError
from utils.validators import year_validator


class YearValidatorTest(TestCase):
    def test_year_validator_correct(self):
        self.assertEqual(None, year_validator(2019))

    def test_year_validator_incorrect_above(self):
        with self.assertRaises(ValidationError):
            year_validator(3000)

    def test_year_validator_incorrect_below(self):
        with self.assertRaises(ValidationError):
            year_validator(-1000)
