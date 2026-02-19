class ContactBook:
    def __init__(self, person):
        self.person = person
    
    def __str__(self):
        contact = {
            "name": "Alis",
            "telephone": +46733399000
            "E-mail": "email@live.com"
            }
        return f"{self.person} 's contact is: {contact}"
    


