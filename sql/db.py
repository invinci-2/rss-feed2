from sqlalchemy import Column, String, Numeric, Boolean
from sql import SESSION, BASE

class database(BASE):
    __tablename__ = "database"
    website = Column(String, primary_key=True)
    link = Column(String)
    website2 = Column(String, primary_key=True)
    link2 = Column(String)

    def __init__(self, website, link):
        self.website = website
        self.link = link
    def __init__(self, website2, link2):
        self.website2 = website2
        self.link2 = link2


database.__table__.create(checkfirst=True)


def get_link(website):
    try:
        return SESSION.query(database).get(website)
    except:
        return None
    finally:
        SESSION.close()


def update_link(website, link):
    adder = SESSION.query(database).get(website)
    if adder:
        adder.link = link
    else:
        adder = database(
            website,
            link
        )
    SESSION.add(adder)
def get_link2(website2):
    try:
        return SESSION.query(database).get(website)
    except:
        return None
    finally:
        SESSION.close()


def update_link2(website2, link2):
    adder2 = SESSION.query(database2).get(website2)
    if adder2:
        adder2.link2 = link2
    else:
        adder2 = database(
            website2,
            link2
        )
    SESSION.add(adder2)
    SESSION.commit()
