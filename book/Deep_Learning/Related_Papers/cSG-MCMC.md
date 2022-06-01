# CYCLICAL STOCHASTIC GRADIENT MCMC FOR BAYESIAN DEEP LEARNING
## Abstract
- cSG-MCMC(Cyclical stochastic gradient MCMC) to explore high-dimensional and multimodal distribution --> NN的weights的后验分布
- cyclical stepsizes: large steps for new modes and small steps for charactering modes, e.g: Multi-Mormal(Fig 2)
- 证明了算法的非渐近收敛(non-asymptotic convergence)
- experiental results
## cSG-MCMC
方法的核心在于cyclical，也就是在原本常规的SG-MCMC的基础上，将decreasing的stepsizes改进为cyclical decreasing，目的就是提高算法效率与降低loss，对比如下图所示。
