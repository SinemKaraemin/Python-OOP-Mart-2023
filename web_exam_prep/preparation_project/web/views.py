from django.shortcuts import render

# Create your views here.


def home_page(request):
    # TODO check template!
    return render(request, 'web/home-no-profile.html')


def add_album(request):
    return render(request, 'web/add-album.html')


def album_details(request, id):
    return render(request, "web/album-details.html")


def album_edit(request, id):
    return render(request, "web/edit-album.html")


def album_delete(request, id):
    return render(request, "web/delete-album.html")


def profile_details(request):
    return render(request, "web/profile-details.html")


def profile_delete(request):
    return render(request, "web/profile-delete.html")
