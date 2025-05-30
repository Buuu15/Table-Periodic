import json
from app import app, db
from app.models import Element

with app.app_context():
    db.drop_all()
    db.create_all()
    with open('data/elements.json') as f:
        elements = json.load(f)
        for el in elements:
            db.session.add(Element(**el))
        db.session.commit()
    print("Database seeded.")
