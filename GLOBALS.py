from opt import *

our = options(
  "python smore.py",
  """
Timm Tools: misc python methods (data mining, optimization).
(C) 2016,2017 Tim Menzies, George Mathews MIT, v2.
The stuff we can use is either simple, or not at all.""",
  "",
  all=[
    "Misc options."
    ,h("disable 'ok' functions while loading", brave =      False)
    ,h("run all tests",            egs=      False)
    ,h("show import dependencies", depends=  False)
    ,h("found for flags",          rounding= 3)
    ,h("verbose level (0=silent)", verbose=  [0,1,2,3])
  ],
  maths=[
    "misc maths stuff"
    ,h("set random number seed", seed=1)
  ],
  thing=[
    "Incrementally sample data."
    ,h("set character marking unknowns", unknown="?")
    ,h("samples per column", samples= 256)
    ,h("small effect (Cliff's delta)", cliffs= [0.147, 0.33, 0.474][0])
  ],
  num=[
    "Numeric samples."
    ,h("never normalize", noNorms= False)
    ,h("Hedges threshold", hedges= 0.38)
    ,h("%statistically confidence", conf=95) 
  ],
  sym=[
    "Samples of symbols."
    ,h("bayesian k", k= 1)
    ,h("bayesian m", m= 2)
  ],
  groups=[
    "Groupings of distance"
    ,h("distance power",      f          = 2)
    ,h("distance columns",    cols       = ["objs","decs"])
    ,h("cull factor",         cull       = 0.5)
    ,h("smallest group size", minGroup   = 30)
    ,h("split redos",         splitRedo  = 20)  
    ,h("split bigger",        splitBigger= 0.1)        
  ]
)

if __name__ == "__main__":
  print("cull",our.groups.cull)
  print("verbose",our.all.verbose)
  print(our.all)