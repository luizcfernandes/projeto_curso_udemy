

from django.forms import ValidationError
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            nome='Category Testing'
        )
        return super().setUp()
    
    def test_RecipeCategoryMOdelStringRepresentation(self):
        needed = 'Category Testing'
        self.assertEqual(
            str(self.category),
            needed
        )

    def test_recipeCagegoryModeNameMaxLength(self):
        self.category.name = 'A' * 70
        with self.assertRaises(ValidationError):
            self.category.full_clean()