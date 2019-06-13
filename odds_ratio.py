     
def find_odds_ratio(topics,frq_word_rel_doc,frq_word_non_rel_doc,threshold): 
     
     """
     This method finds the odds ratio (OR) for terms in the training dataset
     For each topic in the training dataset, it uses the text of relevant and non-relevant documents.
     then calculate the average ll for each term by divide the value by the total number of topics in the training dataset
     
     topics --> list of the training dataset topics
     frq_word_rel_doc --> frequency of the term in the relevant documents
     frq_word_non_rel_doc --> frequency of the term in the non-relevant documents
     threshold --> to exclude terms appears less than the threshold
     
     """
  odds_ratio = list()
  
  for topic in topics:                  
    for i, word in enumerate(frq_word_rel_doc):
      a = frq_word_rel_doc[i][1] 
      b = frq_word_non_rel_doc[i][1]
      c = frq_word_rel_doc[i][2] # c = C-a
      d = frq_word_non_rel_doc[i][2] # d = D-b
      C = total_rel  
      D = total_non_rel  

      #E1, E2
      E1 = C * (a + b)/(C + D)
      E2 = C * (a + b)/(C + D)

      OR = (a * d) / (b * c)

      Odds_ratio.append((frq_word_rel_doc[i][0],OR))

    OR_sorted = sorted(Odds_ratio,key=lambda l:l[1], reverse=True)
    OR_all.append((topic[1],OR_sorted))

        
    combained_list = list()
    
    for i,record in enumerate(OR_all): 
        for j,t in enumerate(OR_all[i][1]): 
            combained_list.append((t[0],t[1])) 
            
    # for ecah term find all the OR values, example (blood,[20,11,17])
    term_ORs = {}
    for tuple in combained_list:
        key,val = tuple
        term_ORs.setdefault(key, []).append(val)
     
   
    temp = list()
    terms_OR = []
    
    #calculate the average OR (divide the OR by total number of topics)
    for term , value in term_ORs.items():
        temp.append((term, (sum(value)/len(topics))))
     
    #sort the list of OR   
    temp = sorted(temp,key=lambda l:l[1], reverse=True)
       
    for term, value in temp:
        terms_OR.append((term,str(value)))
 
    return terms_OR
