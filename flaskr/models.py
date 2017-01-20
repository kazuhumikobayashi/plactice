from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text

from flaskr import db


class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_name = Column(Text)

    def __repr__(self):
        return '<Product id={id} product_name={product_name}>'.format(
                id=self.id, product_name=self.product_name)
