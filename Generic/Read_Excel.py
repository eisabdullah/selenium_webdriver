from xlrd import *


def read_cred(sname):

    wb=open_workbook("../Excel/login_credentials.xlsx")
    sh=wb.sheet_by_name(sname)
    rows=sh.get_rows()
    next(rows)
    for row in rows:
        un=row[0].value
        pwd=row[1].value
        aurl=row[2].value
        return un,pwd,aurl


