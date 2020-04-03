#!/usr/bin/env python3
# coding=utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    tags = db.relationship('Tags', secondary=tags, backref=db.backref())


class Tags(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tag = db.Column(db.String(255))


person_tags = db.Table(
    'person_tags', 
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'))
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

if __name__ == "__main__":
    p1 = Person('Guo')
    p2 = Person('Tao')
    t1 = Tags('AA')
    t2 = Tags('AAA')
    p1.