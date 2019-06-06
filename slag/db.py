
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, DATETIME, VARCHAR, JSON, FLOAT
from sqlalchemy import create_engine, distinct
from sqlalchemy.orm import sessionmaker

import flask
from flask import g
from flask.cli import with_appcontext

Base = declarative_base()

class CpuRecord(Base):
    __tablename__ = 'cpus'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR, nullable=False, index=True)
    brand = Column(VARCHAR, nullable=False)
    series = Column(VARCHAR, nullable=False)
    lithography = Column(INTEGER, nullable=False)
    core = Column(INTEGER, nullable=False)
    threads = Column(INTEGER, nullable=False)
    base_frequency = Column(FLOAT, nullable=False)
    max_frequency = Column(FLOAT, nullable=False)
    socket = Column(VARCHAR, nullable=False)
    tdp = Column(INTEGER, nullable=False)
    price = Column(INTEGER, nullable=False)
    update_date = Column(DATETIME, nullable=False)

class CpuDB:
    def __init__(self):
        self.connect_string = 'mysql+pymysql://reader:123456@192.168.124.5:3306/slag'        
        self.engine = create_engine(self.connect_string, echo=False)
        self.session = None
    
    def _connect(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def _check_connection(self):
        if self.session is None: return False
        # TODO: check connection
        # Try: select 1 as alive;
    
    def get_all_cpus(self):
        if not self._check_connection():
            self._connect()
        records = self.session.query(CpuRecord).all()
        return records
    
    def get_cpu_from_id(id):
        if not self._check_connection():
            self._connect()
        records = self.session.query(CpuRecord).filter(CpuRecord.id == id)
        records = records.all()
        return records
    
    def get_all_cpu_basic(self):
        if not self._check_connection():
            self._connect()
        basic_cols = ['id', 'name', 'core', 'max_frequency', 'price']
        basic_cols = [getattr(CpuRecord, name) for name in basic_cols]
        records = self.session.query(*basic_cols)
        records = records.all()
        return records

    def close():
        self.session.close()
