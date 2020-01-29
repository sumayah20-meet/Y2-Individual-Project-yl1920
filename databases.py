from models import Base,User


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


# replace lecture.db with your own database file
engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))
def save(u,p):
	user = User(
	username=u,
	password=p,
	)
	session.add(user)
	session.commit()

def queryAllUsers():
	return session.query(User).all()

def signin(e,u):
	user=session.query(User).filter_by(username=e).first()
	if user != None:
		if user.password == u :
			s = True
		else:
			s = False
		return s
	else:
		return False
