import sqlite3

from flask import jsonify


def get_result(query: str):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = []

        for item in connection.execute(query).fetchall():
            s = dict(item)
            result.append(s)

    return result


def get_one(query: str):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()

    return dict(result)


def get_movie_by_type(type: str, genre: str, release):
    query = f"""
                SELECT * FROM netflix
                WHERE `type` = '{type}'
                AND listed_in = '{genre}'
                AND release_year = {release}
    """

    result = []

    for item in get_result(query):
        result.append(
            {
                'title': item['title'],
                'description': item['description'],
            }
        )

    return jsonify(result)


get_movie_by_type('Movie', 'Dramas', 2010)
