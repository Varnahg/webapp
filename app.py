from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

myTasks = ['uklidit', 'nakoupit', 'vyvenčit psa']
@app.route('/')
def home():
    return render_template('index.html', url_for_tasks='/mytasks', url_for_add_task='/addtask')

@app.route('/mytasks')
def my_tasks():
    return render_template('myTasks.html', url_for_tasks='/mytasks', url_for_add_task='/addtask',tasks = myTasks)


@app.route('/addtask', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            myTasks.append(new_task)
        return redirect(url_for('my_tasks'))

    return render_template('addTask.html',
                           url_for_tasks=url_for('my_tasks'),
                           url_for_add_task=url_for('add_task'))


if __name__ == '__main__':
    app.run(debug=True)
