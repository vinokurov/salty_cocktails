from flask import render_template, request, Response
from flask import url_for, jsonify
from salty.cocktails import app


@app.route('/cocktails')
def cocktails_main():
    pass

@app.route('/cocktails/teachers/manage_cocktails')
def teachers_manage_cocktails():
    pass

@app.route('cocktails/teachers/manage_cocktails/edit/<cocktail_name>')
def teachers_edit_cocktail(cocktail_name):
    pass

@app.route('cocktails/teachers/manage_cocktails/add')
def teachers_add_cocktail():
    pass
