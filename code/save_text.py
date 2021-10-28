from datetime import datetime

def searchForPhrase(text):

    if "save me" in text:

        text = text.replace("save me", "")
        texts.append(text)

        with open("supremeText.txt", 'a') as f:
            now = datetime.now()
            time_str = ' -- ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " --"
            f.write(time_str)
            for i in  texts:
                f.write("\n"+i)
            f.write("\n")
            print("-- File Saved! --\n")
        
        texts.clear()
        return time_str
    else:
        texts.append(text)
        return "Text Saved!"

def take_text(text):
    text = text.lower()
    msg = searchForPhrase(text)
    if len(texts) > 10:
        texts.pop(0)

    print(text)
    return msg

def declare_list():
        global texts
        texts = []
        print("List declared.")

if __name__ == "__main__":

    declare_list()