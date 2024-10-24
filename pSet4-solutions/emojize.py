import emoji


askUser = input("Input: ")

#language='alias' ensures that shortcodes like :thumbsup:
emojized = emoji.emojize(askUser, language='alias')

print(f"Output: {emojized}")