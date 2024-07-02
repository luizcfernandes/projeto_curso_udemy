from django.urls import reverse, resolve
# from unittest import skip
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeViewsCategoryTest(RecipeTestBase):
    def testeRecipeCategoryViewsFunctionIsCorrect(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        print("Category Views Function está correta")
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_returns_404_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category',
                    kwargs={'category_id':4}))    # noqa E501
        print("Category Views retorna status 404")
        self.assertEqual(response.status_code, 404)

    def test_recipeCategoryTemplateDontLoadRecipesNotPublished(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )
        
        print("Recipes Recipe Template Dont Loads Recipes Not PUblished")
        self.assertEqual(response.status_code, 404)
       
        # função para pular o teste 
        # self.skipTest('pulando esse teste') 

    def test_recipeCategoryTemplateLoadsRecipes(self):
        need_title = 'This is a title'
        self.make_recipe(title=need_title)
        response = self.client.get(reverse('recipes:category', args=(1, )))
        content = response.content.decode('utf-8')

        self.assertIn(need_title, content)

