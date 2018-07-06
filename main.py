f = open('test.txt','r')

a = f.read()

a = a.split('\n')

html = ''
for i in a:
    k = i.strip()
    if not k:
        html = html + '<br \>'
    else:    
        html = html + '<p>' + i + '</p>'
    html = html + '\n'

print (html)
f.close()

f2 = open('test.html','w')
f2.write(html)
f2.close()

