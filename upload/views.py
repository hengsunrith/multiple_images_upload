# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from upload.forms import PostForm, ImageForm
from upload.models import Images
from django.forms.models import modelformset_factory

def get(request):
    images = Images.objects.all()
    return render(request, 'upload/display.html', {'images':images})

def post(request):

    # ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)

    if request.method == 'POST':

        postForm = PostForm(request.POST)
        # formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            # for form in formset.cleaned_data:
            #     image = form['image']
            #     photo = Images(post=post_form, image=image)
            #     photo.save()

            for f in request.FILES.getlist('image'):
                photo = Images(post=post_form, image=f)
                photo.save()

            return HttpResponseRedirect("/")
        else:
            print postForm.errors
    else:
        postForm = PostForm()
        # formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'upload/index.html', {'postForm': postForm}, )