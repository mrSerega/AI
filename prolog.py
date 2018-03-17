import processor

debug = False

class Prolog:
    
    relations = dict()
    
    def parseCode(self, code):
        __code = code.split('\n')
        for line in __code: self.parseLine(line)
    
    def parseLine(self, line):
        line = line.replace(' ','')
        if len(line) < 1: return 
        if line[0] == '#': return 
        if line[0] == '?': return self.parseQuestion(line[1:])
        if ('->') in line: return self.addFormula(line)
        return self.addFact(line)
    
    def parseQuestion(self, question, vars = []):
        questionLine = question.split('(')
        questionName = questionLine[0]
        questionValue = questionLine[1].split(')')[0]
        questionArguments = questionValue.split(',')
        if len(questionValue) == 0: print('Error: no arguments in question')
        elif len(questionArguments) == 1: return self.getAnswer(questionName, questionArguments[0], questionArguments[0], vars)
        elif len(questionArguments) == 2: return self.getAnswer(questionName, questionArguments[0], questionArguments[1], vars)
        else: print('Error: to many arguments in question')
    
    def addFact(self, fact, vars = None):
        factLine = fact.split('(')
        factName = factLine[0]
        factValue = factLine[1].split(')')[0]
        factArgs = factValue.split(',')
        numOfArgs = len(factArgs)
        if(numOfArgs == 0): print('Error: no arguments in fact')
        elif(numOfArgs == 1):
            if vars: self.addRelation(factName,vars[factArgs[0]],vars[factArgs[0]])
            else: self.addRelation(factName,factArgs[0],factArgs[0])
        elif(numOfArgs == 2):
            if vars: self.addRelation(factName,vars[factArgs[0]],vars[factArgs[1]])
            else: self.addRelation(factName,factArgs[0],factArgs[1])
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
        answer = self.parseQuestion(conditionCondition)
        pairs = None
        if 'exists' in formulaCondition:
            formulaCondition = formulaCondition.replace('exists','')
            formulaCondition = formulaCondition[1:-1]
            if debug: print('[addFormula] condition2: {}'.format(formulaCondition))
            formulaCondition = formulaCondition.split(':')
            vars = formulaCondition[0].split(',')
            question = formulaCondition[1]
            if debug: print('[addFormula] vars: {}'.format(vars))
            if debug: print('[addFormula] questions {}:'.format(question))
            pairs = self.parseQuestion(question,vars)
        elif 'forall' in formulaCondition:
            print ('Error: forall coming soon')
        else:
            print ('Error: unknown predicat')
        results = fomulaResult.split('),')
        results_last = results[-1]
        results = results[:-1]
        for index, val in enumerate(results):
            results[index] += ')'
        results.append(results_last)
        if debug: print ('[addFormula] results2: {}'.format(results))
        for result in results:
            for pair in pairs:
                self.addFact(result, {vars[0]:pair[0], vars[-1]: pair[1]})
        # for i, var in enumerate(formulaVars):
        #     var = answer[i]
        # results = formulaResult.split(',')
        # for res in results:
        #     addFact(res)

    def getAnswer(self, questionName, arg1, arg2, vars):
        if arg1 in vars and arg2 not in vars :
            ans = []
            tmp = self.relations[questionName].storage
            for key in tmp:
                if arg2 in tmp[key]: ans.append([key,arg2])
            return ans
        elif arg1 not in vars and arg2 in vars:
            ans = []
            tmp = self.relations[questionName].storage
            for val in tmp[arg1]: 
                ans.append([arg1, val])
            return ans
        elif arg1 in vars and arg2 in vars:
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
        if not debug:
            try:
                print ("returned value={} for line={}".format(prolog.parseLine(line),line))
            except Exception:
                print("Some error occured during parsing line {}".format(line))
        else: print(prolog.parseLine(line))


    # if debug: print ('[main] {}'.format(prolog.relations['P'].storage))  
    # if debug: print ('[main] {}'.format(prolog.relations['P'].isConnected("y","y")))
    # if debug: print ('[main] {}'.format(prolog.getAnswer('P','x',"'y'",['x'])))
    # if debug: print ('[main] {}'.format(prolog.getAnswer('P',"'x'",'y',['y'])))
    # if debug: print ('[main] {}'.format(prolog.getAnswer('P','x','y',['x','y'])))
    # if debug: print ('[main] {}'.format(prolog.relations))
    print (prolog.relations['Q'].storage)