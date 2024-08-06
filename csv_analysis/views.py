from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UploadFileForm
from .models import MyModel
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import urllib.parse

class HomeView(TemplateView):
    template_name = 'csv_analysis/home.html'

class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'csv_analysis/upload.html'

    def form_valid(self, form):
        my_model_instance = form.save()
        try:
            df = pd.read_csv(my_model_instance.file.path)
            plt.figure()
            if not df.select_dtypes(include='number').empty:
                sns.histplot(df.select_dtypes(include='number'))
                plt.title('Histogram for Numerical Columns')
            else:
                plt.text(0.5, 0.5, 'No numerical columns to plot', horizontalalignment='center')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read()).decode()
            uri = urllib.parse.quote(string)
            
            context = {
                'head': df.head().to_html(),
                'describe': df.describe().to_html(),
                'missing': df.isnull().sum().to_html(),
                'plot': uri
            }
            return self.render_to_response(context)
        except Exception as e:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response({'form': form, 'error': 'Error processing file'})
