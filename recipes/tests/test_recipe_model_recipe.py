from recipes.tests.test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(nome='Teste Default'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='dsfs',
            slug='modelo-ok-ok0k',
            preparation_time=3,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='pessoas',
            preparation_steps='Ipsum factum dominus lorum',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_RecipeTitleRaisesErrorIfTitleMoreThan65Chars(self):
        self.recipe.title = 'A' * 70
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand([
        ('title', 65),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
        ('description', 165),
    ])
    def test_RecipeFieldsMaxLength(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipePreparationStepsIsHtmlIsFalseByDefault(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html,
                         msg='Recife preparation is Html is not False')
    
    def test_recipeIsPublishedIsFalseByDefault(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published,
                         msg='Recife is_published is not False')
        
    def test_recipeStringRepresentation(self):
        needed = 'Testing Representation'
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed,
                         msg=f'String Representation is diferente de "{needed}" ')
        
    def test_RecipeDeveGerarErroAoGravarSlugExistente(self):
        self.receita = self.make_recipe_no_defaults()
        slug = 'modelo-ok-ok'
        setattr(self.receita, 'slug', slug)
        with self.assertRaises(ValidationError):
            self.receita.full_clean()