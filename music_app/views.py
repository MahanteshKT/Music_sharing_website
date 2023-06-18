from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import MusicFile
from django.db import models

# views here.
@login_required
def homepage(request):
    user=request.user
    
    #all music files uploaded by logged-user
    User_upload_files=MusicFile.objects.filter(
        models.Q(visibility=MusicFile.PUBLIC,uploaded_by=user)|
        models.Q(visibility=MusicFile.PRIVATE,uploaded_by=user)|
        models.Q(visibility=MusicFile.PROTECTED,uploaded_by=user)
    ).order_by('-date_posted')
    
    # GETTING THE ALL PUBLIC MUSIC FILES
    public_files=MusicFile.objects.filter(
        models.Q(visibility=MusicFile.PUBLIC)
    ).order_by('-date_posted')

    protected_files=MusicFile.objects.filter(
        models.Q(visibility=MusicFile.PROTECTED,allowed_users=user)
    ).order_by('-date_posted')

    #to get all music files containing the private,public,protected of user
    # music_files=MusicFile.objects.filter(
    #     models.Q(visibility=MusicFile.PUBLIC)|
    #     models.Q(visibility=MusicFile.PRIVATE,uploaded_by=user)|
    #     models.Q(visibility=MusicFile.PROTECTED,allowed_users=user)
    #     )
    
    context={
        'title':'HomePage',
        'public_files':public_files,
        'User_upload_files':User_upload_files,
        'protected_files':protected_files,
    }

    return render(request,'music-app/HomePage.html',context)


# ABOUT PAGE FUNCTION
def aboutpage(request):
    context={
        'title':'AboutPage'
    }
    return render(request,"music-app/AboutPage.html",context)

# UPLOADMUSIC METHOD
@login_required
def uploadMusic(request):
    if request.method=="POST":
        user=request.user
        title = request.POST['title']
        music_file = request.FILES.get('file')
        visibility = request.POST.get('visibility')
        print(visibility)
        musicFile = MusicFile(title=title, music_file=music_file, visibility=visibility, uploaded_by=user)
        musicFile.save()
        if visibility == MusicFile.PROTECTED:
            allowed_emails = request.POST.get('allowed_emails', '').split(',')
            allowed_users=User.objects.filter(email__in=allowed_emails)
            print(allowed_users)
            musicFile.allowed_users.set(allowed_users)

        messages.success(request,f"Music file Uploaded Successfully.!")
        return redirect("HomePage")
        
    context={
        'title':'Upload'
    }
    return render(request,"music-app/UploadMusic.html",context)


