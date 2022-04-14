# Prosit Har allergi og nyser kraftigt
sneezy = dict(
    Name = "Prosit",
    Normal = ("Prosit nyser ned i sine hænder og kigger forundret ned i dem bagefter.\n", ""),
    Summon = ("Prosit nyser og nyser og nyser, så Søvnig vågner fra sin lur og kommer trissende med en antihistamin til Prosit.\n", "Søvnig"),
    ChaseAway =  ("Prosit nyser så højt, at Gnavpot stikker ham en med klør fem, mumler sagte undskyld i sit skæg og skrider småskulende.\n", "Gnavpot"),
    Last = "Prosit nyser stolt og går i gulvbrædderne.\n")

# Søvnig Gaber højt
sleepy = dict(
    Name = "Søvnig",
    Normal = ("Søvnig GABER SÅ SÅ SÅ HØJT.\n", ""),
    Summon = ("Søvnig gaber og gaber og gaber så Dumpe bliver interesseret og nærmer sig. Han falder selvfølgelig over sine egne ben, men formår til sidst at komme hen og kigge Søvnig ned i gaber.\n", "Dumpe"),
    ChaseAway = ("Søvnig gaber Prosit i fjæset. Prosit nyser ham i munden, og skynder sig at løbe, da det alligevel var ret klamt gjort\n", "Prosit"),
    Last = "Søvnig ruller sig sammen til en stor klump og sover... zzz zzz ZZ\n")

## Gnavpot Sur men med et godt hjerte
grumpy = dict(
    Name = "Gnavpot",
    Normal = ("Gnavpot mumler i sit skæg. MumlemumleMUMLEL!!!\n", ""),
    Summon = ("Gnavpot råber efter Prosit, som skal komme og se hvad der sker! KOOMMMM!!\n",
       "Prosit"),
    ChaseAway = ("Gnavpot råber ad Prosit som nysende skynder sig væk.\n",
       "Prosit"),
    Last = "Gnavpot gumler gnavent på en grim gulerod og ignorerer alle.\n")
## Dumpe Klodset, ikke tale, løber langt efter de andre.
dopey = dict(
    Name = "Dumpe",
    Normal = ("Dumpe vifter med ører og tæer Do.oD\n", ""),
    Summon = ("Dumpe forsøger at jodle, men der kommer ikke lyde ud..han fægter med armene og vælter sig selv, så det larmer og Gnavpot kommer rendende for at se om der er sket noget!!\n", "Gnavpot"),
    ChaseAway = ("Dumpe er så klodset at han forvirrer sig selv og får jagtet sig selv væk, faldende over egne og andres ben.\n", "Dumpe"),
    Last = "Dumpe vifter med ørerne som den rosin i pølseenden han er.\n")


people = {
    "Dumpe"   : dopey,
    "Gnavpot" : grumpy,
    "Søvnig"  : sleepy,
    "Prosit"  : sneezy
    }

allPeople = [grumpy, sleepy, dopey, sneezy]

