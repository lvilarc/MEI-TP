def fullJustify(words, maxWidth):
    lines = []
    i = 0
    while i < len(words):
        width = len(words[i])
        j = i + 1
        while j < len(words) and width + 1 + len(words[j]) <= maxWidth:
            width += 1 + len(words[j])
            j += 1
        line_words = words[i:j]
        if j == len(words) or len(line_words) == 1:
            line = ' '.join(line_words).ljust(maxWidth)
        else:
            letters = sum(map(len, line_words))
            spaces = maxWidth - letters
            gaps = len(line_words) - 1
            base, extra = divmod(spaces, gaps)
            line = ''
            for idx, word in enumerate(line_words[:-1]):
                line += word + ' ' * (base + (1 if idx < extra else 0))
            line += line_words[-1]
        lines.append(line)
        i = j
    return lines
