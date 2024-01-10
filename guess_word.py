## guess the word riddle game 
## eg T ,E,G  ---> correct
##  `T`  ---> this letter is present in word but position is wrong
##   "T" ---> wrong letter

import random
ques={
"What five-letter word can be read the same upside down or right side up? ": "SWIMS",
"Which word in the dictionary is spelled incorrectly?" :"INCORRECTLY",
"What color can you eat?": "ORANGE",
"What has many words but never speaks? ": "BOOK",
"I am lighter than air, but a hundred people cannot lift me—Im too fragile. What am I?": "BUBBLE"
}

def check():
    s=""
    for i in range(len(ans)):
        if ans[i]==ques[r][i]:             ## check same and correct
            s+=ans[i]
        elif ans[i] in ques[r] and ans[i]!=ques[r][i]:    ## wrong position
            s+="`"+ans[i]+"`"
        else:
            s+="\""+ans[i]+"\""
    return s


if __name__=="__main__":
    r=random.choice(list(ques))
    print(r)
    while True:
        ans=input("Enter word >>> ").upper()
        if ans==ques[r]:
            print("..CORRECT..")
            print(ans)
            break
        else:
            print(check())

    print("THANK YOU")