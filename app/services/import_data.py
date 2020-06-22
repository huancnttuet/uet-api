import pandas as pd
import os
import pandas
import xlrd
from sqlalchemy import create_engine
import json
from app.models import db, ExamtimeModel


def import_csv():

    ROOT_DIR = os.path.dirname(os.path.abspath(
        __file__))  # This is your Project Root
    file_name = ROOT_DIR + "\\lichthi.xlsx"

    df = pd.read_excel(io=file_name, sheet_name=2)

    print(json.dumps(json.loads(df.reset_index().to_json(orient='records')), indent=2))

    # df.to_sql(ExamtimeModel, con=db.engine)


# engine = create_engine('mysql://bd474dc8c06660:2c9f6312@us-cdbr-east-05.cleardb.net/heroku_e3a89c45e672a7c?reconnect=true')
