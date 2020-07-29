from django.db import models

# Create your models here.

class Pipe(models.Model):
	"""A topic the user is learning about."""
	ex_diameter = models.IntegerField(verbose_name='Diameter (in mm)', null=True, blank=False)
	ex_length = models.DecimalField(verbose_name='Culvert Length (in m)', max_digits=7, decimal_places=4, null=True, blank=False)
	ex_inlet = models.DecimalField(verbose_name='Inlet IL (in m)', max_digits=7, decimal_places=4, null=True, blank=False) 
	ex_outlet = models.DecimalField(verbose_name='Outlet IL (in m)', max_digits=7, decimal_places=4, null=True, blank=False) 
	EX_CONSTRUCTION_CHOICES = [
	('brick', 'Brick'),
	('concrete', 'Concrete'),
	('clayware', 'Clayware'),
	('corrugated metal', 'Corrugated Metal'),
	('UV CIPP liner', 'UV CIPP Liner'),
	('HDPE plastic pipe', 'HDPE Plastic Pipe'),
	]
	ex_construction = models.CharField(verbose_name='Construction', max_length=100, choices=EX_CONSTRUCTION_CHOICES)

	pro_diameter = models.IntegerField(verbose_name='Diameter (in mm)', null=True, blank=False)
	pro_length = models.DecimalField(verbose_name='Culvert Length (in m)', max_digits=7, decimal_places=4, null=True, blank=False)
	pro_inlet = models.DecimalField(verbose_name='Inlet IL (in m)', max_digits=7, decimal_places=4, null=True, blank=False) 
	pro_outlet = models.DecimalField(verbose_name='Outlet IL (in m)', max_digits=7, decimal_places=4, null=True, blank=False) 
	PRO_CONSTRUCTION_CHOICES = [
	('brick', 'Brick'),
	('concrete', 'Concrete'),
	('clayware', 'Clayware'),
	('corrugated metal', 'Corrugated Metal'),
	('UV CIPP liner', 'UV CIPP Liner'),
	('HDPE plastic pipe', 'HDPE Plastic Pipe'),
	]
	pro_construction = models.CharField(verbose_name='Construction', max_length=100, choices=PRO_CONSTRUCTION_CHOICES, null=True)
	

class Liner(models.Model):

	diameter = models.IntegerField(verbose_name = 'Existing Diameter (in mm)', null=True, blank=False)
	SHAPE_CHOICES = [
	('circular', 'Circular'),
	('non-circular', 'Non-Circular')
	]
	shape = models.CharField(max_length=100, choices=SHAPE_CHOICES, null=True)
	distance = models.DecimalField(verbose_name='Rail to Sleeper Distance (in m)', max_digits=7, decimal_places=4, null=True, blank=False)