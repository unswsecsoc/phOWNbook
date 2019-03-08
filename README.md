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
## Solution
Simply seach for `administrator` in mixed case - bypassing the isUpper check

## Flag
`OWEEK{cASe_IssUeS_AlWaYs_rEmiNd_ME_oF_sPoNGeBoB}`

# phOWNbook-bonus
A web challenge in trying things - yes this was in the first version published online, I was going to award extra points to anyone who noticed but nobody did.

## Description
A flag has been *hidden*, split into **thousands of tiny pieces!!**

Can you find ***us*** all?

## Solution
View source (the ultimate hacker tool) on the administrator search result page to find the first part.
View source on each of the secsoc team members search results for entertaining flavourtext and the other parts of the flag.

b64 decode and enjoy

## Flag
`OWEEK{Gotta-B-Sn3Aky-Ch@rlie-Sn3Aky}`
