from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SingleForm, SingleModelForm, UploadFormSet, ModelFormSet, MultipleForm
from .models import Image



class SingleView(generic.FormView):
    form_class = SingleForm
    template_name = 'album/base.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)


class SingleWithModelView(generic.CreateView):
    """ファイルモデルのアップロードビュー"""
    model = Image
    form_class = SingleModelForm
    template_name = 'album/base.html'
    success_url = reverse_lazy('album:file_list')


class FileListView(generic.ListView):
    """アップロードされたファイルの一覧ページ"""
    model = Image


class MultiView(generic.FormView):
    form_class = UploadFormSet
    template_name = 'album/base.html'

    def form_valid(self, form):
        download_url_list = form.save()
        context = {
            'download_url_list': download_url_list,
            'form': form,
        }
        return self.render_to_response(context)


def multi_upload_with_model(request):
    formset = ModelFormSet(request.POST or None, files=request.FILES or None, queryset=Image.objects.none())
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('album:file_list')

    context = {
        'form': formset
    }

    return render(request, 'album/base.html', context)


class InputMultiView(generic.FormView):
    form_class = MultipleForm
    template_name = 'album/base.html'

    def form_valid(self, form):
        download_url_list = form.save()
        context = {
            'download_url_list': download_url_list,
            'form': form,
        }
        return self.render_to_response(context)


