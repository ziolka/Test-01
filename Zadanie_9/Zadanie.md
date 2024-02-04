Zadanie

Napisz bota asystenta konsoli, który będzie rozpoznawał komendy wprowadzane z klawiatury i reagował zgodnie z wprowadzoną komendą.

Bot asystent powinien być prototypem aplikacji asystenta. W pierwszym przybliżeniu, aplikacja asystenta powinna być w stanie pracować z książką kontaktów i kalendarzem. W tej pracy domowej skupimy się na interfejsie samego bota. Najprostszym i najwygodniejszym interfejsem na początkowym etapie rozwoju jest aplikacja konsolowa CLI (Command Line Interface). CLI jest dość proste w implementacji. Każdy CLI składa się z trzech głównych elementów:

    Parser poleceń. Jest to część odpowiedzialna za analizowanie ciągów wprowadzanych przez użytkownika, wyodrębnianie słów kluczowych i modyfikatorów poleceń z ciągu.
    Command handlers - zestaw funkcji, zwanych również handler, są one odpowiedzialne za bezpośrednie wykonywanie poleceń.
    Pętla żądanie-odpowiedź. Ta część aplikacji jest odpowiedzialna za odbieranie danych od użytkownika i zwracanie odpowiedzi z funkcji handler do użytkownika.

Na pierwszym etapie nasz asystent bota musi być w stanie zapisać nazwę i numer telefonu, znaleźć numer telefonu według nazwy, zmienić zapisany numer telefonu i wyświetlić wszystkie zapisane rekordy w konsoli. Aby zaimplementować tę prostą logikę, użyjemy słownika. W słowniku będziemy przechowywać nazwę użytkownika jako klucz i numer telefonu jako wartość.
Warunki

    Bot powinien znajdować się w nieskończonej pętli, czekając na polecenie użytkownika.
    Bot kończy pracę, jeśli jeżeli napotka “.”
    Bot nie jest wrażliwy na wielkość liter wprowadzanych poleceń.
    Bot przyjmuje komendy:
        "hello", odpowiada na konsoli "How can I help you?"
        "add ...". Za pomocą tego polecenia bot zapisuje nowy kontakt w swojej pamięci (na przykład w słowniku). Zamiast ..., użytkownik wprowadza nazwę i numer telefonu, zawsze oddzielone spacją.
        "zmień..." Za pomocą tego polecenia bot zapisuje nowy numer telefonu istniejącego kontaktu w pamięci. Zamiast ..., użytkownik wprowadza nazwę i numer telefonu, zawsze oddzielone spacją.
        "phone ...." To polecenie wyświetla numer telefonu dla określonego kontaktu w konsoli. Zamiast ..., użytkownik wprowadza nazwę kontaktu, którego numer ma zostać wyświetlony.
        "show all". To polecenie wyświetla wszystkie zapisane kontakty z numerami telefonów w konsoli.
        "good bye", "close", "exit" za pomocą dowolnej z tych komend bot kończy pracę po wyświetleniu w konsoli komunikatu "Good bye!".
    Wszystkie błędy wprowadzane przez użytkownika powinny być obsługiwane przy użyciu dekoratora input_error. Dekorator ten jest odpowiedzialny za zwracanie komunikatów takich jak "Wprowadź nazwę użytkownika", "Podaj nazwę i telefon" itp. Dekorator input_error musi obsługiwać wyjątki pojawiające się w funkcjach obsługi (KeyError, ValueError, IndexError) i zwracać użytkownikowi odpowiednią odpowiedź.
    Logika poleceń jest zaimplementowana w oddzielnych funkcjach, które przyjmują jeden lub więcej ciągów jako dane wejściowe i zwracają ciąg.
    Cała logika interakcji z użytkownikiem jest zaimplementowana w funkcji main, wszystkie print i input występują tylko tam.