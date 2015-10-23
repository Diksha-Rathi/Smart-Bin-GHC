from django.db import models

# Create your models here.
class bin_info(models.Model):
	location_id = models.CharField(max_length=60,blank=False,unique=False)
	bin_id = models.CharField(max_length=30,blank=True,null=True,unique=False)
	fill_level = models.IntegerField(blank=False,unique=False)
	humidity = models.IntegerField(blank=False,unique=False)
	temperature = models.IntegerField(blank=False,unique=False)

	def __unicode__(self):
    		return u'%s %s %d %d %d' % (self.location_id, self.bin_id, self.fill_level, self.humidity, self.temperature)

	class Meta:
			ordering = ['id']
