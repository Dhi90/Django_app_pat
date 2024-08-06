from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import MyModel
from .forms import UploadFileForm
from django.urls import reverse

class MyModelTestCase(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.csv_file = SimpleUploadedFile(
            "test.csv", b"name,age,height,weight\nAlice,30,5.5,140\nBob,25,5.9,150"
        )

    def test_model_creation(self):
        # Test creating a MyModel instance.
        my_model_instance = MyModel.objects.create(file=self.csv_file)
        self.assertEqual(MyModel.objects.count(), 1)
        self.assertEqual(my_model_instance.file.name, 'csv_files/test.csv')

    def test_upload_file_form(self):
        # Test the UploadFileForm
        form_data = {}
        file_data = {'file': self.csv_file}
        form = UploadFileForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid())

    def test_upload_view(self):
        # Test the upload view
        response = self.client.post(reverse('upload_file'), {'file': self.csv_file})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Analysis Results')
        self.assertContains(response, 'Alice')
        self.assertContains(response, 'Bob')
