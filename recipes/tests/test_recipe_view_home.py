from django.urls import reverse, resolve
# from unittest import skip
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeViewsHomeTest(RecipeTestBase):
    def testeRecipeHomeViewsFunctionIsCorrect(self):
        view = resolve(reverse('recipes:home'))
        print("Home Views Function está correta")
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_Ok(self):
        response = self.client.get(reverse('recipes:home'))
        print("Home Views retorna status 200")
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_LoadsCorrectTemplate(self):
        response = self.client.get(reverse('recipes:home'))
        print("Home Views retorna Template ")
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    def test_recipeHomeShowsNoRecipesFoundNoRecipes(self):
        response = self.client.get(reverse('recipes:home'))
        print('Home Shows No Recipes Found No Recipes')
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8'))
    
    def test_receipeHomeTemplateLoadsRecipes(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        print("Recipe Home Template Dont Loads Recipes")
        self.assertIn(
            'No recipes found here 🙄',
            response.content.decode('utf-8')
        )

    def test_recipeHomeTemplateDontLoadRecipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']
        response_context = response.content.decode('utf-8')

        print("Recipe Home Template Loads Recipes")
        self.assertEqual(len(response.context['recipes']), 1)
        self.assertEqual(response_recipes.first().title, 'Recipe Title')
        self.assertIn(
            'Recipe Title',
            response_context
        )