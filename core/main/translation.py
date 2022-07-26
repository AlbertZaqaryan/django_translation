from .models import News
from modeltranslation.translator import register, TranslationOptions

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
