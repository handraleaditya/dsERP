from enum import auto
from django.db import models
from django.urls import reverse
import uuid

# Project model
'''
- should have a key to project manager
- every request needs to belong to a project

'''
class Project(models.Model):
    name = models.CharField(max_length=256, help_text="Enter the name of the project")

    def __str__(self):
        return self.name

# Approval model
'''
- should have decline comment
- should have acknowledgement(as object or in itself)
- should have status and isApproved? (bool and dropdown)
- 
'''

class Approval(models.Model):
    # Attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this approval")

    title = models.CharField(max_length=256, help_text="Enter the title for the request")
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, help_text="Select the project for this approval")
    
    description = models.TextField(max_length=1024, blank=True, help_text="Enter the description of this request")
    amount = models.FloatField()
    
    beneficiary = models.CharField(max_length=256, help_text="Enter the name of the beneficiary")
    beneficiary_account = models.CharField(max_length=256, help_text="Enter the bank account number of the beneficiary")
    
    # created_by = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_OPTIONS = (
        ('p', "Processing"),
        ('a', "Approved"),
        ('d', "Declined"),
        ('c', "Commented"))
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, blank=True, default='p', help_text="Select the status of the approval" )
    
    
    # Methods
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('approval-detail', args =[str(self.id)])

    class Meta:
        ordering = ['created_at']

# User model
# class User(models.Model):
