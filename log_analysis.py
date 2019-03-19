#!/usr/bin/env python3
# log_analysis.py - code for a log analysis project

import psycopg2

# Connect news database


def connect(database_name="news"):
    """Connect to the PostgreSQL database."""

    return psycopg2.connect("dbname=news")


def getPopularArticles():
    """Top three most popular articles"""
    db = connect()
    c = db.cursor()
    query1 = """select articles.title, count(*) as views from articles, log
                    where articles.slug = substring(log.path, 10,30)
                    group by articles.title
                    order by views desc limit 3;"""
    c.execute(query1)
    result = c.fetchall()
    print("Top three most popular articles:")
    for row in result:
        plot = '{article}: {views} views.'.format(article=row[0], views=row[1])
        print(plot)


def getPopularAuthors():
    """Authors of most popular articles of all time"""
    db = connect()
    c = db.cursor()
    query2 = """select authors.name, count(*) as views from authors, articles, log
                    where authors.id = articles.author and
                    articles.slug = substring(log.path, 10,30)
                    group by authors.name
                    order by views desc;"""
    c.execute(query2)
    result = c.fetchall()
    print("Authors of most popular articles of all time:")
    for row in result:
        plot = '{author}: {views} views.'.format(author=row[0], views=row[1])
        print(plot)


def getErrors():
    """Days with requests with more than 1% of errors"""
    db = connect()
    c = db.cursor()
    query3 = """select date, porcent from (select date, round((sum(requests)/
                    (select count(*) from log where
                    to_char(time,'YYYY-MM-DD') = date) * 100), 2) as porcent
                    from (select to_char(time,'YYYY-MM-DD') as date, count(*)
                    as requests from log where status <> '200 OK' group by
                    date) as log_porcent group by date order by porcent desc)
                    as final_query where porcent >= 1;"""
    c.execute(query3)
    result = c.fetchall()
    print("Days with requests with more than 1% of errors:")
    for row in result:
        plot = '{date}: {error_rate} %.'.format(date=row[0], error_rate=row[1])
        print(plot)

print('')
getPopularArticles()
print('')
getPopularAuthors()
print('')
getErrors()
print('')
