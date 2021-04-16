from option import Option, ChoiceOption, Options

OPTIONS = Options([
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
        choices=["/",]
    ),
    ChoiceOption(
        uri="/drinkinghabits",
        label="Trinkgewohnheiten",
        message="Kaffee oder Alkohol?",
        choices=["/"]
    )
])
