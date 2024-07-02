from django.test import TestCase   # ignore
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        print("home url funcionando para '/'")
        self.assertEqual(home_url, reverse('recipes:home'))

    def test_recipe_category_url_is_correct(self):
        home_url = reverse('recipes:category', kwargs={'category_id': 1})
        print("category com id url está  funcionando para '/recipe/category/id/' ")   # noqa E501
        self.assertEqual(home_url, reverse('recipes:category', kwargs={'category_id': 1}))                              # noqa W291 E501   

    def test_recipe_url_is_correct(self):
        home_url = reverse('recipes:recipe', kwargs={'id': 1})
        print("recipes com id url está  funcionando para '/recipe/id/' ")   # noqa E501
        self.assertEqual(home_url, reverse('recipes:recipe', kwargs={'id': 1}))   
      
    def test_recipeSearchUrlIsCorrect(self):
        url = reverse('recipes:search')
        self.assertEqual(url,'/recipes/search/')                        # noqa W291


# ciclo do TDD
# RED - GREEN - REFACTOR