from api import api_module as ap
from database import database_module as db
from images import images_module as img
from report import report_module as rp
def domain():
    while True:
        print("""
              1. for calling api.
              2 for calling database.
              3. for calling images.
              4. for calling report.
              5. for exiting.""")
        option=int(input("enter any option :"))
        if option==1:
            ap.api()
        elif option==2:
            db.database()
        elif option==3:
            img.images()
        elif option==4:
            rp.report()
        else:
            print("invalid !")
            break

 