from flask import render_template, abort
from . import add


@add.route('/')
def main():
	return render_template('add.html')