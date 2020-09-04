class GameController:
    """Maintains the state of the game."""
    def __init__(self, size):
        self.size = size
        self.black_wins = False
        self.white_wins = False
        self.tie = False
        self.stop = False
        self.black_num = 0
        self.white_num = 0
        self.FINISH = False
        self.ai_turn = False

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.ai_turn or self.black_wins or self.white_wins or self.tie:
            fill(204, 102, 0)
            textSize(50)
            textAlign(CENTER)
        if self.ai_turn:
            text("Thinking...", self.size/2, self.size/2)
        if self.black_wins:
            text("BLACK WINS", self.size/2, self.size/3)
        if self.white_wins:
            text("WHITE WIN!!!", self.size/2, self.size/3)
        if self.tie:
            text("TIE", self.size/2, self.size/3)
        if self.black_wins or self.white_wins or self.tie:
            black_text = "Black: " + str(self.black_num)
            white_text = "White: " + str(self.white_num)
            textSize(30)
            text(black_text, self.size/2, self.size * 3 / 5)
            text(white_text, self.size/2, self.size * 4 / 5)
            self.FINISH = True

    def record(self):
        answer = self.input('enter your name')
        while not answer:
            answer = self.input('enter your name')
        with open('scores.txt', 'r+') as f:
            lines = [line.strip() for line in f]
            info = answer + " " + str(self.black_num) + "\n"
            if len(lines) > 0 and self.black_num > int(lines[0].split()[1]):
                f.seek(0, 0)
                f.write(info)
                for line in lines:
                    f.write(line + "\n")
            else:
                f.write(info)
        self.stop = True

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
