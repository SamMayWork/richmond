name = str(input("Enter the name of the undersigned: "))
upNumber = str(input("Enter the UP Number of the undersigned: "))
email = str(input("Enter the Email Address of the undersigned: "))
affiliation = str(input("Enter the Affiliation of the undersigned: "))


template = '''
<div class="undersigned">
  <img class=profile src="res/profile2.png" alt="">
  <div class="content-container">
    <p id=name>{0}</p>
    <p id=up>{1}</p>
    <p id=email>{2}</p>
    <p id=affiliation>{3}</p>
  </div>
</div>
'''

print(template.format(name, upNumber, email, affiliation));

