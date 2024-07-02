from django.urls import reverse, resolve
# from unittest import skip
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


# @skip('pulando toda a classe de testes ') 
class RecipeViewsTest(RecipeTestBase):
    def test_RecipeDetailViewsFunctionIsCorrect(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        print("Recipe Views Function está correta")
        self.assertIs(view.func, views.recipe)
   
    def test_recipeDetailViewReturns404IfNoRecipesFound(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 5})
        )
        print("Recipe Details retorna erro 404 se nao encontrado!")
        self.assertEqual(response.status_code, 404)

        # faz o teste falhar
        # self.fail("para continuar daqui")

    def test_RecipeDetailTemplateLoadsTheCorretRecipe(self):
        need_title = 'This is a detail page - load one recipe'
        
        self.make_recipe(title=need_title)
        
        response = self.client.get(reverse('recipes:recipe', args=(1, )))
        content = response.content.decode('utf-8')

        self.assertIn(need_title, content)
    
    def test_recipeDetailTemplateDontLoadRecipeNotPublished(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id})
        )
        
        print("Recipes Recipe Template Dont Loads Recipes Not PUblished")
        self.assertEqual(response.status_code, 404)
       
   
