import openpyxl
preferences = {}
valuelist = []

def generatePreferences(values):
    global preferences
    preferences = {}
    global valuelist
    valuelist = []
    counter = 0
    for row in values.rows:
        count = 0
        order_tables = {}
        counter +=1
        vals = []
        for cell in row :
            count +=1
            if cell.value not in order_tables.keys():
                order_tables[cell.value] = count
            else:
                cell.value +=pow(10,-10)
                order_tables[cell.value] = count
            vals.append(cell.value)  
        valuelist.append(vals)
        preferences[counter] = [order_tables[num] for num in sorted(order_tables,reverse= True)] 
    return preferences

def dictatorship(preferences, agent) :
    if (type(agent) is int and agent < len(preferences) +1 ) :
        return preferences[agent][0]
    else:
        return 0
    

def scoringRule(preferences, scoreVector, tieBreak):
    alter_scores = {}
    agents = [k for k in preferences.keys()]
    scoreVector.sort(reverse = True)
    if len(scoreVector) == len(preferences[agents[0]]):
        for agent, alternatives in preferences.items():
            index = 0
            for alert in alternatives :
                if alert in alter_scores.keys() :
                    alter_scores[alert] += scoreVector[index]
                else :
                    alter_scores[alert] = scoreVector[index]
                index +=1
        maxScore = max(alter_scores.values())
        maxAternatives = [alter for alter in alter_scores.keys() if alter_scores[alter] == maxScore]
        return tieBreaker(preferences,maxAternatives,tieBreak)
    else:
        print("Incorrect input: ", scoreVector)
    return False


def tieBreaker(preferences, maxAternatives, tieBreak) :
    if str(tieBreak).lower() == "max" :
        return max(maxAternatives)
    elif str(tieBreak).lower() == "min" :
        return min(maxAternatives)
    elif str(tieBreak).isnumeric() and tieBreak != 0 :
        alters = [alter for alter in preferences[tieBreak] if alter in maxAternatives]
        return alters[0]


def plurality(preferences, tieBreak):
    res = {}
    for key in preferences.keys() :
        vals = preferences[key]
        val = vals[0]
        if val not in res.keys() :
            res[val] = 1
        else :
            res[val] += 1
    if len(res) > 0 :
        maxVal = max(res.values())
        maxAternatives = [alter for alter in res.keys() if res[alter] == maxVal]
        return tieBreaker(preferences,maxAternatives,tieBreak)
    print("plurarity() Failed: " )
    return False

def veto(preferences, tieBreak):
    res = {}
    for key in preferences.keys() :
        alters = preferences[key]
        last_alter = alters[-1]
        for alter in alters :
            if alter == last_alter :
                val = 0
            else :
                val = 1
            if alter in res.keys():
                res[alter] += val
            else :
                res[alter] = val
    if len(res) > 0 :
        maxVal = max(res.values())
        mostPointAlternatives = [alter for alter in res.keys() if res[alter] == maxVal]
        return tieBreaker(preferences,mostPointAlternatives,tieBreak)
    print("veto() Failed: " )
    return False

def borda(preferences, tieBreak):
    res = {}
    for key in preferences.keys():
        alters = preferences[key]
        j = 0
        for alter in alters :
            val = len(alters) - j
            if alter in res.keys() :
                res[alter] +=  val
            else :
                res[alter] = val
            j += 1
    if len(res) > 0 :
        maxVal = max(res.values())
        highScoreAlternatives = [alter for alter in res.keys() if res[alter] == maxVal]
        return tieBreaker(preferences,highScoreAlternatives,tieBreak)
    print("borda() Failed: " )
    return False
    
def harmonic(preferences, tieBreak) :
    res = {}
    for key in preferences.keys() :
        alters = preferences[key]
        last_alter = alters[-1]
        j = 1
        for alter in alters :
            if alter == last_alter :
                val = 0
            else :
                val = 1/j
            if alter in res.keys() :
                res[alter] += val
            else :
                res[alter] = val
            j += 1
    if len(res) > 0 :
        maxVal = max(res.values())
        highScoreAlternatives = [alter for alter in res.keys() if res[alter] == maxVal]
        return tieBreaker(preferences,highScoreAlternatives,tieBreak)
    print("harmonic() Failed: " )
    return False

def rangeVoting(values,tieBreak):
    sheet = values
    scoreVector = {}
    prefs = generatePreferences(values)
    for row in sheet.rows:
        alter = 1
        for cell in row :
            if alter not in scoreVector.keys() :
                scoreVector[alter] = cell.value
            else :
                scoreVector[alter] += cell.value
            alter +=1
    if len(scoreVector) > 0 :
        maxVal = max(scoreVector.values())
        highScoreAlternatives = [ind for ind in scoreVector.keys() if scoreVector[ind] == maxVal]
        return tieBreaker(prefs, highScoreAlternatives,tieBreak)
    print("rangeVoting() Failed: " )
    return False

def STV(preference, tieBreak):
    global preferences
    plurality(preference, tieBreak)
    minimum = min(preferences.values(), default=None)
    val = [key for key in preferences.keys() if preferences[key] == minimum]
    if (len(set(preferences.values())) > 1):
        for k, v in preference.items():
            preference[k] = [alters for alters in v if alters not in val]
        preferences.clear()
        STV(preference, tieBreak)
    return plurality(preference, tieBreak)



