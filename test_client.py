
import requests


words = ['can', 'a', 'hello']
board = [
 ['t', 'c', 'a', 'n', 'h'],
 ['a', 'w', 'z', 'e', 'e'],
 ['p', 'h', '', 'x', 'l'],
 ['o', 'j', 'q', 'w', 'l'],
 ['q', 'i', '', 't', 'o']
]

aax=requests.post('http://127.0.0.1:5000/search',json={'words':words,'board':board})
print(aax.json())
