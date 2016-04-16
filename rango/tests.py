from django.test import TestCase
from rango.models import Category, Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone

# Create your tests here.
def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        ensure_views_are_positive should results True for categories where views are zero or positive
        """
        cat = Category(name='test',views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)    

    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
        i.e. "Random Category String" -> "random-category-string"
        """

        cat = Category(name='Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')

        
        
class PageMethodTests(TestCase):
    def test_last_visit_not_in_the_future(self):
        """
        Test to ensure the last_visit is not in the future
        """
        cat = Category(name='test',views=1, likes=0)
        cat.save()
        page, created = Page.objects.get_or_create(category=cat, title='test', 
                url="www.test.test", views=1, first_visit=timezone.now(), last_visit=timezone.now() - timezone.timedelta(hours=1))       
        page.save()
        self.assertTrue(page.last_visit < timezone.now(), "Last_visit is in the future")
    
class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])    
    def test_index_view_with_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """

        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cats =len(response.context['categories'])
        self.assertEqual(num_cats , 4)