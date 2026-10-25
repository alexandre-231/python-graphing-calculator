class Calcul:
    def __init__(self):
        self.historique = []
        
    def somme(self , a,  b):
        try:
            nba = float(a)
            nbb = float(b)
            return nba + nbb
        except ValueError:
            return "valeur non float"
            
    def soustraction(self, a , b):
        try:
            nba = float(a)
            nbb = float(b)
            return nba - nbb
        except ValueError:
            return "valeur non float"

    def retourneToutLeChiffre(self , nbATrouver, nbdebut, nbBoucle = 0, res =""):
        if nbBoucle < 0:
           return self.retourneToutLeChiffre(nbATrouver,nbdebut,nbBoucle+ 1, nbATrouver[0])
            
        elif nbdebut - nbBoucle == 0:
           
            char = nbATrouver[0]
            if char.isdigit() or char == '.':
                return char + res
            return res
            
        elif nbATrouver[nbdebut-nbBoucle].isdigit() or nbATrouver[nbdebut-nbBoucle] == '.':
             return self.retourneToutLeChiffre(nbATrouver,nbdebut,nbBoucle+ 1, nbATrouver[nbdebut - nbBoucle] + res)
        
        return res



    def retourneToutLeChiffreDroite(self , nbATrouver, nbdebut, nbBoucle = 0, res =""):
      if nbBoucle >= len(nbATrouver) - nbdebut:
          return res
          
      
      elif nbATrouver[nbdebut + nbBoucle].isdigit() or nbATrouver[nbdebut + nbBoucle] == '.':
          return self.retourneToutLeChiffreDroite(nbATrouver,nbdebut,nbBoucle+ 1,  res+nbATrouver[nbdebut + nbBoucle] )
          
      elif nbBoucle == 0:
          return self.retourneToutLeChiffreDroite(nbATrouver,nbdebut,nbBoucle+ 1, nbATrouver[nbdebut])
          
      return res
          

    def verifcode(self ,nbAVerif):
        try:
            suiteNb = str(nbAVerif)
            res = 0
            for k in range(len(suiteNb)):
                if suiteNb[k] == '+':
                    res = self.somme(self.retourneToutLeChiffre(suiteNb,k-1),self.retourneToutLeChiffreDroite(suiteNb,k+1))
                if suiteNb[k] == '-':
                    res = self.soustraction(self.retourneToutLeChiffre(suiteNb,k-1),self.retourneToutLeChiffreDroite(suiteNb,k+1))
            return str(res)
        except ValueError:
            return "val pas bonne"