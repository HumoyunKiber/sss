from django.db import models as m

class Home(m.Model):
    title = m.CharField(max_length=255)
    info = m.CharField(max_length=255)
    background = m.CharField(max_length=255)

class Course(m.Model):
    name = m.CharField(max_length=255)
    info = m.TextField()
    thumb = m.ImageField(upload_to='thumbs/')
    date = m.DateField(auto_now_add=True)
    link = m.URLField()

    def __str__(self):
        return self.name

class Post(m.Model):
    title = m.CharField(max_length=255)
    info = m.TextField()
    date = m.DateField(auto_now_add=True)
    thumb = m.ImageField(upload_to='thumbs/')

    def __str__(self):
        return self.title

class PostImages(m.Model):
    post = m.ForeignKey(Post, on_delete=m.CASCADE)
    image = m.ImageField(upload_to="post/")

    def __str__(self):
        return self.post.title
    

class Member(m.Model):
    name = m.CharField(max_length=255)
    job = m.CharField(max_length=255)
    image = m.ImageField(upload_to="member/")
    main = m.BooleanField(default=False)

    def __str__(self):
        return self.name