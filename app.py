from flask import Flask, render_template, request, redirect
from models import db, Contact
from sqlalchemy import or_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():

    search = request.args.get('search')
    page = request.args.get('page', 1, type=int)
    per_page = 5

    query = Contact.query

    if search:
        query = query.filter(
            or_(
                Contact.name.contains(search),
                Contact.phone.contains(search),
                Contact.email.contains(search)
            )
        )

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    contact = pagination.items

    return render_template(
        "index.html", 
        contact=contact, 
        pagination=pagination, 
        search=search, 
        total_contacts=Contact.query.count(), 
        favorite_count=Contact.query.filter_by(favorite=True).count()
    )


@app.route('/add', methods=['GET', 'POST'])
def add_contact():

    if request.method == 'POST':

        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        new_contact = Contact(
            name=name,
            phone=phone,
            email=email,
            address=address
        )

        db.session.add(new_contact)
        db.session.commit()

        print("Contact Saved Successfully")

        return redirect('/')

    return render_template('add_contact.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):

    contact = Contact.query.get_or_404(id)

    if request.method == 'POST':

        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        contact.address = request.form['address']

        db.session.commit()

        return redirect('/')

    return render_template(
        'edit_contact.html',
        contact=contact
    )


@app.route('/delete/<int:id>')
def delete_contact(id):

    contact = Contact.query.get_or_404(id)

    db.session.delete(contact)

    db.session.commit()

    return redirect('/')


@app.route('/contact/<int:id>')
def contact_detail(id):

    contact = Contact.query.get_or_404(id)

    return render_template(
        'contact_detail.html',
        contact=contact
    )


@app.route('/favorite/<int:id>')
def toggle_favorite(id):

    contact = Contact.query.get_or_404(id)

    contact.favorite = not contact.favorite

    db.session.commit()

    return redirect('/')


@app.route('/favorites')
def favorite_contacts():

    contacts = Contact.query.filter_by(
        favorite=True
    ).all()

    return render_template(
        'favorites.html',
        contacts=contacts
    )


if __name__ == '__main__':
    app.run(debug=True)