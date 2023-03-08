class Games:
    gameStore = 'Maiz EZ Game Store'
    
    def __init__(self, publisher='Paradox Interactive'):
        print('Welcome to Paradox Interactive')
        self.publisher = publisher
        
    def dev(self):
        print('Develope by Colossal Order Ltd.')
    def hello(self):
        print('Explore our games')
    def sell(self):
        print(f'Distribute by {self.publisher}')
    
class Game(Games):
    def __init__(self, title, genre, franchise, publisher, release):
        super().__init__(publisher)
        self.title = title
        self.genre = genre
        self.franchise = franchise
        self.release = release
        
    def checkRelease(self):
        if self.release == 1:
            print(f'{self.title} : Release 23 Feb. 2011')
        elif self.release == 2:
            print(f'{self.title} : Release 3 Apr. 2013')
        elif self.release == 3:
            print(f'{self.title} : Release 10 Mar. 2015')
        else:
            print(f'{self.title} : Release Coming Soon')
            
print('******************************************************')
game01 = Game('Cities in Motion','Simulation','NONE','Paradox Interactive',1)
game01.hello()
game01.sell()
print(f'{game01.gameStore}')
print(f'TITLE: {game01.title}')
print(f'GENRE: {game01.genre}')
print(f'FRANCHISE: {game01.franchise}')
print(f'PUBLISHER: {game01.publisher}')
game01.checkRelease()
game01.dev()

print('******************************************************')
game02 = Game('Cities in Motion 2','Simulation','Cities in Motion','Paradox Interactive',2)
game02.hello()
game02.sell()
print(f'{game02.gameStore}')
print(f'TITLE: {game02.title}')
print(f'GENRE: {game02.genre}')
print(f'FRANCHISE: {game02.franchise}')
print(f'PUBLISHER: {game02.publisher}')
game02.checkRelease()
game02.dev()

print('******************************************************')
game03 = Game('Cities: Skylines','Simulation','NONE','Paradox Interactive',3)
game03.hello()
game03.sell()
print(f'{game03.gameStore}')
print(f'TITLE: {game03.title}')
print(f'GENRE: {game03.genre}')
print(f'FRANCHISE: {game03.franchise}')
print(f'PUBLISHER: {game03.publisher}')
game03.checkRelease()
game03.dev()

print('******************************************************')
game04 = Game('Cities: Skylines II','Simulation','Cities: Skylines','Paradox Interactive',4)
game04.hello()
game04.sell()
print(f'{game04.gameStore}')
print(f'TITLE: {game04.title}')
print(f'GENRE: {game04.genre}')
print(f'FRANCHISE: {game04.franchise}')
print(f'PUBLISHER: {game04.publisher}')
game04.checkRelease()
game04.dev()
print('******************************************************')