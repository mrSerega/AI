import processor

debug = True

class Prolog:
    
    relations = dict()
    
    def parceCode(self, code):
        __code = code.split('\n')
        for line in __code: self.parceLine(line)
    
    def parceLine(self, line):
        line = line.replace(' ','')
        if len(line) < 1: return 
        if line[0] == '#': return
        if line[0] == '?': return self.parceQuestion(line[1:])
        if ('->') in line: return self.addFormula(line)
        return self.addFact(line)
    
    def parceQuestion(self, question):
        questionLine = question.split('(')
        questionName = questionLine[0]
        questionValue = questionLine[1].split(')')[0]
        questionArguments = questionValue.split(',')
        if len(questionValue) == 0: print('Error: no arguments in question')
        elif len(questionArguments) == 1: return self.getAnswer(questionName, questionArguments[0], questionArguments[0])
        elif len(questionArguments) == 2: return self.getAnswer(questionName, questionArguments[0], questionArguments[1])
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
        if debug: print('[addRelation] relation: {}, first: {}, second: {}'.format(relation, firstNode, secondNode))
        if not relation in self.relations:
            self.relations[relation] = processor.Graph()
        self.relations[relation].addEdge(firstNode, secondNode)
    
    def addFormula(self, form):
        if debug: print('[addFormula] {}'.format(form))

        formulaStructure = form.split('->')
        formulaCondition = formulaStructure[0]
        fomulaResult = formulaStructure[1]
        if debug: print ('[addFormula] condition: {}'.format(formulaCondition))
        if debug: print ('[addFormula] result: {}'.format(fomulaResult))
        conditionStructure = formulaCondition.split(':')
        formulaVars = conditionStructure[0][1:]
        formulaVars = formulaVars.split(',')
        conditionCondition = conditionStructure[1][:-1]
        answer = self.parceQuestion(conditionCondition)
        # for i, var in enumerate(formulaVars):
        #     var = answer[i]
        # results = formulaResult.split(',')
        # for res in results:
        #     addFact(res)

    def getAnswer(self, questionName, arg1, arg2, isVar1 = False, isVar2 = False, isReturn1 = False, isReturn2 = False):
        if isVar1 and not isVar2 :
            ans = []
            tmp = self.relations[questionName].storage
            for key in tmp:
                if arg2 in tmp[key]: ans.append([key,arg2])
            return ans
        elif not isVar1 and isVar2:
            ans = []
            tmp = self.relations[questionName].storage
            for val in tmp[arg1]: 
                ans.append([arg1, val])
            return ans
        elif isVar1 and isVar2:
            ans = []
            tmp = self.relations[questionName].storage
            for key in tmp:
                for val in tmp[key]:
                    ans.append([key, val])
            return ans
        else:
            if debug: print ('[getAnswer] question: {}, arg1: {}, arg2: {}'.format(questionName,arg1,arg2))
            relation = self.relations[questionName]
            return relation.isConnected(arg1, arg2)
    
if __name__ == '__main__':
    file = open('test.txt','r')

    prolog = Prolog()

    for line in file:
        print (prolog.parceLine(line))  

    if debug: print ('[main] {}'.format(prolog.relations['P'].storage))  
    if debug: print ('[main] {}'.format(prolog.relations['P'].isConnected("y","y")))
    if debug: print ('[main] {}'.format(prolog.getAnswer('P','x',"'y'",True, False)))
    if debug: print ('[main] {}'.format(prolog.getAnswer('P',"'x'",'y',False,True)))
    if debug: print ('[main] {}'.format(prolog.getAnswer('P','x','y',True, True)))