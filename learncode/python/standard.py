from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python' 
favorite_languages['sarah'] = 'c' 
favorite_languages['edward'] = 'ruby' 
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
   print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("------------------------------------")
favorite_languages1 = {}
favorite_languages1['jen'] = 'python' 
favorite_languages1['sarah'] = 'c' 
favorite_languages1['edward'] = 'ruby' 
favorite_languages1['phil'] = 'python'

for name, language in favorite_languages1.items():
   print(name.title() + "'s favorite language is " +
        language.title() + ".")