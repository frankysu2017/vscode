#!/usr/bin/env python3
# coding=utf-8

import sys

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table = db.Table(
    'association',
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))


class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    tags = db.relationship('Tags',
                           secondary=association_table,
                           back_populates='persons')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Person '{}'>".format(self.name)


class Tags(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tag = db.Column(db.String(255))
    persons = db.relationship('Person',
                              secondary=association_table,
                              back_populates='tags')

    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return "<Tag '{}'>".format(self.tag)


if __name__ == "__main__":
    print(sys.path)
