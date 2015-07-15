import models as m
import peewee

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


def populate_artists(box):
	
	for a in m.Artist:
		box.addItem(a.first)	

def populate_types(box):
	
	for a in m.ShotType:
		box.addItem(a.shotType)

def populate_status(box):
	
	for a in m.Status:
		box.addItem(a.status)




