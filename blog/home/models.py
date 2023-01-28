from django.db import models




class Post(models.Model):
  title = models.CharField(max_length = 250)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  
  def __str__(self):
        return self.title

class Comment(models.Model):
  text = models.CharField(max_length = 250)
  post_id = models.ForeignKey("Post" , on_delete=models.CASCADE)

  def __str__(self):
    return self.text