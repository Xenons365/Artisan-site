from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import ArtModel

class ArtModelValidationTest(TestCase):
    def test_title_and_price_are_required(self):
        """
        Test that creating an ArtModel with no title or price raises a ValidationError.
        """
        with self.assertRaises(ValidationError) as cm:
            art = ArtModel()
            art.full_clean()

        the_exception = cm.exception
        self.assertIn('title', the_exception.message_dict)
        self.assertIn('price', the_exception.message_dict)

    def test_description_is_optional(self):
        """
        Test that an ArtModel can be created with a title and price but no description.
        """
        try:
            art = ArtModel(title="Test Art", price=10.00)
            art.full_clean()
            art.save()
        except ValidationError:
            self.fail("ArtModel should be valid with a title and price, but no description.")

        self.assertEqual(ArtModel.objects.count(), 1)
        self.assertEqual(ArtModel.objects.first().title, "Test Art")