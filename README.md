**In Silico Protein Evolution with Hallucination**

There has been numerous progress in protein structure prediction using language models. Powerful models such as ESM(Evolutionary Scale Modelin) and AlphaFold have shown a powerful result in predicting the protein's structure with a quite good accuracies. ESM, one of the language models trained only on natural sequences, predicts the features faster than other models trained on both sequences and MSA and shows quite good structural confidence(PTTM,PLDDT,PAE,...) in protein structure predictions. Therefore,  Here we investigate ESM, to examine if the features captured by it can be used in simulating sequence evolution and generating sequences different from natural ones. Deep learning methods have shown that by borrowing structural predictors they can generate new protein backbones without considering their sequences or generating new sequences without considering their backbones. However, none of them generated both sequences and backbones simultaneously. In here the protein evolution has been simulated considering both protein's amino acids and their backbones. Starting with the population of randomly generated protein sequences, they are given to the ESM model for structure prediction and, as expected, they will be featureless. Next, with one of the evolution algorithms, here Genetic Algorithm, it has been tried to optimize the population iteratively  toward the desired structural constraints. For each sequence a fitness score has been defined and based on that  sequences with high fitness scores will be chosen. Each step consists of applying crossover and mutation operations on the sequences and calculating their distances from their centroid and also, evaluating their structural scores is one of the other fitness criteria.  Optimization from random protein having 20\% dissimilarity in their residues resulted in the population of having high plddt scores. Thus, ESM model trained on the natural proteins can be used to hallucinate sequences and their backbones with high confidence, showing a possibility of using the model to generate de novo protiens being different from natural proteins.


<br>

<p align="center">
  <img src="Flowchart.jpg" alt="ProteinEvolution" width="500" height="400">
</p>
