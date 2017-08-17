# https://www.hackerrank.com/contests/real-data-contest-april-2016/challenges/language-detection

"""
Problem Description

Given a snippet of text in English, French, German, or Spanish, detect the snippet's language and print the language name. You may build an offline model for this. The snippet may contain one or more lines.

Input Format
One or more lines of text.

Constraints
1) The snippet will not exceed 3KB in size
2) The snippet will be in one of the following languages: English, French, German and Spanish

Output Format
Print the snippet's language (in Title Case, as written above) on a new line.

"""

import operator
import string

# Gathered most common words from different languages and compared the input text to these words
eng_words = 'the|of|and|to|a|in|for|is|on|that|by|this|with|i|you|it|not|or|be|are|from|at|as|your|all|have|new|more|an|was|we|will|home|can|us|about|if|page|my|has|search|free|but|our|one|other|do|no|information|time|they|site|he|up|may|what|which|their|news|out|use|any|there|see|only|so|his|when|contact|here|business|who|web|also|now|help|get|pm|view|online|c|e|first|am|been|would|how|were|me|s|services|some|these|click|its|like|service|x|than|find'
spa_words = 'va|mientras|menos|momento|hacia|hace|estos|mayor|otro|antes|le|ver|dice|han|la|lo|vida|tu|vez|bien|otra|hay|decir|creo|te|porque|estaba|esa|yo|ya|cuando|nada|de|algunos|tanto|mucho|tambi n|nos|a o|cosas|espa a|desde|gran|sido|hoy|el|en|bueno|ser|otras|c mo|ejemplo|qu|toda|as|sea|casi|todo|es|adem s|pues|nunca|muy|aqu|poco|ese|un|sus|estas|sobre|eso|vamos|solo|a os|tienen|forma|puede|seg n|sino|les|que|como|aunque|veces|luego|ten a|ahora|o|una|nosotros|hab a|mismo|gente|uno|despu s|por|durante|son|cada|donde|otros|tiene|siempre|m|contra|est n|pero|los|todas|ellos|poder|trabajo|a|m s|d a|parte|personas|gobierno|ha|he|me|casa|caso|mi|fue|del|era|d as|tres|usted|este|unos|esta|esto|al|mundo|general|pa s|mejor|tal|mujer|tan|ni|para|no|parece|pol tica|hecho|pueden|s|sin|todos|algo|lugar|tiempo|est|ella|entonces|hombre|estado|las|hacer|e|entre|su|hasta|primera|si|y|dos|con|se'
ger_words = 'august|siehe|kommt|etwa|begriff|immer|liste|selbst|meist|aber|weitere|als|denen|alle|auf|genannt|ihr|aus|einige|hatte|hat|ca|geschichte|waren|unter|beim|landkreis|de|da|band|isbn|das|leben|dr|bis|wenn|diesen|name|zeit|die|deutschland|teil|haben|erste|jedoch|ihn|kirche|bereits|kann|art|deutschen|jahrhundert|nur|welt|jahren|artikel|zu|es|er|wird|zwei|diesem|bekannt|werden|dieser|dieses|f  r|gemeinde|dort|soll|menschen|welche|diese|ort|seine|auch|drei|nicht|ende|bezeichnung|je|sind|zur|wurden|of|jahre|literatur|ist|und|durch|zum|and|wie|einer|eines|namen|nach|keine|damit|eine|basisdaten|ihm|einem|usa|oder|liegt|befindet|was|war|sondern|konnte|viele|gegen|wurde|m  nchen|adresse|gibt|beiden|heute|muss|schon|bei|karte|seit|januar|der|des|beispiel|um|dann|stadt|dem|den|politik|sein|ein|ihre|seinem|seinen|ab|wieder|ohne|noch|vom|von|dass|am|an|im|zwischen|vor|in|allem|ersten|mehr|seiner|verwendet|sowie|steht|form|bedeutung|bezeichnet|jahr|also|einwohner|sich|sie|neue|hier|verlag|anderen|mit|besteht|sehr|dabei|wappen|gilt|deutsche|man|bzw|deren|ihren|m|berlin|km|st|so|oft|the|ihrer'
frn_words = 'vraiment|monde|l|comme|trop|femme|le|mais|la|donner|tu|ici|aux|te|regarder|ta|ami|me|de|personne|moi|ces|mon|ma|du|voir|sans|d|faire|toujours|vouloir|tr  s|l|partir|t|peut  tre|attendre|oui|en|ses|tuer|laisser|chez|autre|et|jamais|homme|rien|quelque|peu|bien|sur|lui|avoir|accord|chose|fois|savoir|les|que|comprendre|dire|s  r|qui|je|vrai|on|juste|oh|pouvoir|cette|s|tout|une|bon|estce|demander|ou|comment|aimer|mes|vie|croire|ce|son|besoin|passer|avec|parler|toi|penser|temps|venir|suivre|vous|arr  ter|sortir|m  me|prendre|o|des|dans|pour|merci|un|falloir|mettre|conna  tre|encore|aller|p  re|petit|aussi|non|an|pourquoi|il|par|pas|quand|alors|seul|ne|mourir|deux|plus|quoi|ils|arriver|rester|devoir|notre|  a|elle|dieu|maintenant|jour|apr  s|mal|trouver|fille|si|y|nous|sa|se'

en_count = 0
spa_count = 0
ger_count = 0
frn_count = 0


# Cleaning the string to get rid of punctuation marks
def cleanString(str):
    # str1 = ''.join([i if ord(i) < 128 else ' ' for i in str])
    table = string.maketrans("",
                             "")  # Ref - http://stackoverflow.com/questions/36464160/what-does-python-string-maketrans
    return str.translate(table, string.punctuation)


# Taking multi-line input without knowing the number of inputs lines
sentinel = ''  # ends when this string is seen
line = raw_input()
# for line in iter(raw_input, sentinel):
for word in cleanString(line.strip()).split(' '):
    if len(word) > 2:
        if word in eng_words:
            en_count = en_count + 1
        elif word in spa_words:
            spa_count = spa_count + 1
        elif word in ger_words:
            ger_count = ger_count + 1
        elif word in frn_words:
            frn_count = frn_count + 1

count_list = {'English': en_count, 'Spanish': spa_count, 'French': frn_count, 'German': ger_count}

# list.sort can also be used but it does in place sorting and can only be used for lists
sorted_count_list = sorted(count_list.items(), key=operator.itemgetter(1))

print sorted_count_list[3][0]
