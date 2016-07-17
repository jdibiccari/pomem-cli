def multiline_input(stopword="@@"):
    text = ""
    while True:
        line = raw_input()
        print line
        if line.strip() == stopword:
            break
        text += "%s\n" % line
    return text

if __name__ == '__main__':
	multiline_input()