from django.urls import reverse, resolve
# from unittest import skip
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeViewsSearchTest(RecipeTestBase):
    def test_RecipeSearchUsesCorrectViewFunction(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
        # função para pular o teste 
        # self.skipTest('pulando esse teste') 

    def test_recipeSearchLoadsCorrectTemplate(self):
        url = reverse('recipes:search') + '?q=teste'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def testRecipeSearchRaises404IfNoSearchTerm(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_RecipeSearchTermIsOnPageTitleAndEscaped(self):
        url = reverse('recipes:search') + '?q=<teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_RecipeCanFindRecipeByTitle(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = self.make_recipe(
            slug='one',
            title=title1,
            author_data={'username': 'C1net1ca@', },
        )
        recipe2 = self.make_recipe(
            slug='two',
            title=title2,
            author_data={'username': 'C1net1ca@2', },
        )

        search_url = reverse('recipes:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(
            recipe1,
            response1.context['recipes']
        )
        self.assertIn(
            recipe2,
            response2.context['recipes']
        )

        self.assertIn(
            recipe1,
            response_both.context['recipes']
        )

        self.assertIn(
            recipe2,
            response_both.context['recipes']
        )
        self.assertNotIn(
            recipe2,
            response1.context['recipes']
        )

        