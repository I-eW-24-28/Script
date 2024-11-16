# Python Dictionaries

In Python Dictionaries können ähnlich wie in Python-Listen eine Reihe von
Elementen abgelegt werden. Anders als in Python-Listen werden die Elemente
allerdings nicht über einen Index aufgerufen, sondern über einen Schlüssel. Man
spricht daher von *key - value* Paaren. Das folgende Listing zeigt ein einfaches
Beispiel für ein Python Dictionary.

```Python
definitions = {
    'list': 'Eine Python-Liste ist eine geordnete Ablage von Werten von bliebiger Länge.',
    'dictionary': 'Ein dictionary in Python bietet die Möglichkeit, key-value Paare abzulegen.'
}
```

Die *key - value* Paare werden für die Erstellung eines Python Dictionary in
geschweifte Klammern geschrieben. Die Verbindung von Schlüssel und Wert erfolgt
durch die Verbindung mit einem Doppelpunkt (`key: value`). Als Schlüssel eignen
sich dabei Strings, Tupel (werden noch erklärt), sowie Ganzzahlen. Um die
Lesbarkeit des Codes zu verbessern, hat es sich als gängige Praxis etabliert, die
Variabel, welcher das Dictionary zugewiesen wird auf einer separaten Zeile zu
schreiben und anschliessend für jedes *key - value* Paar eine neue Zeile zu
verwenden. Mehrere Elemente werden durch Kommata abgegrenzt.

Um auf einen Eintrag in einem Dictionary zuzugreifen, verwendet man die Variabel
mit anschliessenden eckigen Klammern, in denen der Schlüssel steht.

```Python
defintions['list']
```

Das obige Listing gibt entsprechend den dem Schlüssel `list` zugewiesenen Wert aus.