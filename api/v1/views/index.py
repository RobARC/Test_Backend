#!/usr/bin/env python3
""" Module of Index views"""
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/card', methods=['GET'], strict_slashes=False)
def get_card_number():
    """ GET card number
    Return:
      - Franchise name
    """
    if validate_cardnum() % 10 == 0:
        return jsonify({"Credit card number": "Is OK!"},
                       {"Franchise": validate_franchise(request.card_number)})
    else:
        return jsonify({"Credit card number": "Bad number!"})


def validate_num(value):
    """Method evalute each position is > 9"""

    value_int = int(value)

    if value_int > 9:
        string_value = str(value)
        return int(string_value[0]) + int(string_value[1])
    return value_int


def validate_cardnum():
    """Method to validate credicard number
       Luhn algorhitm
    """

    card_num = request.card_number
    card_num_length = len(card_num)
    result = 0

    if card_num_length < 15 or card_num_length > 16:
        abort(400, description="Please check your number!")

    for i in range(card_num_length):

        try:
            value = int(card_num[i])
        except Exception:
            """if there if a character != int"""
            abort(403, description="Bad Request")

        if i % 2 == 0:
            result += validate_num(value * 2)
        else:
            result += value

    return result


def validate_franchise(str_num):
    """Method to evaluate franchise"""

    first_number = int(str_num[0])

    if first_number == 3:
        franchise = "American Expres"
        return franchise
    if first_number == 4:
        franchise = "Visa"
        return franchise
    if first_number == 5:
        franchise = "Master Card"
        return franchise
    if first_number == 6:
        franchise = "Discovery"
        return franchise
    if first_number < 3 or first_number > 6:
        franchise = "Other"
        return franchise
