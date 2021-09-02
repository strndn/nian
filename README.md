# nian
Uppgiften som löses.

Nian
Instruktioner
Uppgiften ska lösas individuellt.
Resultatet ska vara ett Python-program. Programmets källkod ska lämnas in i inlämningslådan
i iLearn2 (se kursanvisningar för datum för inlämning).
Högst uppe i källkodsfilen i en kommentar ska inlämnarens namn och personnummer stå.
Närmare instruktioner om inlämningsförfarandet kommer senare i iLearn2.
Obs! Det kan hända att de inlämnade uppgifterna ska rättas maskinellt. Detta innebär att
utskrifter från programmet måste följa nedanstående instruktioner exakt!
Beskrivning av pusslet Nian
Svenska Dagbladet brukade varje dag ha ett pussel som hette Nian. Pusslet gick ut på att
skapa så många ord som möjligt ur ett mönster på nio angivna bokstäver.
Orden måste vara på minst fyra bokstäver.
Orden måste vara i grundform och finnas i en ordbok1
.
Varje pussel har också en speciell bokstav som varje ord måste innehålla (mittersta bokstaven
i mönstret av de nio givna bokstäverna).
Orden får inte innehålla fler förekomster av en viss bokstav än vad som finns i pusslet.
Det finns alltid åtminstone en lösning där alla bokstäver ingår (alltså åtminstone ett riktigt
svenskt ord på nio bokstäver som kan bildas av alla de bokstäver som finns i pusslet).
Nian brukar presenteras som en 3x3-matris fylld med bokstäver, med den speciella bokstaven
som måste finnas i varje ord i mitten, t.ex.
A N I
T S K
S E M
För ovanstående pussel är exempel på korrekta ord: ’ansikte’, ’kista’ och ’misstanke’.
Exempel på felaktiga ord är ’satan’ (för många ’a’), ’ask’ (för kort) och ’kenta’ (finns inte i
SAOL). Ord med alla nio bokstäverna är ’misstanke’ och ’semantisk’.

1
I SvDs pussel var ordboken SAOL (Svenska Akademins Ordlista) men i denna uppgift är det en mycket mindre
omfattande fil med ca 23000 svenska ord 
Uppgiften
Uppgiften går ut på att skriva ett Python-program som löser Nian. Som ordbok ska användas
en egen förteckning av ord som finns på samma ställe som denna text på filen
svenskaOrd.txt. Obs att denna fil är mycket mindre omfattande än SAOL så en del ord
kommer ditt program inte att hitta.
Programmet ska läsa in pusslet som en sträng på nio bokstäver, där den mittersta bokstaven är
den speciella som ska finnas med i varje lösning. Sedan ska programmet skriva ut alla
lösningar det hittar, lösningarna ska presenteras med ett ord per rad i alfabetisk ordning (det
kan hända att Python sorterar åäö i fel ordning – det behöver du inte bry dig om).
Därefter ska det komma en utskrift om hur många lösningar som använder alla nio bokstäver
och så en lista på dessa ord.
Exempel på programdialogen (användarens inmatning i svart):
Nian: anitsksem
anemisk
anis
anse
ansikte
... (många andra ord borttagna från utskriften av utrymmesskäl)
stam
stank
stek
steka
sten
stena
stim
stinka
2 ord använder alla bokstäver:
misstanke
semantisk