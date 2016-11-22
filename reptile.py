import urllib.request
import re

url = 'http://www.baidu.com/s?wd=daletou'
def getHtml(url):
    http = urllib.request.urlopen(url)
    #print(type(http))
    #print(http)
    html = http.read()
    #print(type(html))
    #print(html)
    return html

def getBalllist(html):
    #reg = '-red.*|.*c-icon c-icon-ball-blue.*'
    reg = '<span class="c-icon c-icon-ball-.*\d{2}</span>'
    ball = re.compile(reg)
    #print(ball.findall(html.decode('utf-8')))
    return ball.findall(html.decode('utf-8'))

html = getHtml(url)
#print (html)
ballList = getBalllist(html)
redball = ''
blueball = ''
for ball in ballList:
    #print(ball)
    red = '.*red.*(\d{2}).*'
    blue = '.*blue.*(\d{2}).*'
    if re.search(red, ball):
        #print ('red:%s' % re.search(red, ball).group(1))
        redball += re.search(red, ball).group(1) + ' '
    if re.search(blue, ball):
        #print ('blue:%s' % re.search(blue, ball).group(1))
        blueball += re.search(blue, ball).group(1) + ' '

print('red:%s' % redball)
print('blue:%s' % blueball)
    
