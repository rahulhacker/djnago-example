#create of form 
#repre HTML forms
#class meta to add attribute which is not the part
#attach additional information to the class is not direct attributes of that
from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text',)

    #added to match the text area, overriding the defalut value
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'textarea','placeholder':'What\'s on your mind?'})