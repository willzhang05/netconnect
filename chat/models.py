'''***************************************************************************************
*  REFERENCES
*  Title: chatty
*  Author: SteinOveHelset
*  Date: Mar/28/21
*  URL: https://github.com/SteinOveHelset/chatty
*  URL2: https://www.youtube.com/watch?v=wLwu1NqU1rE
*
*  Title: chatty
*
***************************************************************************************'''

from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
