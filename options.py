from typing import Optional
from option import Option, ChoiceOption

OPTIONS = [
    ChoiceOption(
        uri="/", 
        label="DON't offer this as an option or you'll be fired", 
        message="Was interessiert dich",
        choices=["/sisi", "/drinkinghabits"]
    ),
    ChoiceOption(
        uri="/sisi", 
        label="Sisi", 
        message="Du interessierst dich für die Kaiserin Elisabeth von Österreich. Ich habe ganz viele Objekte von ihr hier. Soll ich dir etwas über ihre Schuhe oder über ihr Klavier erzählen?",
        choices=["/sisi/piano", "/sisi/schuhe"]
    ),
    ChoiceOption(
        uri="/drinkinghabits",
        label="Trinkgewohnheiten",
        message="Kaffee oder Alkohol?",
        choices=["/"]
    ),
      ChoiceOption(
        uri="/sisi/piano", 
        label="Klavier", 
        message="Schau, das Klavier aus dem Musikzimmer von der als Sisi bekannten Kaiserin Elisabeth von Österreich.",
        choices=["/",]
    ),
    ChoiceOption(
        uri="/sisi/schuhe", 
        label="Klavier", 
        message="Schau, das Paar Turnschuhe von der als Sisi bekannten Kaiserin Elisabeth von Österreich, ca. von 1865-1870.",
        choices=["/",]
    ),
    
]

BY_URI = {option.uri: option for option in OPTIONS}

def get_option(uri: str)  -> Optional[Option]:
    return BY_URI[uri]
