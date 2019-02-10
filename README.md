# phOWNbook
A web challenge in filter bypassing

## Description
Psst. Hey you. 
I heard the guy who made [SecSoc's new phonebook](https://phownbook.unswsecurity.com/) wrote it late the night before the ctf.
I got a hold of some of the code, maybe you can see an issue?

```python
def do_search(search):
    search = search.lower()
    if search in phOWNbook:
        return (phOWNbook[search])
    return()

@app.route('/', methods=['GET','POST'])
def main_page():
    if request.method == 'POST':
        search = request.form.get("username").strip()
        if search.isupper():
            search = search.lower()
        if search == "administrator":
            search = ""
        return render_template('home.html', searchTerm="You searched for: '" + search + "'", results=do_search(search), msg="No Results")
    else:
        return render_template('home.html')
```