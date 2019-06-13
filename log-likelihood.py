     
def find_log_likelihood(topics,frq_word_rel_doc,frq_word_non_rel_doc,threshold): 
     
     """
     This method finds the log likelihood (LL) for terms in the training dataset
     For each topic in the training dataset, it uses the text of relevant and non-relevant documents.
     then calculate the average ll for each term by divide the value by the total number of topics in the training dataset
     
     topics --> list of the training dataset topics
     frq_word_rel_doc --> frequency of the term in the relevant documents
     frq_word_non_rel_doc --> frequency of the term in the non-relevant documents
     threshold --> to exclude terms appears less than the threshold
     
     """
  log_likelihood = list()
  
  for topic in topics:                  
    for i, word in enumerate(frq_word_rel_doc):
      a = frq_word_rel_doc[i][1] 
      b = frq_word_non_rel_doc[i][1]
      c = frq_word_rel_doc[i][2]      # c = C-a
      d = frq_word_non_rel_doc[i][2]  # d = D-b
      C = total_rel  
      D = total_non_rel  

      #E1, E2
      E1 = C * (a + b)/(C + D)
      E2 = D * (a + b)/(C + D)

      log_value1 = (math.log(a/E1))
      log_value2 = (math.log(b/E2))

      LL =  2 * ( (a * log_value1)  +  (b * log_value2 ))

      log_likelihood.append((frq_word_rel_doc[i][0],LL))

    #sort the list    
    LL_sorted = sorted(log_likelihood,key=lambda l:l[1], reverse=True)
    #for each topic append the list of terms and LL
    LL_all.append((topic[1],LL_sorted))
        
    combained_list = list()
    
    for i,record in enumerate(LL_all): 
        for j,t in enumerate(LL_all[i][1]): 
            combained_list.append((t[0],t[1])) 
            
    # for ecah term find all the LL, example (blood,[20,11,17])
    term_lls = {}
    for tuple in combained_list:
        key,val = tuple
        term_lls.setdefault(key, []).append(val)
     
   
    temp = list()
    terms_LL = []
    
    #calculate the average LL (divide the LL by total number of topics)
    for term , value in term_lls.items():
        temp.append((term, (sum(value)/len(topics))))
     
    #sort the list of LL   
    temp = sorted(temp,key=lambda l:l[1], reverse=True)
       
    for term, value in temp:
        terms_LL.append((term,str(value)))
 
    return terms_LL
