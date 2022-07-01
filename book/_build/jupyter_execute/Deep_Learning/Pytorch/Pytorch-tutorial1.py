#!/usr/bin/env python
# coding: utf-8

# # Pytorch Tensor Tutorial
# Initializing tensors, math, indexing, reshaping
# ## Tensor Initialization

# In[1]:


import torch

# create a tensor
device = "cuda" if torch.cuda.is_available() else "cpu" # if we have a GPU then use it

my_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], # 2 rows and 3 columns
                         dtype=torch.float32, # float32 type
                         device=device, requires_grad=True) # default device = "cpu"
print(my_tensor)


# We can see the attributes of a tensor like below, which we have defined when initialiazation.

# In[2]:


print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.shape)
print(my_tensor.requires_grad)


# Other initialization methods:

# In[3]:


x = torch.empty(size = (3, 3)) # random values
print(x)


# In[4]:


x = torch.zeros((3, 3)) # zeros values
print(x)


# In[5]:


x = torch.rand((3, 3)) # random values in [0,1]
print(x)


# In[6]:


x = torch.ones((3, 3)) # ones values
print(x)


# In[7]:


x = torch.eye(5, 5) # identity matrix
print(x)


# In[8]:


x = torch.arange(start=0, end=5, step=1) # range[0,5]
print(x)


# In[9]:


x = torch.linspace(start=0.1, end=1, steps=10) # equal cut into parts
print(x)


# In[10]:


x = torch.empty(size = (1, 5)).normal_(mean=0, std=1) # normal distribution
print(x)


# In[11]:


x = torch.empty(size = (1, 5)).uniform_(0, 1) # uniform distribution, same as torch.rand()
print(x)


# In[12]:


x = torch.diag(torch.ones(3)) # diagonal matrix with ones values, same as torch.eye(3, 3)
print(x)


# How to initialize and convert tensors to other types (int, float, double)

# In[13]:


# create an int64 tensor
tensor = torch.arange(4)
# convert it into a boolean tensor
print(tensor.bool())
# convert to int16 tensor
print(tensor.short())
# convert to int64 tensor
print(tensor.long()) # important to use
# convert to float16 tensor
print(tensor.half())
# convert to float32 tensor
print(tensor.float()) # most often to use
# convert to float64 tensor
print(tensor.double())


# Array to Tensor conversion and vice-versa

# In[14]:


import numpy as np
np_array = np.zeros((5, 5))

# array to tensor
tensor = torch.from_numpy(np_array)

# tensor to array
np_array_back = tensor.numpy()
print(tensor)
print(np_array_back)


# ## Tensor Math & Comparison Operations

# In[15]:


x = torch.tensor([1, 2, 3])
y = torch.tensor([9, 8, 7])


# In[16]:


# addition
z1 = torch.empty(3)
torch.add(x, y, out=z1)
print(z1)
# same result
z2 = torch.add(x, y)
print(z2)
# cleanest method
z = x + y
print(z)


# In[17]:


# Substraction
z = x - y
print(z)


# In[18]:


# Division
z = torch.true_divide(x, y) # equal shape of x and y
print(z)


# In[19]:


# inplace operations
t = torch.zeros(3)
t.add_(x)


# In[20]:


t += x # t = t + x
print(x)


# In[21]:


# Exponentiation
z = x.pow(2) # a power of 2 # same as z = x ** 2
print(z)


# In[22]:


# Simple comparison
z = x > 0
print(z)


# In[23]:


# Matrix Multiplication
x1 = torch.rand((2, 5))
x2 = torch.rand((5, 3))
x3 = torch.mm(x1, x2) # matrix 2x3
# same result
x3 = x1.mm(x2)
print(x3)


# In[24]:


# Matrix exponentiation
matrix_exp = torch.rand(5, 5)
matrix_exp.matrix_power(3) # matrix A^3


# In[25]:


# element wise multiplication
z = x * y
print(z)


# In[26]:


# dot product
z = torch.dot(x, y)
print(z)


# In[27]:


# Batch Matrix Multiplication
batch = 32
n = 10
m = 20
p = 30

