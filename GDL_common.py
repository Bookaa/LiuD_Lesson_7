import re

class Parser00:
    def __init__(self, txt):
        self.txt = txt
        self.pos = 0
    def handle_NAME(self):
        partn = '[A-Za-z_][A-Za-z0-9_]*'
        partn_compiled = re.compile(partn)
        m = partn_compiled.match(self.txt, self.pos)
        if m:
            content = m.group()
            self.pos = m.end()
            return content
        return None
    def handle_NUMBER(self):
        partn = r'0|[1-9]\d*'
        partn_compiled = re.compile(partn)
        m = partn_compiled.match(self.txt, self.pos)
        if m:
            content = m.group()
            self.pos = m.end()
            return content
        return None
    def handle_STRING(self):
        partn = r"'[^'\\]*(?:\\.[^'\\]*)*'"
        partn_compiled = re.compile(partn)
        m = partn_compiled.match(self.txt, self.pos)
        if m:
            content = m.group()
            self.pos = m.end()
            return content
        return None
    def handle_NEWLINE(self):
        partn = r"\n[\n \t]*"
        partn_compiled = re.compile(partn)
        m = partn_compiled.match(self.txt, self.pos)
        if m:
            content = m.group()
            self.pos = m.end()
            return content
        return None
    def handle_str(self, s):
        if self.txt[self.pos:].startswith(s):
            self.pos += len(s)
            return s
    def restorepos(self, pos):
        self.pos = pos
    def skipspace(self):
        while self.pos < len(self.txt) and self.txt[self.pos] in ' \t':
            self.pos += 1
    def skipspacecrlf(self):
        while self.pos < len(self.txt) and self.txt[self.pos] in ' \n':
            self.pos += 1

class OutP:
    def __init__(self):
        self.txt = ''
    def puts(self, s):
        #print s,
        if self.txt != '' and self.txt[-1] != '\n':
            self.txt += ' '
        self.txt += s
    def newline(self):
        #print
        self.txt += '\n'
