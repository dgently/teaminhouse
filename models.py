import peewee as pw 


db = pw.SqliteDatabase('inhousekeeper.db')

class BaseModel(pw.Model):
	class Meta:
		database=db

class Status(BaseModel):
	status=pw.CharField()
	color=pw.CharField()

class Artist(BaseModel):
	first = pw.CharField()
	last = pw.CharField()
	hostname = pw.CharField()
	email = pw.CharField()

class ShotType(BaseModel):
	shotType=pw.CharField()
	color=pw.CharField()
	description=pw.TextField()


class Shot(BaseModel):
	name = pw.CharField()
	description = pw.TextField()
	status = pw.ForeignKeyField(Status, related_name='shots')
	currentArtist = pw.ForeignKeyField(Artist, related_name='shots')
	turnoverDate = pw.DateField()
	modified = pw.DateTimeField()
	shared = pw.BooleanField()
	shotType=pw.ForeignKeyField(ShotType,related_name='shots')


class Submission(BaseModel):
	artist = pw.ForeignKeyField(Artist, related_name='submissions')
	date = pw.DateTimeField()
	artistNote = pw.TextField()
	clientNote = pw.TextField()
	shot = pw.ForeignKeyField(Shot, related_name='submissions')
	versionName = pw.CharField()