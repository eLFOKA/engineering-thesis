import language_tool_python

def main():
    tool = language_tool_python.LanguageTool('en-US')
    text = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
    matches = tool.check(text)
    for match in matches:
        print(f"Error: {text[match.offset:match.offset + match.errorLength]}")
        print(f"Message: {match.message}")
        print(f"Suggested Replacements: {match.replacements}")
        print(f"Rule: {match.ruleId}\n")

main()
