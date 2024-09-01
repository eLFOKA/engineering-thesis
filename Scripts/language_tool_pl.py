import language_tool_python

def main():
    try:
        tool = language_tool_python.LanguageTool('pl')
        print("LanguageTool załadowany pomyślnie.")
    except Exception as e:
        print(f"Błąd podczas ładowania LanguageTool: {e}")
        return

    text = 'To jest zdanie z błędęm ortograficznym oraz niepoprawnym składniowym. Te zdanie ma problem z gramatyka.'
    print("Sprawdzany tekst:")
    print(text)
    matches = tool.check(text)
    if not matches:
        print("Nie znaleziono błędów w tekście.")
    for match in matches:
        print(f"Błąd: {text[match.offset:match.offset + match.errorLength]}")
        print(f"Wiadomość: {match.message}")
        print(f"Sugerowane Poprawki: {match.replacements}")
        print(f"Reguła: {match.ruleId}\n")

if __name__ == "__main__":
    main()
