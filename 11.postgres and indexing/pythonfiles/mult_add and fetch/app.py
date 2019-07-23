from user import User
from database import Database

Database.initialise(database="learners", user="godfrey", password="kiugokiega", host="localhost")
email = input('print enter email:/t')
firstname = input("enter first name:/t")
lastname = input ('enter last name:/t')
user = User(email, firstname,lastname)

user.save_to_db()

user_from_db = User.load_from_db_by_email(email)

print(user_from_db)
