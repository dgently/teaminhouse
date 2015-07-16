import models as m
import peewee
import re

def get_shots_simple_row(fA,fS,fT):
	allA= (fA == 'ALL')
	allS= (fS=='ALL')
	allT= (fT=='ALL')
		

	query = (m.Shot
					.select(m.Shot,m.Artist,m.Status,m.ShotType)
					.join(m.Artist)
					.switch(m.Shot)
					.join(m.Status)
					.switch(m.Shot)
					.join(m.ShotType)
					.where(((m.Artist.first==fA) | allA)&((m.Status.status==fS) | allS) & ((m.ShotType.shotType==fT)|allT))
					)
	return query

def get_current_submission_note(shot):
		try:
			r = shot.submissions.order_by(m.Submission.date)[0].clientNote
		except IndexError:
			r=''

		return r 


def get_current_submission_version(shot):
		try:
			r = shot.submissions.order_by(m.Submission.date)[0].versionName[-4:]
			
		except IndexError:
			r=''
		return r 

def populate_artists(box):
	
	for a in m.Artist:
		box.addItem(a.first)	

def populate_types(box):
	
	for a in m.ShotType:
		box.addItem(a.shotType)

def populate_status(box):
	
	for a in m.Status:
		box.addItem(a.status)

def update_shot_attribute(shot, field, value):
	db_shot = m.Shot.get(name=shot)
	if field=='artist_box':
		
		db_shot.currentArtist = m.Artist.get(first=value)

	if field=='status_box':
		
		db_shot.status=m.Status.get(status=value)

	if field=='type_box':
		
		db_shot.shotType=m.ShotType.get(shotType=value)

	db_shot.save()