tensor1 = torch.rand((batch, n, m))
tensor2 = torch.rand((batch, m, p))
out_bmm = torch.bmm(tensor1, tensor2) # shape is (batch, n, p)


# In[28]:


# Example of Broadcasting
x1 = torch.rand((5, 5)) # matrix
x2 = torch.rand((1, 5)) # vector
z = x1 - x2
print(z)


# In[29]:


# other useful tensor operations
sum_x = torch.sum(x, dim=0) # which dimension used to sum over

values, indices = torch.max(x, dim=0) # x.max(dim=0)
values, indices = torch.min(x, dim=0) # x.min(dim=0)

abs_x = torch.abs(x)

z = torch.argmax(x, dim=0)
z = torch.argmin(x, dim=0)

mean_x = torch.mean(x.float(), dim=0)

z = torch.eq(x, y) # which elements are the same
print(z)


# In[30]:


torch.sort(y, dim=0, descending=False) # return values and indices


# In[31]:


z = torch.clamp(x, min=2, max=2) # 将不在范围的值替换为最大/最小值
print(x)
print(z)


# In[32]:


x = torch.tensor([1,0,1,1,1], dtype = torch.bool)
z1 = torch.any(x) # or
z2 = torch.all(x) # and
print(z1, z2)


# ## Tensor Indexing

# In[33]:


# indexing
batch_size = 10
features = 25
x = torch.rand((batch_size, features))

print(x[0].shape) # x[0,:]


# In[34]:


print(x[:,0].shape) # x[:,0]


# In[35]:


print(x[2, 0:10]) # third row, first 10 columns


# In[36]:


x[0,0] = 100
print(x[0])


# In[37]:


# Fancy indexing
x = torch.arange(10)
indices = [2,5,8]
print(x[indices])


# In[38]:


x = torch.rand((3, 5))
rows = torch.tensor([1, 0])
cols = torch.tensor([4, 0])
print(x[rows, cols].shape) # pick out the element of (1,4) and (0,0)


# In[39]:


# More advanced indexing
x = torch.arange(10)
print(x[(x < 2) | (x > 8)]) # pick out smaller than 2 or bigger than 8
print(x[(x < 2) & (x > 8)]) # pick out smaller than 2 and bigger than 8


# In[40]:


print(x[x.remainder(2) == 0]) # remainder == 0


# In[41]:


# useful opertions
print(torch.where(x > 5, x, x*2)) # same as np.where()


# In[42]:


print(torch.tensor([0,0,1,2,2,3,4]).unique()) # return unique elements 


# In[43]:


print(x.ndimension()) # the number of dimensions


# In[44]:


print(x.numel()) # number of elements


# ## Tensor Reshaping

# In[45]:


x = torch.arange(9)

x_3x3 = x.view(3, 3)
x_3x3 = x.reshape(3, 3)
print(x_3x3)


# In[46]:


y = x_3x3.t() # transpose
print(y)
print(y.reshape(9))
print(y.contiguous().view(9))


# In[47]:


x1 = torch.rand((2, 5))
x2 = torch.rand((2, 5))
print(torch.cat((x1, x2), dim=0).shape) # combine 2 tensors by columns
print(torch.cat((x1, x2), dim=1).shape) # combine 2 tensors by rows


# In[48]:


z = x1.view(-1) # number of elements
print(z.shape)


# In[49]:


batch = 64
x = torch.rand((batch, 2, 5))
z = x.view(batch, -1) # keep the dimension of `batch`, and conbine other dimensions
print(z.shape)


# In[50]:


z = x.permute(0, 2, 1) # change the dimension order: 0 to 0, 2 to 1, 1 to 2
print(z.shape)


# In[51]:


x = torch.arange(10) # [10]
print(x.shape)
print(x.unsqueeze(0).shape) # insert 1 at the 0 position of dimension
print(x.unsqueeze(1).shape) # insert 1 at the 1 position of dimension


# In[52]:


x = torch.arange(10).unsqueeze(0).unsqueeze(2) # 1x10x1
print(x.shape)


# In[53]:


z = x.squeeze(2) # delete the dimension of 1 at the position 2
print(z.shape)

