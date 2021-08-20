# List of optimization problems

## Problem structure

All problems have an identical folder structure

- formulation/
    - formalisation milp
    - formalisation constraint programming
- instance/
    - format_[x]
        - checker.py
        - metadata.yml
        - datasets
            - dataset_[x]
                - metadata.yml
                - instance_[x].ext
                - instance_[y].ext
    - transformer
- modelling language wrapper/
    - lp
    - localsolver        
- solver/
    - solver_[x]
        - code
            - Dockerfile
            - solve.sh
        - results
            - instance_[x]
                - paper_[x]
                - run_[x]
                    - metadata.yml
                    - solution.txt
- data_viz/
    - 
- reports/
    - script
    - experimental_plan

## Metadata

File describing the result of the optimisation of an instance
```yml
apiVersion: v1
kind: magma-run
metadata:
  author : "wariel"
  run_time : "2021-20-08"
data :
  host :
    cpu : "2,6 GHz Intel Core i7 6 cœurs"
    ram : "16Go"
  used :
    cpu :
      mean : 2.2
      max : 3
    ram :
      max : "3Go"
  time : "235s"
  value : 666
```
