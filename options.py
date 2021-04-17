from typing import Optional
from option import Option, ChoiceOption, LeafOption
from message import TextMessage, PhotoMessage, RandomMessage, MedieGroupMessage, AnimationMessage

from telegram import MessageEntity, InputMediaPhoto


OPTIONS = [
    ChoiceOption(
        uri="/", 
        label="Erzähl mir etwas anderes, bitte!", 
        message="Was interessiert dich?",
        choices=["/sisi", "/drinkinghabits", "/skkg", "/silverfish"]
    ),
    LeafOption(
        uri="/silverfish",
        label="Erzähl mir mehr von dir.",
        messages=[
            TextMessage(
                "Nett, dass du fragst\\. Ich bin ein [Silberfischchen](https://de.wikipedia.org/wiki/Silberfischchen), wohne hier im Depot und kümmere mich um den Erhalt der Sammlung\\.",
                markdown = True,
            ),
        ],
        next_option="/restart",
    ),
    ChoiceOption(
        uri="/restart",
        label="Soll ich dir etwas anderes erzählen?",
        messages=[
            RandomMessage([
                TextMessage("Soll ich dir etwas anderes erzählen?"),
                TextMessage("Interessiert dich eines dieser Themen?")
            ])
        ],
        # TODO create new choice option that randomly picks a sublist if there are too man (and offers an option to show other options as well)
        choices=["/sisi", "/drinkinghabits", "/skkg", "/silverfish"],
    ),
    ChoiceOption(
        uri="/skkg", 
        label="Erzähl mir doch etwas über die Sammlung.", 
        messages=[
            PhotoMessage(photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/bst.jpg"),
            TextMessage("Alle die Objekte hat Bruno Stefanini über fünfzig Jahre hinweg gesammelt. Er interessierte sich für nahezu alles. Die Objekte sind bei mir hier im Depot eingelagert und werden für Ausstellungen an Museen verliehen. Manchmal müssen dann die Mitarbeiter und Mitarbeiterinnen im grossen Depot ein bisschen nach den Objekten suchen, aber bisher haben sie noch immer alles gefunden. Dabei hilft ihnen die Museumsdatenbank. Von dort habe übrigens auch ich meine Infos, die ich dir hier erzähle. All das kann sich doch niemand merken!"),
            TextMessage("Worüber soll ich dir nun etwas erzählen?"),
        ],
        choices=["/sisi", "/drinkinghabits"]
    ),
    ChoiceOption(
        uri="/sisi", 
        label="Sisi (Kaiserin Elisabeth von Österreich)", 
        messages=[
            TextMessage(
                "Du interessierst dichs für die [Kaiserin Elisabeth von Österreich](https://de.wikipedia.org/wiki/Elisabeth_von_%C3%96sterreich-Ungarn)\\. Ich habe ganz viele Objekte von ihr hier\\. Soll ich dir etwas über ihre Schuhe oder über ihr Klavier erzählen?",
                markdown = True,
            ),
        ],
        choices=["/sisi/piano", "/sisi/schuhe"]
    ),
     ChoiceOption(
        uri="/drinkinghabits",
        label="Historische Trinkgewohnheiten",
        message="Für welches Getränk interessierst du dich? Kaffee oder Alkohol?",
        choices=["/kaffee","/alkohol"]
    ),
    ChoiceOption(
        uri="/alkohol",
        label="Alkohol",
        messages=[
            TextMessage("Prost!"),
            MedieGroupMessage(
                media=[
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/43083.jpg", caption="Bowlen-Set, ein Ehrengeschenk von Kaiser Wilhelm II. an den Kampfpiloten Freiherr von Richthofen im Jahre 1917"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/23932.jpg", caption="Bierkrug aus Erich Honeckers Besitz aus der 2. Hälfte des 20. Jahrhunderts"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/11348.jpg", caption="Champagnerschalen aus dem Service von Reza Pahlavi, welcher 1925-1941 als letzter Schah von Persien regierte"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/5048.jpg", caption="Weinkaraffe aus dem Service von König Ludwig II. von Bayern aus dem 19. Jahrhundert"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/12449.jpg", caption="Bierkrug, den Feldmarshall Montgomery von den sogenannten Wüstenratten einer Britischen Division, welche während des 2. Weltkrieges in Nordafrika stationiert war, als Andenken geschenkt bekommen hat"),
                ],
            ),
            TextMessage("Genug angeheitert, um dich mit dem Tod zu befassen?")
        ],
        choices=["/tod","/alkohol/ende"]
    ),
   LeafOption(
        uri="/alkohol/ende", 
        label="Danke, aber nein Danke!", 
        message="Gut... Lass mich kurz überlegen...",
        next_option="/restart"
    ),
    ChoiceOption(
        uri="/tod",
        label="uuh... morbide! Ja, gerne!",
	    messages=[
            PhotoMessage(
                caption="Schau, die getrockneten Blumen vom Katafalk Franz Josephs I. als Erinnerungsstück an sein Begräbnis 1916, aus dem Besitz der Schauspielerin Katharina Schratt.",
                photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/43214.jpg",
            ),
            TextMessage(
                "Falls du dich gerade fragst, was genau ein [Kataphalk](https://de.wikipedia.org/wiki/Katafalk) ist, verlinke ich dir hier mal den Wiki\\-Artikel\\.",
                markdown = True,
            ),
		  TextMessage(
                "Und wenn dich Franzls Frau Sisi interessiert, kann ich dir gerne mehr zu ihr zeigen\\. Was meinst du?",
                markdown = True,
            ),
        ],
        
        choices=["/sisi", "/"]
    ),	
	
    ChoiceOption(
        uri="/kaffee",
        label="Kaffee",
        messages=[
            AnimationMessage(animation_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/fish_coffee_cigarett.gif "),
            TextMessage("Coffee and Cigaretts!"),
        ],
        choices=["/kaffee/cigaretts", "/kaffee/only"]
    ),

    ChoiceOption(
        uri="/kaffee/cigaretts",
        label="Erzähl mir mehr...",
	    messages=[
            TextMessage("Hier eine Zusammenstellung  von Objekten zum Thema Coffee and Cigaretts:"),
            MedieGroupMessage(
                media=[
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/11595.jpg", caption="24 Kaffeelöffel aus dem Service von König Karl I. von Portugal"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/23072.jpg", caption="Milchkanne aus dem Service der Luzerner Hotelière Katharina Morel-Peyer von ca. 1810"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/23118.jpg", caption="Mokkaservice mit goldenen Bienen aus dem Besitz von Napoleon Bonaparte von ca. 1810"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/46060.jpg", caption="Zigarettenetui, welches die Schauspielerin Katharina Schratt 1911 von ihrem Verehrer Erzherzog Franz Salvator zu Wihnachten geschenkt bekam"),
		            InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/51650.jpg", caption="Zigarettenetui von Prinz Friedlich Leopold von Preussen, wohl um die letzte Jahrhundertwende"),
                ],
            ),
            TextMessage("…noch ein Filmtipp gefällig?")
        ],
        choices=["/kaffee/cigaretts/film", "/"]
    ),

    ChoiceOption(
        uri="/kaffee/cigaretts/film",
        label="Ja, gerne!",
        messages=[
            TextMessage(
                "Der Film [Coffee and Cigarettes](https://www.youtube.com/watch?v=mM6Mpn0-eyQ), von Jim Jarmusch ist einer meiner Lieblingsfilme\\.",
                markdown = True,
            ),
        ],
        choices=["/"],
    ),
    LeafOption(
        uri="/kaffee/only",
        label="Nur Kaffee, bitte.",
        messages=[ 
	        TextMessage("Voilà, Inspirationen für den königlichen Nachmittagskaffee:"),
	        MedieGroupMessage(
                media=[
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/11595.jpg", caption="24 Kaffeelöffel aus dem Service von König Karl I. von Portugal"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/23118.jpg", caption="Mokkaservice mit goldenen Bienen aus dem Besitz von Napoleon Bonaparte von ca. 1810"),
                ],
            ),
		    TextMessage("Hübsch, nicht?"),
	    ],
        next_option="/restart"
    ),
    ChoiceOption(
        uri="/sisi/piano", 
        label="Klavier", 
        messages=[
            PhotoMessage(
                caption="Schau, das Klavier aus dem Musikzimmer von der als Sisi bekannten Kaiserin Elisabeth von Österreich.  Soll ich dir mehr über Sisi erzählen?",
                photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/12672.jpg",
            ),
        ],
        choices=["/sisi/wiki", "/sisi/ende"]
    ),
    ChoiceOption(
        uri="/sisi/schuhe", 
        label="Schuhe",
        messages=[
            TextMessage("Sisi war sehr gesundheitsbewusst und hat viel Sport getrieben, hier sind ihre Sportschuhe von 1865-1870."),
            PhotoMessage(
                photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/37618.jpg",
                caption="Paar Turnschuhe von der als Sisi bekannten Kaiserin Elisabeth von Österreich, ca. von 1865-1870",
            ),
            TextMessage("Wenn dich Gesundheit und Schönheit interessieren, zeige ich dir gerne weitere Objekte zum Thema.")
        ],
        choices=["/gesundheit", "/sisi/ende", "/alkohol/switch"]
    ),
	
   LeafOption(
        uri="/alkohol/switch", 
        label="Nein, ich möchte lieber was Trinken…!",
        message="Ok, moment. Ich bin gleich soweit.",
        next_option="/drinkinghabits",
    ),
    LeafOption(
        uri="/gesundheit", 
        label="Ja, unbedingt!", 
        messages=[
            RandomMessage([
                PhotoMessage(
                    caption="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: Toilettenspiegel von Hortense de Beauharnais, verziert mit Odalisken und dem Wappen Napoleons, datiert um 1810",
                    photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/12094.jpg",
                ),
                PhotoMessage(
                    caption="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: Schminktisch; mit Beleuchtung; Sarah Bernhardt",
                    photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects./6471jpg",
                ),
                PhotoMessage(
                    caption="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: Toilettengarnitur von Adolf Hitler von um 1935",
                    photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/42838.jpg",
                ),
            ]),
        ],
        next_option="/restart",
    ),
   LeafOption(
        uri="/sisi/ende", 
        label="Nein!", 
        message="Gut... Lass mich kurz überlegen...",
        next_option="/restart"
    ),
    ChoiceOption(
        uri="/sisi/wiki", 
        label="Ja!", 
        messages=[
            TextMessage(
                "Kennst [Kaiser Franz Josef I\\.](https://de.wikipedia.org/wiki/Franz_Joseph_I.), dem Mann von Sisi\\. Ich habe dir hier den Wiki\\-Artikel herausgesucht\\.",
                markdown = True,
            ),
            TextMessage("Ich habe auch eine Objekt von Franz Josef I. in der Sammlung. Soll ich es dir zeigen?"),
        ],
        choices=["/sisi/ende", "/sisi/franz"]
    ),  
    ChoiceOption(
        uri="/sisi/franz", 
        label="Ja!", 
        messages=[
            PhotoMessage(
                caption="Schau, das ist der Badeumhang von Kaiser Franz Joseph I. von Österreich mit einer Echtheitsbestätigung von Eugen Ketterl, dem letzten Kammerdiener seiner Majestät, von vor 1916.",
                photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/25212.jpg",
            ),
    	    TextMessage("Wenn wir schon beim Baden sind... Soll ich dir mehr über die Gesundheit erzählen?"),
        ],
        choices=["/gesundheit", "/sisi/ende"]
    ),  
]

BY_URI = {option.uri: option for option in OPTIONS}

def get_option(uri: str)  -> Optional[Option]:
    return BY_URI[uri]
