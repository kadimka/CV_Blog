from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Task(models.Model):
    progress = (
        ('Plan', 'Plan'),
        ('Task', 'Task'),
        ('Process', 'Process'),
        ('Done', 'Done'),
    )

    task_name = models.CharField(max_length=300)
    task_progress = models.CharField(max_length=100, choices=progress, default='Plan')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task_name



# Create your models here.
