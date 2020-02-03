from django import forms
from django.core.files.storage import default_storage
from .models import Image


class SingleForm(forms.Form):
    file = forms.ImageField(label='画像ファイル')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)


class SingleModelForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'


class BaseFormSet(forms.BaseFormSet):

    def save(self):

        url_list = []


        for form in self.forms:
            try:
                url = form.save()
            except KeyError:

                pass
            else:
                url_list.append(url)
        return url_list


UploadFormSet = forms.formset_factory(SingleForm, formset=BaseFormSet, extra=5)

ModelFormSet = forms.modelformset_factory(
    Image, form=SingleModelForm,
    extra=3
)


class MultipleForm(forms.Form):
    file = forms.ImageField(
        label='画像ファイル',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    def save(self):
        url_list = []
        for upload_file in self.files.getlist('file'):
            file_name = default_storage.save(upload_file.name, upload_file)
            file_path = default_storage.url(file_name)
            url_list.append(file_path)
        return url_list




