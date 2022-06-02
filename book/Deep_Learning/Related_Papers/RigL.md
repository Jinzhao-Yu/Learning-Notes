# Rigging the Lottery: Making All Tickets Winners
Training sparse nerual network with fixed parameter count and computational cost
## Abstract
- updates the topology(拓扑结构) of the sparse network during training by using parameter magnitudes and infrequent gradient calculations
- requires fewer floating-point operations (FLOPs)
```{note} FLOPS
FLOPS: floating point operations per second, a measure of computer performance, useful in fields of scientific computations that require floating-point calculations. 
```
- empirical evaluation: ResNet-50, MobileNets on Imagenet-2012, and RNNs on WikiText-103
## Intro
- 现有的sparse training NN的limitations
  - sparse models的最大size会受到最大的dense models的限制
  - inefficient: sparse models的parameters大部分是zero-valued，但仍需要大量计算
  - 无法确定目前最优的算法是否是sparse models quality的上限？
- **Lottery Ticket Hypothesis**: if we can find a sparse neural network with iterative pruning, then we can train that sparse network from scratch, to the same level of accuracy, by starting from the original initial conditions.\
**RigL** could be a new method that doesn't need specific "lucky" initialization: 
  - maintain memory and computitional cost proportional to density of the network
  - for a given cost, *RigL* achieves higher quality on CV and NLP tasks
  - *RigL* can find more accurate models than the current best dense-to-sparse training algorithms
## RigL Algorithm
![image](https://user-images.githubusercontent.com/105667644/171728000-edaf2c35-d2c0-4221-9a65-e3dfe2bd2221.png)\
Summary: 初始化一个random sparse network，每一次update的过程中对每一个layer的connections进行按比例$\mathbb{S}$(sparsity distribution)的drop一部分，再activate一些新的connections(using *instantaneous gradient information*)，update后train新的网络，再进行下一次update
![image](https://user-images.githubusercontent.com/105667644/171729587-b72ab8b7-33d3-4289-8143-d58a9277cbc3.png)
- Sparse Distribution $\mathbb{S}$
  - Uniform: 每一层的稀疏度与总稀疏度相等，需要保持第一个layer dense
  - Erdos-Renyi: $s^l = 1-\frac{n^{l-1}+n^l}{n^{l-1}\*n^l}$, $n^l$表示第$l$层neruons数量
  - ERK: 在ER的基础上引入kernel dimensions, number of parameters of the sparse convolutional layers are scaled proportional to $1-\frac{n^{l-1}+n^l+w^l+h^l}{n^{l-1}\*n^l\*w^l\*h^l}$, where $w^l$ and $h^l$ are the width and the height of the $l^{th}$ convolutional kernel
- Update Schedule
  - $\Delta T$: 每两次update之间的iterations数量
  - $T_{end}$: 结束update的iterations数量
  - $\alpha$: initial fraction of connections updated
  - $f_{decay}$: 每$\Delta T$次循环执行一次函数，用于decay the fraction of updated connections
  $$
  f_{decay} = \frac{\alpha}{2}(1+\cos(\frac{t\pi}{T_{end}}))
  $$
- Drop Crition: drop参数绝对值最小的top $K$个connections, $K=f_{decay}\*(1-s^l)N^l$
- Grow Crition: (*Novelty*)在所有的未被保留下来的connections中，magnitude gradients绝对值最大的top $K$会被grow并参数初始化为0
