

import numpy as np

from flask import Flask, request
from flask import jsonify
app = Flask(__name__)


class WordFinder(object):
    def __init__ (self,words,board):
        """words list of search words
           board 2D array of letters
        """
        self.words = words
        self.board = board
        # transpose the board
        self.transposed_board = np.matrix(board).transpose().tolist()


    def finder (self,word,board,is_transposed=False):
        """ Loop over the letter matrix. If you find your word continue matching letters
        word: search str
        board: 2D array of letters
        is_transposed: bool  board is tranposed
        returns: list of starting indexes of found word
        """
        locations=[]
        rows =  len(board)
        for i in range(rows):
            skip = False
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    cc=j
                    for x in range(len(word)):
                        if cc >= len(board[i]) or board[i][cc] != word[x]:
                            skip=True
                        cc += 1
                    if not skip:
                        locations.append( (j,i) if is_transposed else (i,j)  )
        return locations

    def search(self):
        """ return dictionary of word -> starting index , direction
        nort_south, east_west
        """
        word_idx_map={}
        for w in self.words:
            found_tp = self.finder(w,self.transposed_board,is_transposed=True)
            if found_tp:
                word_idx_map[w] = (found_tp, 'N_S')
            found = self.finder(w,self.board)
            if found:
                word_idx_map[w] = (found, 'E_W')
        return jsonify(word_idx_map)




@app.route('/search',methods=['POST'] )
def search():
    """ json POST
    keys:
        words: list of search words
        boards: 2D array of letters
    """
    request_json = request.get_json()
    app.logger.info(request_json)
    words =request_json.get('words')
    board = request_json.get('board')
    wf = WordFinder(words,board)
    return wf.search()


if __name__ == '__main__':
    app.run(debug=True, port=5000)




