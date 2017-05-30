import json

def goku():
    print("goku")
    return

def led(cmd):
    print(cmd + "led")

def voice(cmd):
    print(cmd+"voice\n")

def vote(cmd):
    json_file = '/home/pi/interop2017/result.json'
    with open(json_file) as data_file:
        data = json.load(data_file)
    if cmd == 'goku':
        data['goku'] = data['goku'] +1
    else:
        data['freeza'] = data['freeza'] +1
    print(data)
    with open(json_file,'w') as outfile:
        json.dump(data,outfile)

if __name__=="__main__":
    goku()
