import numpy as np
from typing import List
from abc import ABC, abstractmethod


#Initial sequences:
class ProteinSequenes(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def GeneratingPopulation(self, chain_num : int, sequence_num:int, length:int, amino_acid : List[str] ) -> List[str]:
        pass

class RandomPopulation(ProteinSequenes):

    def __init__(self) -> None:
        super().__init__()


    def GeneratingPopulation(self, chain_num : int, sequence_num : int, length:int, amino_acid = ["A", "C", "G", "T", "S", "D", "L", "N", "Q", "P", "F", "V", "Y", "W", "I", "H", "E", "R", "K", "M"]) -> List[str]:
        
        def mutation(seq, amino_acid = ["A", "C", "G", "T", "S", "D", "L", "N", "Q", "P", "F", "V", "Y", "W", "I", "H", "E", "R", "K", "M"]) -> List[str]:
            

              index = np.random.choice(range(length-1), int(0.2*length), replace=False)
              aa = np.random.choice(amino_acid, int(0.2*length), replace = True )
              seq = list(seq)
              for i, j in enumerate(index):
                seq[j] = aa[i]
              seq = "".join(seq)
              return seq
   
        sequence_produced = ""
        for k in range(length):
            # no more than three consecutive amino acid repeats
            if k < 3 or sequence_produced[k-3:k] != sequence_produced[k-2:k+1]:
                amino = np.random.choice(amino_acid)
                sequence_produced += amino

        proteins = []
        for l in range(sequence_num):
            mutated_seq = mutation(sequence_produced)
            proteins.append(mutated_seq)
        
        if chain_num == 1:
          return proteins
        
        else:
          complex = []
          for seq in proteins:
            seqs = ":".join([seq]*chain_num)
            complex.append(seqs)
          return(complex)

