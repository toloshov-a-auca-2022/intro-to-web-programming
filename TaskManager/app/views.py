from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Fabric
from app.forms import FabricForm
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    fabrics = Fabric.query.all()
    return render_template('index.html', fabrics=fabrics)

@main.route('/add', methods=['GET', 'POST'])
def add_fabric():
    form = FabricForm()
    if form.validate_on_submit():
        new_fabric = Fabric(
            name=form.name.data,
            color=form.color.data,
            quantity=form.quantity.data
        )
        db.session.add(new_fabric)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_fabric.html', form=form)

@main.route('/delete/<int:fabric_id>')
def delete_fabric(fabric_id):
    fabric = Fabric.query.get_or_404(fabric_id)
    db.session.delete(fabric)
    db.session.commit()
    return redirect(url_for('main.index'))
