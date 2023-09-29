import numpy as np
from numpy import linalg as la

from sklearn.metrics.pairwise import cosine_similarity

#########################Dot product###########################

a= np.array([3,-4,5])
b= np.array([1,1,-2])

print(a+b)

u = np.array([2,-3,6])
v = np.array([8,2,-3])
print(np.dot(v,u))

#######################L2 norm##############################

print("L2 norm ",np.sqrt(np.sum(u*u)), la.norm(u))

#######################L1 norm##############################

print("L1 norm ", la.norm(u,1))

#######################Cosine Similarity###########################

print("Cosine similarity ", (np.dot(v,u)/(la.norm(u)*la.norm(v))))

#######################Cosine Similarity with sklearn###########################

i1=np.array([-0.89,0.2,0.8])
i2=np.array([0.2,0.4,0.5])
i3=np.array([0.3,-0.9,0.3])
i4=np.array([0.4,0.23,0.4])
i5=np.array([0.34,0.3,-0.1])

print("Cosine similarity Matrix", cosine_similarity([i1,i2,i3,i4,i5]), sep="\n")

##########################2D matrix##############################################

a =np.array([[1,2,-3],[0,-4,1]])
print("dimensions=", a.shape)

b= np.array([[3,2,1],[0,1,0]])

################################Hadamard Product#################################
print("a+b= \n", a+b)

print("Hadamard Product=\n", np.multiply(a,b))

#################################matrix multiplication###########################
a= np.array([[1,3],[2,-1]])
b= np.array([[2,0,-4],[3,-2,6]])

print(a.shape)
print(b.shape)
print("AB= ", a@b)
print("AB =", np.matmul(a,b))

########################ex#######################################

b=np.array([[1,3],[5,3]])

print("f(x)= 2x^2-4x+3: \n", 2*np.dot(b,b)-4*b+3*np.eye(2))
print("g(x)= x^2-4x-12: \n", np.dot(b,b)-4*b-12*np.eye(2))

######################################Determinant##############################

b= np.array([[2,1],[4,0]])
print("Det ", la.det(b))

###############################Inverse##########################################

a= np.array([[5,3],[2,1]])
print("Inverse of a is\n",la.inv(a))
b= np.array([[1,1,0],[1,1,1],[0,2,1]])
print("Inverse of b is\n",la.inv(b))

a= np.array([[3,5],[2,3]])
print("Inverse of a is\n",la.inv(a))
print("Rank of a is\n",la.matrix_rank(a))

b= np.array([[2,2],[4,4]])
##print("Inverse of a is\n",la.inv(b))
print("Rank of a is\n",la.matrix_rank(b))


###########################Solving Vector expression#####################################

a= np.array([[2,1],[3,-5]])
b= np.array([7,4])

inva= la.inv(a)

ans= np.matmul(inva,b)

print(ans)
print(la.solve(a,b))


a= np.array([[1,1,2],[2,3,6],[3,6,10]])
b= np.array([4,10,17])

print(la.solve(a,b))

####################Root of Polynomial#################################

coeff=[-1,-15,-140,500]                                

print("Root are\n", np.roots(coeff))

#######################Eigen values#####################################

a=np.array([[5,-10,-5],[2,14,2],[-4,-8,6]])
print("Eigen value \n", la.eig(a))


#######################Orthonormalization########################################

a= np.array([[3,2],[-4,-6]])
v1=a[0]
v2=a[1]

u1= v1/la.norm(v1)
w2= v2-np.dot(u1,v2)*u1
u2= w2/la.norm(w2)

o_n_a= np.array([u1,u2])

print("Orthonormalized=\n", o_n_a)



