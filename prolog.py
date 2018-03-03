import processor

class Prolog:
    
    relations = dict()
    
    def parceCode(self, code):
        __code = code.split('\n')
        for line in __code: self.parceLine(line)
    
    def parceLine(self, line):
        line = line.replace(' ','')
        if len(string) < 1: return 
        if string[0] == '#': return
        if string[0] == '?': self.parceQuestion(line[1:])
        if ('->') in line: self.parceFormula(line)
        self.parceFact(line)
    
    def parce():
        pass
    
    def parceQuestion(self, question):
        questionLine = question.split('(')
        questionName = questionLine[0]
        questionValue = questionLine[1].split(')')[0]
        questionArguments = questionValue.split(',')
        if len(questionValue) == 0: print('Error: no arguments in question')
        elif len(questionValue) == 1: self.getAnswer(questionName, questionArguments[0], questionArguments[0])
        elif len(questionValue) == 2: self.getAnswer(questionName, questionArguments[0], questionArguments[1])
        else: print('Error: to many arguments in question')
    
    def addFact(self, fact):
        factLine = fact.split('(')
        factName = factLine[0]
        factValue = factLine[1].split(')')[0]
        factArgs = factValue.split(',')
        numOfArgs = len(factArgs)
        if(numOfArgs == 0): print('Error: no arguments in fact')
        elif(numOfArgs == 1): self.addRelation(factName,factArgs[0],factArgs[0])
        elif(numOfArgs == 2): self.addRelation(factName,factArgs[0],factArgs[1])
        else: print('Error: to many arguments in facts')
            
    def addRelation(self, relation, firstNode, secondNode):
        if relation in relations:
            self.relations[relation].addEdge(firstNode, secondNode)
		else:
            self.relations[relation] = Graph()
    
    def addFormula(self, form):
        pass
    
    def getAnswer(self, question):
        pass
    
if __name__ == '__main__':
    file = open('test.txt','r')
    print(file.read().split('\n'))
    