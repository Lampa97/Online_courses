from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    preview = models.ImageField(upload_to="courses/", default="courses/default_course.png", verbose_name="Preview")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    preview = models.ImageField(upload_to="lessons/", default="lessons/default_lesson.png", verbose_name="Preview")
    video_link = models.URLField(verbose_name="Video link")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Course")

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["title"]

    def __str__(self):
        return self.title