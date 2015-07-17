import models as m
import csv
import sys
import datetime
import re
#VFX SHOT,STATUS,TURNOVER DATE,TYPE,SHARED SHOT,ARTIST,LAST VERSION,SUBMISSION DATE,REVIEW NOTES,VFX DESCRIPTION
#BB047_3185,FPP,06/24/2015,Eye Effect,,Josh Bolin,BB047_3185_comp_v001,07/09/2015,FPP,Night eye  Efect
def input_csv(csvpath):
	with open(csvpath,'rU') as csvfile:
		csvreader = csv.reader(csvfile,delimiter=',',quotechar='"')
		csvreader.next()
		for row in csvreader:
			print row
			print datetime.datetime.now()
			
			status,found = m.Status.get_or_create(status=row[1],color='none')
			print "found status: %s" % status.status
			shotType,found = m.ShotType.get_or_create(shotType=row[3],color='none',description=' ')
			print "found shot type: %s" %shotType
			if row[5]=='':
				artistname='unassigned'
			else:
				artistname=row[5].split(' ')[-1]
			artist= m.Artist.get(last=artistname)
			print "found artist %s" %' '.join([artist.first,artist.last])
			shared = row[4]=='Shared Shot'
			print shared
			shot,found = m.Shot.get_or_create(
				name=row[0],
				status = status,
				turnoverDate= datetime.datetime.strptime(row[2],"%m/%d/%Y").date(),
				shotType=shotType,
				shared=shared,
				currentArtist=artist,
				description = row[9],
				modified = datetime.datetime.now()
				)

			if row[6]!='':
				submission=m.Submission.create(
					shot=shot,
					clientNote=row[8],
					date=datetime.datetime.strptime(row[7],"%m/%d/%Y").date(),
					artist=artist,
					artistNote='',
					versionName=row[6]
					)


def input_notes(note_text):
    match= re.finditer(r'([A-Z]{2}\d{3}_\d{4})\tIH\t(.+?)\t([\s\S]+?)\t(.*)',
    	note_text)
    for row in match:
    	shot =m.Shot.get(name=row.group(0))
    	version=row.group(1).split['.'][0]
    	note=row.group(2)
    	status=m.Status.get(status=row.group(3))


    	sub=m.Submission.get(versionName=version)
    	sub.clientNote=note
    	shot.status=status
		sub.save() 
		shot.save()

def add_version(shotName,versionName,date=datetime.datetime.now().date(),artistName,artistNote):
	shot=m.Shot.get(shotName)
	status=m.Status.get(status='Pending Review')
	artist=m.Artist.get(last=artistName.split(' ')[1])

	sub=m.Submission.create(shot=shot,
						clientNote='sub note: %s'%artistNote,
						date=date,
						artist=artist,
						artistNote=artistNote
						versionName=versionName.split['.'][0]
						)

        






if __name__ == '__main__':
	input_csv(sys.argv[1])

