from contextlib import contextmanager
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        # 开启事务,自动提交和回滚
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        # if 'status' not in kwargs.keys():
        #     kwargs['status'] = 1
        # return super(Query, self).filter_by(**kwargs)
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer, nullable=False)

    def set_attr(self, attrs_dict):
        # 自动赋值
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def __init__(self):
        self.create_time = datetime.now().timestamp()

    @property
    def create_datetime(self):
        # 格式化时间
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

