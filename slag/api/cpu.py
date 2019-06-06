
from flask import request
import json

from slag.db import CpuDB

db_cpu = CpuDB()

def get_cpu():
    if request.method == 'GET':
        cpu_id = request.form.get('cpu_id', None)
        if cpu_id is not None:
            return from_id(id)
        else:
            return all_basic()
    elif request.method == 'POST':
        return ''


def from_id(id):
    data = db_cpu.get_cpu_from_id(id)
    data_json = json.dumps(data)
    return data_json

def all_basic():
    data = db_cpu.get_all_cpu_basic()
    data_json = json.dumps(data)
    return data_json