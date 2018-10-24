#Dojo Survey with Validation
#2018 10 04
#Cheung Anthony

# Take the Dojo Survey assignment that you completed previously and add validations! The Name and Comment fields should be validated so that they are not blank. Also, validate that the comment field is no longer than 120 characters.

from flask import Flask, render_template, redirect, request, session,flash
app = Flask(__name__)
app.secret_key='as43df46asd3f4as4'

#our index route will handle the form
@app.route('/')
def index():
    return render_template('index.html')

#route to handle form submission that calls HTTP allowed for this route
@app.route('/submitted', methods=['POST'])
def submitted():
    session['full_name']=request.form['q0_full_name']
    session['comment']=request.form['q3_comment']
    q0_str=str(request.form['q0_full_name'])
    q3_str=str(request.form['q3_comment'])
    q3_len=len(request.form['q3_comment'])
    if not q0_str.strip() and not q3_str.strip():
        flash("Please complete Name Comments in order to submit")
        return redirect('/')
    if q0_str.strip() and not q3_str.strip():
        flash("Please Comments in order to submit")
        return redirect('/')        
    if q0_str.strip() and not q3_str.strip() and q3_len>120:
        print(q3_len)
        flash("Please revise. Comments cannot exceed 120 characters")
        return redirect('/')        
    else:
        print("successful submission")
        session.clear()
    return render_template('submitted.html')

if __name__=="__main__":
    app.run(debug=True)

