# Queues in Python

Queues sind Datenstrukturen, welche Daten speichern und grundsätzlich in der
Reihenfolge, in der sie abgespeichert worden sind, wieder zurückgeben (First In
\- First Out, FIFO). Eine Queue ist eine derart fundamentale Datenstruktur, dass
Python sie als [Library](https://docs.python.org/3/library/queue.html) zur
Verfügung stellt.

Um zu verstehen, wie eine Queue funktioniert, geht es im folgenden darum, eine
eigene Klasse Queue in Python zu implementieren. 

Zu Beginn ist zu überlegen, welche Eigenschaften, die Queue aufweisen muss. Sie
muss Daten abspeichern und diese in der gleichen Reihenfolge wieder ausgeben
können. Wir brauchen also eine Struktur für die Daten und eine Struktur, welche
die Reihenfolge der Speicherung festhält. Die Struktur, welche die Reihenfolge
festhält, muss ausserdem in der Lage sein, neue Daten abzuspeichern und bereits
abgespeicherte Daten wieder zurückzugeben. Diese Beschreibung kann als
UML-Klassendiagramm dargestellt werden.

## Funktionen, welche eine Queue aufweisen muss

Eine Queue muss, um abgespeicherte Daten in der richtigen Reihenfolge
Für die Implementation wird auf
der Klasse Node, welche für die [Implementation eines
Stack](../250122/speicherstrukturen.md) geschrieben wurde, aufgebaut.