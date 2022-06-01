# CYCLICAL STOCHASTIC GRADIENT MCMC FOR BAYESIAN DEEP LEARNING
## Abstract
- cSG-MCMC(Cyclical stochastic gradient MCMC) to explore high-dimensional and multimodal distribution --> NN的weights的后验分布
- cyclical stepsizes: large steps for new modes and small steps for charactering modes, e.g: Multi-Mormal(Fig 2)
- 证明了算法的非渐近收敛(non-asymptotic convergence)
- experiental results
## cSG-MCMC
方法的核心在于cyclical，也就是在原本常规的SG-MCMC的基础上，将decreasing的stepsizes改进为cyclical decreasing，目的就是提高算法效率与降低loss，对比如下图所示。
![image](https://user-images.githubusercontent.com/105667644/171495988-eb274e68-baab-4a90-9546-a2818b4719b0.png)\
相比于传统的decreasing stepsizes，cSG-MCMC可以看作是不断的重复传统SG-MCMC的一个过程，将每一次decrease分为exploration stage和sampling stage，也就是abstract提到large steps和small steps的区别：
- Exploration Step: 通过大的stepsize使得sampler做出较大的改变，不断更新参数$\theta$，从而跳出local mode去找到新的mode
- Sampling Step: 小的stepsize可以让sampler留在已经发现的新mode并characterize，通过MCMC collect samples进而找到mode的posterior和parameters
除此之外，文章还提到cSG-MCMC可以看作'an efficient approximation of parallel MCMC', 相比于parallel MCMC可以以更低的cost去获得相似的结果
## Algorithm of cSG-MCMC
在传统SG-MCMC中，sampler会始终在local mode中进行sample，因此文章提出了使用$cos$构造stepsize schedule：The stepsize at iteration k is defined as:\
$\alpha_k = \frac{\alpha_0}{2}\left\[cos\left\(\frac{\pi\mod(k-1, \lceil K/M \rceil)}{\lceil K/M \rceil}\right\)+1\right\]$\
where $\alpha_0$ is the initial stepsize, $M$ is the number of cycles and $K$ is the number of total iterations.\
\
在每一个iteration开始的时候，$\alpha_k$从$\alpha_0$开始不断下降，进入sampling stage后开始collect samples直到结束，而后开始新的iteration，stepsize回到large水平，跳出local mode从而找到新的mode\
\
根据定义的stepsize schedule，在Exploration stage仍然存在问题，当stepsize too large，SG-MCMC的stationary distribution会与真实的后验分布存在较大的误差，同时在更新过程中会十分容易被拒绝而长时间无法更新降低效率，因此引入了system temperature，但是在文章中选择在exploration stage设定$T=0$, sampling stage设定$T=1$. 在划分两个stage方面，文章选择使用'completed proportion of a cycle' $r(k)=\frac{\mod(k-1, \lceil K/M \rceil)}{\lceil K/M \rceil}$衡量并设定一个threshold，低于边界即进入sampling stage.
![image](https://user-images.githubusercontent.com/105667644/171493212-f7f73a45-d29c-4dc9-86c0-225e9361ff42.png)
## Experiental Results
- multi-modal distribution on a 2D mixture of 25 Gaussians\
SGLD can only discover 4 modes but cSGLD can discover all 25 modes
- classification on CIFAR-10 and CIFAR-100
- ImageNet: ResNet-50
- MNIST and notMNIST
