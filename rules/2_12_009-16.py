from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime


def get_age(birthdate):
    birth_date = datetime.strptime(birthdate, '%Y%m%d')
    current_date = datetime.now()
    age = (current_date - birth_date).days // 365
    return age


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户类型"] == "脱贫户":
        birthdate = record.objectInfo['出生日期']
        age = get_age(birthdate)
        if age >= 16 and age < 60:
            if record.objectInfo["健康状况"] == "健康":
                for member in record.family.member:
                    if member.objectInfo is None:
                        continue
                    if member.objectInfo["劳动技能"] == "丧失劳动力":
                        raise Error(no='2_12_009-16', objectInfo=[member.objectInfo])
