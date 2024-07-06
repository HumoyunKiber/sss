from django.shortcuts import render, get_object_or_404
from .models import Post,Course,Member

def index(request):
    posts = Post.objects.order_by('-date')[:3]
    courses = Course.objects.order_by('-date')[:3]
    members = Member.objects.filter(main=True)
    context = {
        'posts' : posts,
        'courses' : courses,
        'members' : members,
    }
    return render(request,'index.html',context)

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request,'posts.html',context)

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request,'courses.html',context)


def members(request):
    members = Member.objects.all()
    context = {
        'members' : members,
    }
    return render(request,'members.html',context)





def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_images = post.postimages_set.all()  # Fetch all related images
    context = {
        'post': post,
        'post_images': post_images,
    }
    return render(request, 'post_detail.html', context)


def course_details(request,course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course' : course,
    }
    return render(request,'course-details.html',context)