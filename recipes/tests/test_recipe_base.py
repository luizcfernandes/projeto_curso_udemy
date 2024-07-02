
from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_category(self, nome='Peixes'):
        return Category.objects.create(name=nome)

    def make_author(
            self,
            first_name='user',
            last_name='user',
            username='username',
            password='123',
            email='email@gmail.com'):
        return User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
    
    def make_recipe(
            self,
            category_data=None,
            author_data=None,
            title='Recipe Title',
            description='dsfs',
            slug='modelo-ok-ok',
            preparation_time=3,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='pessoas',
            preparation_steps='Ipsum factum dominus lorum',
            preparation_steps_is_html=False,
            is_published=True,
    ):
        if (category_data is None):
            category_data = {}
        if (author_data is None):
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
