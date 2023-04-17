
import json

from contactDB import contactDB

ctdb=contactDB()

o=input("Select an option (1-search first, 2-search last, 3-search type, 4-add, 5-edit, 6-delete, 7-end): ")
while o!='7':
  if o=='1':
    search=input("First name: ")
    results=ctdb.findByFirst(search)
    print(json.dumps(results))
  elif o=='2':
    search=input("Last name: ")
    results=ctdb.findByLast(search)
    print(json.dumps(results))
  elif o=='3':
    search=input("Type: ")
    results=ctdb.findByType(search)
    print(json.dumps(results))
  elif o=='4':
    first=input("First: ")
    last=input("Last: ")
    phone=input("Phone: ")
    ptype=input("Type: ")
    results=ctdb.addEntry(first,last,phone,ptype)
    print(json.dumps(results))
  elif o=='5':
    idnum=input("ID: ")
    first=input("First: ")
    last=input("Last: ")
    phone=input("Phone: ")
    ptype=input("Type: ")
    ctdb.editEntry(idnum,first,last,phone,ptype)
    results=printResults(results)
    print(json.dumps(results))
  elif o=='6':
    rid=form.getvalue("deleteid")
    results=ctdb.delete(rid)
    print(json.dumps(results))
  else:
    print("Error,Bad command:"+o)
  o=input("Select an option (1-search first, 2-search last, 3-search type, 4-add, 5-edit, 6-delete, 7-end): ")
