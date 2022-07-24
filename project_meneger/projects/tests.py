from django.test import TestCase, Client
from .views import *
from .forms import Edit_form
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class Test_views(TestCase):
    def setUp(self):
        self.client=Client()
        self.project1=Project.objects.create(id=1,name='ss',describtion='sss',deadline='2022-07-30')
    def test_index(self):
        request=self.client.get('/')
        self.assertEqual(request.status_code, 200)
    def test_edit(self):
        self.project1.workers.set(User.objects.all())
        #get request
        request_get=self.client.get('/edit/1')
        self.assertTemplateUsed(request_get,'edit.html')
        self.assertEquals(request_get.status_code,200)
        #post request
        request_post=self.client.post('/edit/1',{'name':'aa','describtion':'aaa', 'deadline':'2022-07-30'})
        self.assertEquals(request_post.status_code,302)
    def test_add(self):
        #get request
        request_get=self.client.get('/add')
        self.assertEqual(request_get.status_code,200)
        #post request
        request_post=self.client.post('/add',{'name':'jaja','describtion':'jajka','dedline':'2022-08-04'})
        self.assertAlmostEqual(request_post.status_code,302)
    def test_delete(self):
        request=self.client.get('/delete/1')
        self.assertEqual(request.status_code,302)

class Test_forms(TestCase):
    def test_Edit_form_valid_data(self):
        form=Edit_form(data={'name':'coffe','describtion':'costs','deadline':'2022-05-13','workers':User.objects.all()})
        self.assertTrue(form.is_valid())

    def test_Edit_form(self):
        form=Edit_form(data={})
        self.assertFalse(form.is_valid())

class Test_models(TestCase):
    def test_blank_fields(self):
        project=Project.objects.create(name='test')
        self.assertEqual(project.describtion,'')
        self.assertEqual(project.deadline, None)
        self.assertFalse(project.workers.all().exists())