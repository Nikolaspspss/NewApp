from django import template

register = template.Library()

@register.filter()
def censor(text):
   bad_words = ["shit", "ass"]
   bad_words_pattern = '|'.join(bad_words)
   text = re.sub(rf'{bad_words_pattern}', '**', text)
   return text

register.filter(censor)