# Datenstrukturen in Python: Listen

Eine Datenstruktur kann allgemein als Bündelung von Daten und Funktionalitäten
verstanden werden. Wie das funktioniert, soll am Beispiel von Python-Listen
gezeigt werden.

Python-Listen können dazu verwendet werden, einer Variabel mehrere Werte
zuzuweisen. Die Werte behalten dabei grundsätzlich ihre ursprüngliche
Reihenfolge bei.
Listen werden in der Regel nach der Art Ihrer Elemente benannt. Wenn eine Python-Liste von
Namen erstellt wird, wird sie beispielsweise der Variablen `names`
zugewiesen. Die Variable wird als Kennzeichen dafür, dass sie auf eine
Python-Liste verweist, in den Plural gesetzt.

>### Hintergrund der Datenstruktur Liste in Python (Exkurs)
>
>Im Verlauf der Entwicklung haben sich für die Ablage einer Datenreihe
>die Datenstrukturen Liste und Array herausgebildet. Die beiden
>Datenstrukturen weisen Ähnlichkeiten auf, unterscheiden sich aber auch
>in wesentlichen Punkten. Ähnlich sind sie sich darin, dass sie die
>Daten in einer vorgegebenen Reihenfolge speichern.  
>Unterschiede bestehen bezüglich der Anzahl Elemente, die sie aufnehmen
>können, sowie bezüglich des Zugriffs auf die einzelnen Elemente.
>Eine Liste kann grundsätzlich eine unbeschränkte Anzahl von Elementen
>aufnehmen. Begrenzt ist ihre Länge lediglich durch den physischen
>Speicherplatz des Computers. Im Gegensatz dazu muss bei einem Array
>grundsätzlich von Anfang an festgelegt werden, wie viele
>Elemente es aufnehmen kann.  
>Wenn auf ein Element einer Liste zugegriffen werden soll, muss in einer
>Liste am Beginn der Liste gestartet werden und dann Element für Element
>durch die Liste durchgegangen werden, bis man beim gewünschten Element
>angekommen ist. In einem Array ist der direkte Zugriff auf jedes
>Element möglich.
>
>Die Datenstruktur der Liste in Python verbindet aus der Sicht des
>Programms die Eigenschaften von Listen und Arrays. Eine Python-Liste
>kann jederzeit zusätzliche Elemente aufnehmen oder nicht mehr benötigte
>Elemente können gelöscht werden. Trotzdem kann mit Hilfe eines Index'
>direkt auf jeden Wert zugegriffen werden. Aus technischer Sicht handelt
>es sich daher bei Python-Listen in Python nicht um Listen im allgemeinen Sinn
>der Informatik, sondern um dynamische Arrays.
