# Binary Search Tree

Die bisher verwendete Python Listen sind sehr einfach zu bedienen. Allerdings
verschleiern sie die zu Grunde liegende Datenstruktur.  
Bei einer Python Liste handelt es sich um ein dynamisches Array. Ein Array ist
eine Datenstruktur, bei der im Voraus ein zusammenhängender Speicherbereich von
fixer Grösse definiert wird. Bei einem dynamischen Array fällt die Restriktion
der fixierten Grösse weg und dem Speicherplatz wird laufend den Bedürfnissen
angepasst. Die Anpassung der Grösse des Speicherbereichs ist allerdings mit
erheblichem Rechenaufwand verbunden. Diesem Nachteil steht allerdings der
Vorteil gegenüber, dass in einem Array mittels des Index mit konstantem Aufwand
auf die einzelnen Elemente zugegriffen werden kann. Falls das Array sortiert
ist, kann ausserdem relativ effizient nach einem Element in dieser Datenstruktur
gesucht werden.

Eine Alternative für das Ablegen einer Sequenz von Elementen mit nicht im Voraus
bestimmten Umfang, ist eine verkettete Liste (linked list).   
Die verkettete Liste (linked list) ist eine Datenstruktur, bei der mit einer
Variabel auf das erste gespeicherte Element verwiesen wird. Zusammen mit diesem
Element wird auch der Speicherort des nächsten Elementes gespeichert. Von dieser
Verkettung von Element zu Element hat die Datenstruktur ihren Namen. In einer
verketteten Liste lassen sich neue Elemente mit konstantem Aufwand einfügen.
Allerdings hat die verkettete Liste den Nachteil, dass die Suche nach einem
Element mit linearem Aufwand verbunden ist.

An dieser Stelle kommt der binäre Suchbaum (binary search tree, bst) inst Spiel.



In verschiedenen Programmiersprachen können in
einem Array nur Elemente vom gleichen Datentyp abgelegt werden.